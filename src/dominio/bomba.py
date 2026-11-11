"""BombaIrrigacao.  Responsável: Rafael.

Planejado: id, vazão, estado (ligada/desligada), litros bombeados; ligar()/desligar().
Lança ErroBombaIndisponivel se estiver em uso/quebrada. Contadores mexidos por threads: proteger com Lock.
Depende de: excecoes.
"""
