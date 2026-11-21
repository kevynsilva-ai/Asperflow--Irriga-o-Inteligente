"""Testes - responsável: João Vitor.

Planejado: limiar; preditiva; respostas diferentes ao mesmo cenário.
Meta do projeto: >= 12 testes (unittest ou pytest), incluindo exceções e concorrência.
"""

import unittest
from unittest.mock import MagicMock

from src.servicos.politica_limiar import PoliticaPorLimiar
from src.servicos.politica_preditiva import PoliticaPreditiva
from src.servicos.comparar_politicas import comparar_politicas


class TestPoliticaLimiar(unittest.TestCase):

    def setUp(self):
        self.talhao = MagicMock()
        self.talhao.cultura.umidade_minima = 40
        self.politica = PoliticaPorLimiar()

    def test_umidade_abaixo_do_limite(self):
        self.talhao.umidade_atual = 20
        self.assertTrue(self.politica.decidir(self.talhao))

    def test_umidade_acima_do_limite(self):
        self.talhao.umidade_atual = 50
        self.assertFalse(self.politica.decidir(self.talhao))

    def test_umidade_igual_ao_limite(self):
        self.talhao.umidade_atual = 40
        self.assertFalse(self.politica.decidir(self.talhao))


class TestPoliticaPreditiva(unittest.TestCase):

    def criar_talhao(self):
        talhao = MagicMock()
        talhao.umidade_atual = 20
        talhao.cultura.umidade_minima = 40
        talhao.historico_umidade = [20, 25, 30]
        return talhao

    def test_criacao(self):
        self.assertIsNotNone(PoliticaPreditiva())

    def test_janela_padrao(self):
        self.assertEqual(PoliticaPreditiva().janela, 3)

    def test_seed_padrao(self):
        self.assertEqual(PoliticaPreditiva().seed, 42)

    def test_janela_invalida(self):
        with self.assertRaises(ValueError):
            PoliticaPreditiva(janela=0).decidir(self.criar_talhao())

    def test_historico_vazio(self):
        talhao = self.criar_talhao()
        talhao.historico_umidade = []
        self.assertTrue(PoliticaPreditiva().decidir(talhao))

    def test_resultado_deterministico(self):
        talhao = self.criar_talhao()
        p1 = PoliticaPreditiva(seed=42)
        p2 = PoliticaPreditiva(seed=42)
        self.assertEqual(p1.decidir(talhao), p2.decidir(talhao))

    def test_resultado_booleano(self):
        resultado = PoliticaPreditiva().decidir(self.criar_talhao())
        self.assertIsInstance(resultado, bool)

    def test_historico_grande(self):
        talhao = self.criar_talhao()
        talhao.historico_umidade = [20, 25, 30, 35, 40, 45]
        self.assertIsInstance(PoliticaPreditiva().decidir(talhao), bool)

    def test_comparacao_entre_politicas(self):
        talhao = self.criar_talhao()
        talhao.umidade_atual = 35
        talhao.historico_umidade = [35, 35, 35]

        limiar = PoliticaPorLimiar()
        preditiva = PoliticaPreditiva(seed=1)

        self.assertTrue(limiar.decidir(talhao))
        self.assertFalse(preditiva.decidir(talhao))

    def test_janela_personalizada(self):
        self.assertEqual(PoliticaPreditiva(janela=1).janela, 1)


class TestComparacaoPoliticas(unittest.TestCase):

    def test_comparar_politicas(self):
        talhao1 = MagicMock()
        talhao1.umidade_atual = 20
        talhao1.cultura.umidade_minima = 40
        talhao1.historico_umidade = [20, 20, 20]

        talhao2 = MagicMock()
        talhao2.umidade_atual = 50
        talhao2.cultura.umidade_minima = 40
        talhao2.historico_umidade = [50, 50, 50]

        resultado = comparar_politicas([talhao1, talhao2])

        self.assertEqual(resultado["limiar"], 1)
        self.assertEqual(resultado["preditiva"], 1)

    def test_lista_vazia(self):
        resultado = comparar_politicas([])
        self.assertEqual(resultado["limiar"], 0)
        self.assertEqual(resultado["preditiva"], 0)


if __name__ == "__main__":
    unittest.main()