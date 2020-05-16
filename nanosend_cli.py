#-*-coding: utf-8-*-
import socket
import sys
p = 8010
print("""
###########################################
# NanoSend v1.0 by: Renegado              #
###########################################
""")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  try:
    sock.connect((sys.argv[1], p))
    try:
      with open(sys.argv[2], "r") as fl:
        for o in fl.readlines():
          sock.send(o.encode("utf-8")) # erro aqui
        msg = sock.recv(4096).decode("utf-8")
        if msg == 1:
          print("Mensagem não enviada!")
        else:
          print("Mensagem enviada!")
    except IOError:
      print("Impossivel ler arquivo!")
    except IndexError:
      print("Impossivel enviar mensagem!")
  except ConnectionRefusedError:
    print("Servidor off")
