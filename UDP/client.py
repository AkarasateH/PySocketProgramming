from socket import *
from time import *
import random
import statistics

RETRY = 4
TIMEOUT = 2 # unit as second
MESSAGE = 'TEST'

serverPort = 4000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)
serverNameInput = ''

try:
  serverNameInput = input('ping ')
  print('PING %s (%s): %d data bytes' % (serverNameInput, serverNameInput, len(MESSAGE) * RETRY))
  ttl = random.randint(1, 200)
  modifiedMessage = bytearray()
  timeRec = []

  for i in range(RETRY):
    try:
      encodedMessage = str.encode(MESSAGE)
      startTime = time() * 1000.0
      clientSocket.sendto(encodedMessage, (serverNameInput, serverPort))
      receivedMessage, addr = clientSocket.recvfrom(1024)
      endTime = time() * 1000.0
      timeRec.append(float(endTime - startTime))
      print('{} bytes from {}: icmp_seq={} ttl={} time={} ms'.format(len(receivedMessage), serverNameInput, i, ttl, format(endTime - startTime, '.3f')))
    except Exception as socketError:
      timeRec.append(-1)
      print('Request timeout for icmp_seq', i)
      pass
    sleep(1)

  success = list(filter(lambda x: x >= 0, timeRec))
  print('\n ---', serverNameInput, 'ping statistics ---')
  print(RETRY, 'packets transmitted,', len(success),'packets received,', format(len(list(filter(lambda x: x < 0, timeRec))) / RETRY, '.1f'),'% packet loss')
  print('round-trip min/avg/max/stddev = {}/{}/{}/{} ms'.format(format(min(success),'.3f'), format(sum(success) / len(success),'.3f'), format(max(success),'.3f'), format(statistics.stdev(success),'.3f')))

  clientSocket.close()
except Exception as e:
  print('ping: cannot resolve ' + serverNameInput + ': Unknown host')
  pass
