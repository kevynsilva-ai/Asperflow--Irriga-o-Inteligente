"""Controlador concorrente.  Responsável: Kevynson. Semana 3.

Uma thread por sensor -> Queue -> thread consumidora que aciona a política; Lock na cota diária;
Semaphore nas bombas; Event para parar; join() no encerramento.
Cuidados: sem condição de corrida; encerramento limpo (sem threads penduradas); testável
de forma DETERMINÍSTICA. Depende de: fazenda, politicas, sessao_irrigacao, alerta.
"""
