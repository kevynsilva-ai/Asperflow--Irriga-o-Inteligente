"""Sensor (abstrata) e subclasses.  Responsável: João Thiago.

Planejado: Sensor(ABC) com ler() ABSTRATO e registrar() CONCRETO (+ histórico);
SensorUmidadeSolo, SensorTemperatura, SensorChuva sobrescrevendo ler() (>= 3 sobrescritas, uso de super()).
Requisitos: encapsulamento com @property; seed/fonte injetável (teste determinístico);
ler() pode lançar ErroLeituraSensor (raise ... from).
Atenção: SensorTemperatura e SensorChuva devem INFLUENCIAR algo (evaporação, bloqueio/previsão
de chuva); senão são enfeite. Veja decisão D1 em docs/plano_de_trabalho.md.
Depende de: leitura, excecoes.
"""
