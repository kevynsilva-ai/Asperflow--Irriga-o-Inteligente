# AsperFlow - Irrigação Inteligente

Simulador de irrigação e monitoramento de lavoura (variação do tema 7, IoT).
Uma fazenda tem talhões, cada um com uma cultura e sensores simulados. Um controlador
lê os sensores em threads e decide quando acionar as bombas, respeitando uma cota diária de água.

POO - Bacharelado em IA - UFCAT/IMTec - Trabalho Final em Grupo

## Equipe
Kevynson Silva (202600450), João Vitor (202501171), João Thiago (202601034),
Bryan (202600446), Rafael (202601032)

## Como executar
```bash
python -m venv .venv && source .venv/bin/activate   # opcional
pip install -r requirements.txt
python main.py          # TODO: documentar o menu
pytest                  # roda os testes
```

## Mapa de conteúdos (Anexo B) - preencher conforme o código for entrando
| Item | OK? | Onde (arquivo/classe) |
| --- | --- | --- |
| >= 8 classes de domínio com `__init__` e métodos coesos | ☐ | |
| Encapsulamento com @property (e validações) | ☐ | |
| `__str__` e `__repr__` (e outros métodos especiais) | ☐ | |
| Composição e agregação/associação | ☐ | |
| Herança com >= 2 níveis e `super()` | ☐ | |
| Polimorfismo com sobrescrita (>= 3 sobrescritas) | ☐ | |
| Classe abstrata (abc) e interface implementada por 2+ classes | ☐ | |
| Hierarquia de exceções própria (>= 3) e try/except/else/finally | ☐ | |
| Classe com `__enter__`/`__exit__` usada em with | ☐ | |
| Threads com sincronização (Lock/Queue) | ☐ | |
| Persistência em JSON/CSV com tratamento de erros | ☐ | |
| >= 12 testes automatizados passando | ☐ | |
| UML inicial e final | ☐ | |
| README com instruções de execução | ☐ | |
| Declaração de uso de IA | ☐ | |

## Estrutura
Veja `docs/plano_de_trabalho.md` (responsáveis, ordem de implementação e contratos entre as classes).

## Uso de ferramentas de IA
TODO (relatório): NotebookLM e Gemini como apoio. Declarar para quê e em quais partes.
