import socket
import csv
from time import sleep

def main():
    host = '127.0.0.1'
    port = 5001

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #mySocket.connect((host, port))

    message = input(' -> ')

    with open('rutas/routes_with_intention.csv') as csvfile:
        rows = [tuple(line) for line in csv.reader(csvfile, delimiter=',')]

        period = 0.1
        #while message != 'q':
        for i, row in enumerate(rows):
            if i > 234:
                break
            sleep(period)
            mySocket.sendto(str(row).encode('utf-8'), (host, port))
        mySocket.sendto('q'.encode(), (host, port))
        mySocket.close()

if __name__ == '__main__':
    main()
