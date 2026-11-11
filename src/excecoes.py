"""Hierarquia de exceções do AsperFlow.  Responsável: Rafael.

Planejado: ErroAgro (raiz) -> ErroLeituraSensor, ErroBombaIndisponivel,
ErroCotaExcedida, ErroPersistencia.

Requisito (4.1): superclasse própria + >= 3 subclasses; mensagens úteis; nenhum
`except:` silencioso; uso de `raise ... from`; try/except/else/finally em algum fluxo real.
Depende de: nada. NÃO importe nada do projeto aqui (evita import circular).
Atenção: cada exceção precisa ser lançada em um fluxo real e ter teste; senão é "enfeite" (8.2).
Ordem: PRIMEIRO PR do projeto (todos usam).
"""
