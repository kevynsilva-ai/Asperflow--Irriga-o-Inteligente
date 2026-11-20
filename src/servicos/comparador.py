"""Comparador das políticas.  Responsável: João Vitor (apoio: Kevynson). Semana 4.

Roda a mesma simulação (mesma seed) com cada política e compara consumo de água e
tempo em faixa ideal. Depende de: controlador, fazenda, politicas.
"""
from src.servicos.politica_limiar import PoliticaPorLimiar
from src.servicos.politica_preditiva import PoliticaPreditiva


def comparar_politicas(talhoes):
    limiar = PoliticaPorLimiar()
    preditiva = PoliticaPreditiva()

    resultados = {
        "limiar": 0,
        "preditiva": 0
    }

    for talhao in talhoes:
        if limiar.decidir(talhao):
            resultados["limiar"] += 1

        if preditiva.decidir(talhao):
            resultados["preditiva"] += 1

    return resultados