# Plano de trabalho - AsperFlow

## 1. Responsáveis (um arquivo = um dono, para evitar conflito de merge)
| Arquivo | Dono |
| --- | --- |
| src/excecoes.py | Rafael |
| src/dominio/leitura.py, sensor.py | João Thiago |
| src/dominio/cultura.py, talhao.py | Bryan |
| src/dominio/bomba.py, alerta.py | Rafael |
| src/dominio/fazenda.py | Kevynson |
| src/servicos/politica_irrigacao.py, politica_limiar.py, politica_preditiva.py, comparador.py | João Vitor |
| src/servicos/sessao_irrigacao.py | Rafael |
| src/servicos/controlador.py (threads) | Kevynson |
| src/persistencia/repositorio_json.py | João Thiago |
| main.py, UML final | Kevynson |

Quem precisa mexer no arquivo de outra pessoa abre PR para ela ou pede a alteração.

## 2. Ordem de implementação do núcleo (Semana 2, prazo 20/11)
Princípio: implementar de baixo para cima no grafo de dependências. Quem depende de algo
ainda não pronto programa contra o contrato (seção 3) e testa com um objeto falso.

- Onda 0 (todos, 1 reunião curta): fechar contratos (seção 3) e decisões abertas (seção 4).
  Rafael abre o PR de src/excecoes.py logo (todos usam; não importa nada do projeto).
- Onda 1 (em paralelo, sem dependência entre si): Rafael: BombaIrrigacao. Bryan: Cultura e
  subclasses. João Thiago: Leitura e Sensor (abstrata). João Vitor: interface PoliticaIrrigacao.
- Onda 2: João Thiago: 3 subclasses de Sensor + simulação. Bryan: Talhao (usa Cultura e Sensor).
  Rafael: Alerta e SessaoIrrigacao (usa Bomba). João Vitor: PoliticaPorLimiar.
- Onda 3 (integração do núcleo): Kevynson: Fazenda (compõe Talhao, agrega Bomba) e um
  script de demonstração do polimorfismo para o check-in. João Vitor: PoliticaPreditiva.
- Semana 3: Controlador (threads), persistência JSON, integração dos erros, testes (>= 6 passando em 27/11).
- Semana 4: comparador das políticas, UML final, README, relatório (Anexo B), vídeo, ensaio.

Marcos internos sugeridos: Ondas 0-1 até 14/11; Onda 2 até 17/11; Onda 3 até 19/11 (folga de 1 dia).

## 3. Contratos a combinar ANTES de programar (propostas, ajustem na reunião)
1. Leitura: sensor_id, tipo (str), valor (float), instante (float/datetime). Imutável.
2. Sensor.ler() -> Leitura. Sensor.registrar(leitura) é concreto: guarda no histórico.
3. Talhao expõe: cultura, ultima_leitura(tipo), historico(tipo, n), sensores.
4. PoliticaIrrigacao.decidir(talhao) -> bool (irrigar agora?). Só métodos abstratos.

## 4. Decisões abertas (alteram o código de mais de uma pessoa)
- D1. Quem é dono do estado físico da umidade? Proposta: o Talhao guarda a umidade simulada
  (protegida por Lock, pois sensor e irrigação mexem nela em threads diferentes). Perguntas:
  como a água irrigada sobe a umidade? como a temperatura aumenta a evaporação? quem avança o "tempo"?
- D2. Onde mora o Semaphore das bombas? Proposta: na Fazenda (ela agrega as bombas).
- D3. O que a persistência salva? Proposta: configuração da fazenda (seed) + resultado de uma simulação.

## 5. Plano de testes (meta: 14, mínimo exigido 12)
- Bryan (2): validação de Cultura; sobrescrita polimórfica entre Soja/Milho/Hortalica.
- João Thiago (4): sensor determinístico com seed; ErroLeituraSensor; salvar/carregar JSON; arquivo corrompido -> ErroPersistencia.
- Rafael (3): bomba indisponível; SessaoIrrigacao desliga a bomba mesmo com exceção; ErroCotaExcedida.
- João Vitor (3): limiar; preditiva; as duas respondem de forma diferente ao mesmo cenário.
- Kevynson (2): teste de concorrência determinístico (cota nunca excedida, sem leituras perdidas); Fazenda compõe Talhoes.

## 6. Fluxo Git
- Branches: feature/<área>-<nome> (ex.: feature/cultura-bryan). Commits pequenos, mensagem clara.
- Cada um configura `git config user.email` com o e-mail da conta do GitHub (senão o commit não conta como seu).
- PR para main, revisão cruzada, aprovação, merge (de preferência merge commit, para preservar os commits de cada autor).
- Todos precisam ter commits (nota individual, seção 8.1 da especificação).
