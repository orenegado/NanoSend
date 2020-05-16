#-*-coding: utf-8-*-
import socket
h = ""
p = 8010
b = "\n[][][][][][][][][][][][][][][][][]\n"
"""
####################################
# NanoSend v1.0 by: Renegado   #
####################################
"""
try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((h, p))
    sock.listen(2)
    while True:
      print("Esperando msg...")
      cnx, ip = sock.accept()
      try:
        with open("nanosend_log.txt", "a") as fl:
          msg = cnx.recv(4096)
          print("Msg recebida de ", ip)
          fl.write(str(msg.decode("utf-8")))
          fl.write(str(b))
          cnx.send('0'.encode("utf-8"))
      except IOError:
        print("Erro ao abrir log.")
        cnx.send('1'.encode("utf-8"))
        exit()
except KeyboardInterrupt:
  print("\nServidor fechado.")
  cnx.send('1'.encode("utf-8"))
  exit()
