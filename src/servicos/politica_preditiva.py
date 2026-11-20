"""PoliticaPreditiva (IA, estratégia 2; funcionalidade 4.3-e).  Responsável: João Vitor.

Média móvel das leituras + previsão de chuva simulada. A "previsão" é uma simplificação e deve
ser descrita assim no relatório. Precisa ser DETERMINÍSTICA por seed para comparar com a estratégia 1.
Depende de: politica_irrigacao, talhao.
"""
"""Politica preditiva de irrigação. Responsável: João Vitor."""

import random
from .politica_irrigacao import PoliticaIrrigacao


class PoliticaPreditiva(PoliticaIrrigacao):

    def __init__(self, janela=3, seed=42):
        self.janela = janela
        self.seed = seed

    def decidir(self, talhao):

        if self.janela <= 0:
            raise ValueError("A janela deve ser maior que zero")

        historico = talhao.historico_umidade

        if not historico:
            return talhao.umidade_atual < talhao.cultura.umidade_minima

        leituras = historico[-self.janela:]
        media = sum(leituras) / len(leituras)

        gerador = random.Random(self.seed)
        chuva_prevista = gerador.random() < 0.3

        umidade_minima = talhao.cultura.umidade_minima

        if chuva_prevista:
            return media < umidade_minima * 0.8

        return media < umidade_minima