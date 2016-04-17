# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Código responsável por pegar a comunicação com o arduino >

author: Cassiano Kunsch das Neves
last edited: <22/01/2016>
"""

from serial import Serial
import subprocess
import time

def start_communication():
    comport = Serial("COM4", 9600, timeout=1, rtscts=True)

    return comport

def get_serial_port():
    ports = subprocess.getoutput('python -m serial.tools.list_ports').split()

    return ports[0]


#protocolo de comunicação
# # - indetificador de inicio
# 000 - tres digitos para a funcao desejada
# 00000 - cinco digitos para dados
# 00 - erro
# : - para fim da mensagem

# porta = get_serial_port()
# comport = start_communication(porta)
#
PARAM_ASCII = "#temp"

# Time entre a conexao serial e o tempo para escrever (enviar algo)
time.sleep(1.5)  # Entre 1.5s a 2s
comport = start_communication()

# comport.write(PARAM_CARACTER)
comport.write(PARAM_ASCII.encode())

VALUE_SERIAL=comport.readline()
print(VALUE_SERIAL)