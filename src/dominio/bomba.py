"""BombaIrrigacao.  Responsável: Rafael.

Planejado: id, vazão, estado (ligada/desligada), litros bombeados; ligar()/desligar().
Lança ErroBombaIndisponivel se estiver em uso/quebrada. Contadores mexidos por threads: proteger com Lock.
Depende de: excecoes.
"""


import threading
from src.excecoes import ErroBombaIndisponivel
class BombaIrrigacao:
    def __init__(self, id = str, vazao = float):
        self.id = id
        self.vazao = vazao
        self.estado = True  # False = desligada, True = ligada
        self.total_litros_bombeados = 0
        self.lock = threading.Lock()
        self.lock_vazao = threading.Lock()
        self.lock_id = threading.Lock()
        self.quebrada = False  # Atributo para indicar se a bomba está quebrada

    def ligar(self):

        with self.lock:
            if self.estado:
                try:
                    raise ErroBombaIndisponivel("A bomba já está ligada, não é possível ligar novamente.")
                except ErroBombaIndisponivel as error:
                    print(f"Foi encontrado um erro na bomba: {error}")
            
            elif not self.quebrada and not self.estado:
                self.estado = True
                return print(f"A bomba {self.id} foi ligada com sucesso.")

            else:
                self.quebrada = True
                raise ErroBombaIndisponivel("A bomba está quebrada, não é possível ligar.")
                                  

    def desligar(self):
        with self.lock:
                
            if not self.estado:
                try:
                    raise ErroBombaIndisponivel("A bomba já está desligada, não é possível desligar novamente.")
                except ErroBombaIndisponivel as error:
                    print(f"Foi encontrado um erro na bomba: {error}")
            
            if self.estado:
                self.estado = False
                return print(f"A bomba {self.id} foi desligada com sucesso.")
                

    def estado_atual(self):
        with self.lock:
            if self.estado == True:
                return "A bomba está ligada no momento."
            else:
                return "A bomba está desligada no momento."

    def bombeamento(self, tempo_minutos):
        with self.lock:
            if not self.estado:
                try:    
                    raise ErroBombaIndisponivel("A bomba está desligada, não é possível bombear água.")
                except ErroBombaIndisponivel as error:
                    print(f"Foi encontrado um erro na bomba: {error}")

            if tempo_minutos <= 0:
                    try:
                        raise ValueError("O tempo de bombeamento é inválido. Deve ser um valor positivo.")
                    except ValueError as error:
                        print(f"Foi encontrado um erro: {error}")
            
            litros = self.vazao * tempo_minutos
            self.total_litros_bombeados += litros

        return litros

    def vazao_atual(self):
        with self.lock_vazao:
            return self.vazao

"""BombaIrrigacao.  Responsável: Rafael. AINDA NÃO FINALIZADO."""