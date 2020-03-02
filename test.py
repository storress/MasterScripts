from math_functions import *
import csv
import matplotlib.pyplot as plt

with open('pruebas/test.csv') as file:
    data=[tuple(line) for line in csv.reader(file, delimiter=',')]
##for datos in data:
##    vel=float(datos[2]);
##    pos=(float(datos[0]), float(datos[1]))
##    print( probable_turn(vel, pos) )
suma=0
promedio=0
counter = 0
fakes = 0
verdaderos = []
currentVehicleId = ''
realPosX = []
realPosY = []
realVel = []
estimatedPosX = []
estimatedPosY = []
estimatedVel = []
probGiro = []
prom = []

for i in range(len(data)):
    if i+2<len(data):
        vel=float(data[i][2])
        pos=(float(data[i][0]), float(data[i][1]))

        #stats
        realPosX.append(pos[0])
        realPosY.append(pos[1])
        realVel.append(vel)
        #############################################

        vel_actual=float(data[i+1][2])
        pos_actual=(float(data[i+1][0]), float(data[i+1][1]))
        valor_actual=probable_turn(vel, pos, vel_actual, pos_actual, promedio)

        #stats
        estimatedPosX.append(valor_actual[2][0])
        estimatedPosY.append(valor_actual[2][1])
        estimatedVel.append(valor_actual[2][2])
        probGiro.append(valor_actual[1])
        #########

        suma=suma+valor_actual[1]
        promedio=suma/float(i+1)
        prom.append(promedio)
        if valor_actual[0] == 1:
            #if currentVehicleId != data[i][3]:
            #    currentVehicleId = data[i][3]
            #    counter += 1
            print("Giro detectado en tiempo " + str(i + 1))
            #print("Giro detectado en tiempo " + str(i+1) + ' id vehiculo: ' + data[i][3] + ' tiempo: ' + data[i][4])
            print("Giro supuesto en ("+data[i][0]+','+data[i][1]+')')



# print(counter)
# print(fakes)
# print(verdaderos)
# print(valor_actual)


plt.figure(1)
plt.subplot(221)
plt.plot(realPosX, realPosY, label='real')
plt.plot(estimatedPosX, estimatedPosY, label='estimado')
plt.legend()




plt.subplot(222)
plt.plot(estimatedVel, label='estimado')
plt.plot(realVel, label='real')
plt.legend()


plt.subplot(224)
plt.plot(probGiro, label='estimado')
plt.legend()

plt.subplot(223)
plt.plot(prom, label='promedio')
plt.legend()
plt.show()



# fig, ax1 = plt.subplots()
#
# ax1.plot(realPosY)
#
# ax2 = ax1.twinx()
#
# ax2.plot(probGiro)
#
# fig.tight_layout()
# plt.show()
