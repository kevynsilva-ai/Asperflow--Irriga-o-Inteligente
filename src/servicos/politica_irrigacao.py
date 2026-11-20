"""PoliticaIrrigacao: INTERFACE.  Responsável: João Vitor.

Requisito (4.1): classe só com métodos abstratos, implementada por 2+ classes.
Contrato proposto: decidir(talhao) -> bool. Nenhum método concreto aqui.
"""
class PoliticaIrrigacao:
    def decidir(self, talhao):
        raise NotImplementedError("Método decidir() deve ser implementado")