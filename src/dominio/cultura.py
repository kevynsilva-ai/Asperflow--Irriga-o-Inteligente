"""
Hierarquia (herança em 3 níveis):

    Cultura
    ├── CulturaGraos
    │   ├── Soja
    │   └── Milho
    └── Hortalica

Cada cultura se diferencia pela umidade mínima e pela umidade ideal do
solo (em % de 0 a 100). O comportamento que muda entre as culturas é o
limiar de irrigação: a umidade abaixo da qual vale a pena irrigar.
"""

from __future__ import annotations


def _validar_percentual(valor: float, nome: str) -> float:
    """Garante que ``valor`` é um número entre 0 e 100.

    Levanta TypeError se não for número e ValueError se estiver fora
    da faixa. Usamos os erros padrão do Python porque é um argumento
    inválido (erro de quem chama), não uma falha do domínio do AsperFlow.
    """
    # bool é subclasse de int em Python; True/False não são percentuais.
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError(f"{nome} deve ser um número, recebeu {valor!r}")
    if not 0 <= valor <= 100:
        raise ValueError(f"{nome} deve estar entre 0 e 100, recebeu {valor}")
    return float(valor)


class Cultura:
    """Cultura agrícola com faixa de umidade do solo desejada.

    Atributos:
        nome: nome da cultura.
        umidade_minima: abaixo disso a planta sofre (%).
        umidade_ideal: umidade em que a planta está bem (%); sempre
            maior que a mínima.
    """

    def __init__(self, nome: str, umidade_minima: float,
                 umidade_ideal: float) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("nome da cultura não pode ser vazio")
        self.nome = nome.strip()
        # Começam como None para os setters conseguirem validar a relação
        # mínima < ideal mesmo quando o outro valor ainda não existe.
        self._umidade_minima: float | None = None
        self._umidade_ideal: float | None = None
        self.umidade_minima = umidade_minima
        self.umidade_ideal = umidade_ideal

    # --- encapsulamento: leitura livre, escrita validada ---------------

    @property
    def umidade_minima(self) -> float:
        """Umidade mínima do solo (%)."""
        return self._umidade_minima  # type: ignore[return-value]

    @umidade_minima.setter
    def umidade_minima(self, valor: float) -> None:
        valor = _validar_percentual(valor, "umidade_minima")
        if self._umidade_ideal is not None and valor >= self._umidade_ideal:
            raise ValueError(
                f"umidade_minima ({valor}) deve ser menor que a "
                f"umidade_ideal ({self._umidade_ideal})")
        self._umidade_minima = valor

    @property
    def umidade_ideal(self) -> float:
        """Umidade ideal do solo (%)."""
        return self._umidade_ideal  # type: ignore[return-value]

    @umidade_ideal.setter
    def umidade_ideal(self, valor: float) -> None:
        valor = _validar_percentual(valor, "umidade_ideal")
        if self._umidade_minima is not None and valor <= self._umidade_minima:
            raise ValueError(
                f"umidade_ideal ({valor}) deve ser maior que a "
                f"umidade_minima ({self._umidade_minima})")
        self._umidade_ideal = valor

    # --- comportamento que as subclasses podem sobrescrever -------------

    def limiar_irrigacao(self) -> float:
        """Umidade (%) abaixo da qual a cultura deve ser irrigada.

        Na cultura base é a própria umidade mínima.
        """
        return self.umidade_minima

    def precisa_irrigar(self, umidade_atual: float) -> bool:
        """Diz se a umidade atual pede irrigação.

        Usa limiar_irrigacao(), então cada subclasse muda a decisão só
        sobrescrevendo o limiar (polimorfismo).
        """
        return umidade_atual < self.limiar_irrigacao()

    def __str__(self) -> str:
        return (f"{self.nome} (mín {self.umidade_minima:g}%, "
                f"ideal {self.umidade_ideal:g}%)")

    def __repr__(self) -> str:
        return (f"{type(self).__name__}(nome={self.nome!r}, "
                f"umidade_minima={self.umidade_minima!r}, "
                f"umidade_ideal={self.umidade_ideal!r})")


class CulturaGraos(Cultura):
    """Culturas de grãos, que têm um ciclo de vida longo em dias.

    ``ciclo_dias`` é o atributo próprio que justifica esta classe:
    sem ele, ela seria herança artificial.
    """

    def __init__(self, nome: str, umidade_minima: float,
                 umidade_ideal: float, ciclo_dias: int) -> None:
        super().__init__(nome, umidade_minima, umidade_ideal)
        if (isinstance(ciclo_dias, bool)
                or not isinstance(ciclo_dias, int) or ciclo_dias <= 0):
            raise ValueError(
                f"ciclo_dias deve ser um inteiro positivo, "
                f"recebeu {ciclo_dias!r}")
        self.ciclo_dias = ciclo_dias

    def __str__(self) -> str:
        # super() reaproveita o texto da base e só acrescenta o que é novo.
        return f"{super().__str__()}, ciclo de {self.ciclo_dias} dias"


class Soja(CulturaGraos):
    """Soja, com valores típicos (ilustrativos) já preenchidos."""

    def __init__(self) -> None:
        super().__init__("Soja", umidade_minima=60, umidade_ideal=75,
                         ciclo_dias=120)


class Milho(CulturaGraos):
    """Milho, com valores típicos (ilustrativos) já preenchidos."""

    def __init__(self) -> None:
        super().__init__("Milho", umidade_minima=55, umidade_ideal=70,
                         ciclo_dias=130)


class Hortalica(Cultura):
    """Hortaliças são sensíveis à seca: irrigam ANTES de chegar ao mínimo.

    ``margem`` é quantos pontos percentuais acima da umidade mínima a
    irrigação começa.
    """

    def __init__(self, nome: str = "Hortaliça", umidade_minima: float = 70,
                 umidade_ideal: float = 85, margem: float = 5) -> None:
        super().__init__(nome, umidade_minima, umidade_ideal)
        if isinstance(margem, bool) or not isinstance(margem, (int, float)):
            raise TypeError(f"margem deve ser um número, recebeu {margem!r}")
        if margem < 0:
            raise ValueError(f"margem não pode ser negativa, recebeu {margem}")
        self.margem = float(margem)

    def limiar_irrigacao(self) -> float:
        """Mínima + margem, mas nunca acima da umidade ideal."""
        return min(super().limiar_irrigacao() + self.margem,
                   self.umidade_ideal)
