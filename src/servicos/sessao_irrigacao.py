"""SessaoIrrigacao: gerenciador de contexto.  Responsável: Rafael.

__enter__ liga a bomba e registra o início; __exit__ desliga a bomba SEMPRE (mesmo com exceção),
registra a duração e NÃO engole a exceção (retorna False/None). Uso: `with SessaoIrrigacao(bomba): ...`
Se a bomba veio de um Semaphore, garanta que ela seja devolvida. Depende de: bomba, excecoes.
"""
