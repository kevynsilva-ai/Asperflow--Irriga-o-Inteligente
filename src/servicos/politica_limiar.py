"""PoliticaPorLimiar (IA, estratégia 1).  Responsável: João Vitor.

Irriga quando a umidade fica abaixo do mínimo da cultura (polimorfismo: cada Cultura tem o seu mínimo).
Depende de: politica_irrigacao, talhao (pode testar com um Talhao falso).
"""
from .politica_irrigacao import PoliticaIrrigacao


class PoliticaPorLimiar(PoliticaIrrigacao):

    def decidir(self, talhao):
        return talhao.umidade_atual < talhao.cultura.umidade_minima