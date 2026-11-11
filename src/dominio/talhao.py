"""Talhao: área da lavoura com uma cultura e sensores.  Responsável: Bryan.

Planejado: área, cultura (associação), sensores (AGREGAÇÃO), __len__ (nº de sensores), __str__/__repr__.
Expõe para as políticas: cultura, ultima_leitura(tipo), historico(tipo, n).
Composição: o Talhao é criado e pertence à Fazenda (ciclo de vida dependente).
Depende de: cultura, sensor, leitura.
"""
