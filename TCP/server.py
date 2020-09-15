from socket import *
from time import sleep
import random
import threading

serverPort = 4000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

def multiClient(connection):
  while 1:
      sleepTime = random.randint(1, 4)
      print('Receiving data . . .')
      receivedMsg = connection.recv(1024)

      if not receivedMsg: break
      print('Received from client:', receivedMsg.decode())

      sleep(sleepTime)

      connection.send(receivedMsg)

  connection.close()
  print('Client disconnected')

while 1:
  connectionSocket, addr = serverSocket.accept()
  job = threading.Thread(target=multiClient, args=[connectionSocket])
  job.start()

print('Server shutdown.')
sys.exit()
