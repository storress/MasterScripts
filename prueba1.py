from math_functions1 import *
import csv
from time import sleep
import matplotlib.pyplot as plt


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
#with open('pruebas/trazasGiro.csv') as csvfile:
#with open('pruebas/pruebaxs.csv') as csvfile:
#with open('rutas_win/single_intencion.csv') as csvfile:
#with open('rutas/gpsWinConIntencion.csv') as csvfile:
#with open('rutas/routes_with_intention.csv') as csvfile:
#with open('rutas/routes_with_intention.csv') as csvfile:
with open('rutas_win/test_generated_routes_intencion.csv') as csvfile:
    data = [tuple(line) for line in csv.reader(csvfile, delimiter=',')]

# define the first route
current_route = data[0][3]

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
detected = False

#i = 430
#while i < 760:
c = 0
while i < len(data) - 1:
    if current_route != data[i+1][3]:
        end_route = True
        # print(data[i][5], detected_turn)
        current_route = data[i+1][3]
        nueva_ruta = True
        detected = False
        if not detected_turn and data[i][5] == '1':
            false_negative += 1

        elif not detected_turn and data[i][5] == '2':
        #elif data[i][5] == '2':
            true_negative += 1


        detected_turn = False
        # print('cambio de ruta')
        average = 0.0
        total = 0.0
        i += 2


    # print(i)
    row = data[i]
    prev_pos_x = float(row[0])
    prev_pos_y = float(row[1])
    prev_velocity = float(row[2])
    current_route = row[3]
    intention = row[5]

    pos_x = float(data[i + 1][0])
    pos_y = float(data[i + 1][1])
    velocity = float(data[i + 1][2])
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

    if current_p[0] == 1 and not detected:

        detected_turn = True
        if nueva_ruta:
            counter += 1
            nueva_ruta = False
            if intention == '1':
                true_positive += 1
            elif intention == '2':
                false_positive += 1
        #print('Giro detectado en tiempo: ' + str(i + 1) + " Prob : " + str(current_p[1]))
#    if current_p[1] > 0.691:
#        detected = True


    # print(xPos, yPos, velocity)
    # print(nextPosX, nextPosY, nextVelocity)
    # print(i)
    i += 1
    pal_prom += 1
    end_route = False
total_samples = true_negative + true_positive + false_negative + false_positive
accuracy = float(true_positive + true_negative)/total_samples
print('Cantidad de detecciones : ' + str(counter))
print('True positives : ' + str(true_positive))
print('False positives : ' + str(false_positive))
print('True negatives : ' + str(true_negative))
print('False negatives : ' + str(false_negative))
print('Total : ' + str(total_samples))
print('Accuracy : ' + str(accuracy))



plt.figure(1)
plt.subplot(221)
plt.plot(probGiro, label='turn probability')

plt.plot(prom, label='average')
plt.legend()

plt.subplot(222)
plt.plot(velocidad, label='real')
plt.plot(e_velocidad, label='estimada')

#plt.plot(e_pos_x, e_pos_y, label='estimada')
plt.legend()

plt.subplot(223)
plt.plot(velocidad, label='real')
#plt.plot(e_pos_x, e_pos_y, label='estimada')
plt.legend()

plt.subplot(224)
plt.plot(realPosX, realPosY, label='real')
plt.plot(e_pos_x, e_pos_y, label='estimada')


fig, ax1 = plt.subplots()
ax1.plot(realPosX, 'red', label='X position')
plt.xlabel('Data steps [Frequency=10 Hz]', labelpad=5)
plt.ylabel('Position', labelpad=5)
plt.legend()
ax2 = ax1.twinx()
ax2.plot(probGiro, label='Turn Probability')
plt.xlabel('Data steps [Frequency=10 Hz]', labelpad=5)
plt.ylabel('Probability', labelpad=5)
fig.tight_layout()
plt.legend()


plt.figure(3)
plt.plot(probGiro, label='turn probability')
plt.plot(prom, label='average')
plt.xlabel('Data steps [Frequency=10 Hz]', labelpad=5)
plt.ylabel('Probability', labelpad=5)
plt.legend()


plt.figure(4)
plt.plot(velocidad, label='real')
plt.plot(e_velocidad, label='estimated')
plt.xlabel('Data steps [Frequency=10 Hz]', labelpad=5)
plt.ylabel('Velocity [m/s]', labelpad=5)
plt.legend()

plt.figure(5)
plt.plot(realPosX, realPosY, label='real')
plt.plot(e_pos_x, e_pos_y, label='estimated')
plt.xlabel('Position X', labelpad=5)
plt.ylabel('Position Y', labelpad=5)
plt.legend()

#plt.show()
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
