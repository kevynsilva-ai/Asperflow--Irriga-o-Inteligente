"""
Cobrem a validação das propriedades e a sobrescrita polimórfica entre
Soja, Milho e Hortalica.
"""

import unittest

from src.dominio.cultura import (Cultura, CulturaGraos, Hortalica, Milho,
                                 Soja)


class TestValidacaoCultura(unittest.TestCase):
    def test_cria_cultura_valida(self):
        c = Cultura("Feijão", 58, 72)
        self.assertEqual(c.umidade_minima, 58)
        self.assertEqual(c.umidade_ideal, 72)

    def test_umidade_fora_de_0_a_100_e_recusada(self):
        with self.assertRaises(ValueError):
            Cultura("X", -1, 50)
        with self.assertRaises(ValueError):
            Cultura("X", 50, 101)

    def test_minima_deve_ser_menor_que_ideal(self):
        with self.assertRaises(ValueError):
            Cultura("X", 70, 70)
        with self.assertRaises(ValueError):
            Cultura("X", 80, 60)

    def test_setter_tambem_valida(self):
        c = Cultura("X", 50, 70)
        with self.assertRaises(ValueError):
            c.umidade_minima = 75
        with self.assertRaises(ValueError):
            c.umidade_ideal = 40
        self.assertEqual(c.umidade_minima, 50)  # não mudou

    def test_tipo_invalido_levanta_type_error(self):
        with self.assertRaises(TypeError):
            Cultura("X", "50", 70)
        with self.assertRaises(TypeError):
            Cultura("X", True, 70)

    def test_nome_vazio_e_recusado(self):
        with self.assertRaises(ValueError):
            Cultura("  ", 50, 70)

    def test_ciclo_dias_de_graos_deve_ser_positivo(self):
        with self.assertRaises(ValueError):
            CulturaGraos("Trigo", 50, 70, ciclo_dias=0)


class TestPolimorfismo(unittest.TestCase):
    def test_limiar_difere_entre_soja_milho_e_hortalica(self):
        self.assertEqual(Soja().limiar_irrigacao(), 60)
        self.assertEqual(Milho().limiar_irrigacao(), 55)
        # Hortaliça: 70 (mínima) + 5 (margem)
        self.assertEqual(Hortalica().limiar_irrigacao(), 75)

    def test_mesma_umidade_decide_diferente_por_cultura(self):
        umidade = 72
        self.assertFalse(Soja().precisa_irrigar(umidade))
        self.assertFalse(Milho().precisa_irrigar(umidade))
        self.assertTrue(Hortalica().precisa_irrigar(umidade))

    def test_lista_mista_usa_a_versao_de_cada_classe(self):
        culturas = [Soja(), Milho(), Hortalica()]
        limiares = [c.limiar_irrigacao() for c in culturas]
        self.assertEqual(limiares, [60, 55, 75])

    def test_limiar_da_hortalica_nunca_passa_da_ideal(self):
        h = Hortalica("Alface", 70, 72, margem=10)
        self.assertEqual(h.limiar_irrigacao(), 72)

    def test_subclasses_sao_culturas(self):
        self.assertIsInstance(Soja(), CulturaGraos)
        self.assertIsInstance(Soja(), Cultura)
        self.assertIsInstance(Hortalica(), Cultura)

    def test_str_de_graos_inclui_ciclo(self):
        self.assertIn("120 dias", str(Soja()))
        self.assertIn("Soja", str(Soja()))


if __name__ == "__main__":
    unittest.main()
