import socket
from math_functions1 import *


def main():
    host = '127.0.0.1'
    port = 5001

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.bind((host,port))

    #mySocket.listen(1)
    #conn, addr = mySocket.accept()
    #print('Connection from: ' + str(addr))

    data = []

    average = 0.0
    total = 0.0
    probGiro = []
    prom = []
    realPosY = []
    realPosX = []
    velocidad = []
    e_velocidad = []
    e_pos_x = []
    e_pos_y = []

    i = 0
    pal_prom = 0
    counter = 0
    nueva_ruta = True
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0
    total_samples = 0
    end_route = False
    detected_turn = False

    while True:
        inc_data, adrr = mySocket.recvfrom(1024)
        decoded_data = inc_data.decode('utf-8')
        print(decoded_data)
        if str(decoded_data) == 'q':
            print('deberia salir del loop')
            break
        #print('from connected user: ' + str(adrr))
        # data = str(data).upper()
        data.append(eval(decoded_data))
        if len(data) > 1:
            print(len(data))
            if data[-2][3] != data[-1][3]:
                del data[:]
                data.append(eval(decoded_data))
                average = 0.0
                total = 0.0
                print('Cambio de ruta')
                print(data)
                print(len(data))
                continue
                # print(i)
            row = data[-2]
            prev_pos_x = float(row[0])
            prev_pos_y = float(row[1])
            prev_velocity = float(row[2])
            current_route = row[3]
            intention = row[5]

            pos_x = float(data[-1][0])
            pos_y = float(data[-1][1])
            velocity = float(data[-1][2])
            current_p = probable_turn(prev_velocity, prev_pos_x, prev_pos_y, velocity, pos_x, pos_y, average)
            # print(current_p[1])
            realPosY.append(pos_y)
            realPosX.append(pos_x)
            probGiro.append(current_p[1])
            velocidad.append(prev_velocity)

            e_velocidad.append(current_p[2][2])
            e_pos_x.append(current_p[2][0])
            e_pos_y.append(current_p[2][1])

            total = total + current_p[1]
            # print(current_p[1])
            average = total / float(pal_prom + 1)
            prom.append(average)
            # print(average)

            if current_p[0] == 1:

                detected_turn = True

                if nueva_ruta:
                    counter += 1
                    nueva_ruta = False
                    if intention == '1':
                        true_positive += 1
                    elif intention == '2':
                        false_positive += 1

                print('Giro detectado en tiempo: ' + str(i+1) + " Prob : " + str(current_p[1]))

            # print(xPos, yPos, velocity)
            # print(nextPosX, nextPosY, nextVelocity)
            # print(i)
            i += 1
            pal_prom += 1
            end_route = False
    total_samples = true_negative + true_positive + false_negative + false_positive
    accuracy = float(true_positive + true_negative) / total_samples
    print('Cantidad de detecciones : ' + str(counter))
    print('True positives : ' + str(true_positive))
    print('False positives : ' + str(false_positive))
    print('True negatives : ' + str(true_negative))
    print('False negatives : ' + str(false_negative))
    print('Total : ' + str(total_samples))
    print('Accuracy : ' + str(accuracy))

            #print(datos[-2], datos[-1])

        #print('sending: ' + str(datos[1]))
        #conn.send(datos[0].encode())

    #conn.close()






if __name__ == '__main__':
    main()
