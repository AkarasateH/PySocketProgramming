from socket import *
from time import sleep
import random

serverPort = 4000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('The server is ready to receive')

while 1:
  sleepTime = random.randint(1, 4)
  print('Receiving data . . .')
  receivedData, addr = serverSocket.recvfrom(1024)
  print('Received from client:', receivedData.decode())

  sleep(sleepTime)

  serverSocket.sendto(receivedData, addr)


print('Server shutdown.')
sys.exit()
