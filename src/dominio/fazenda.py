"""Fazenda: raiz do domínio.  Responsável: Kevynson.

Planejado: COMPOSIÇÃO com Talhao (a Fazenda cria seus talhões); AGREGAÇÃO com BombaIrrigacao;
cota diária de água (protegida por Lock; levanta ErroCotaExcedida); Semaphore das bombas
(decisão D2). Menos bombas que talhões.
Depende de: talhao, bomba, excecoes.
"""
