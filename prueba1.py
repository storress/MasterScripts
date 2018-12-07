from math_functions1 import *
import csv
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
with open('rutas/routes_with_intention.csv') as csvfile:
    data = [tuple(line) for line in csv.reader(csvfile, delimiter=',')]

    i = 232
    pal_prom = 0
    #while i < len(data) - 1:
    while i < 394:

        print(i)
        row = data[i]
        prev_pos_x = float(row[0])
        prev_pos_y = float(row[1])
        prev_velocity = float(row[2])

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

        if current_p[0] == 1:
            print('Giro detectado en tiempo: ' + str(i+1) + " Prob : " + str(current_p[1]))

        # print(xPos, yPos, velocity)
        # print(nextPosX, nextPosY, nextVelocity)
        # print(i)
        i += 1
        pal_prom += 1

#
# plt.plot(probGiro, label='prob')
#
# plt.plot(prom, label='prom')
#
# plt.show()
#
#
# plt.plot(realPosX, realPosY)
# plt.show()
plt.figure(1)
plt.subplot(221)
plt.plot(probGiro, label='prob')

plt.plot(prom, label='prom')
plt.legend()

plt.subplot(222)
plt.plot(velocidad, label='velocidad')

#plt.plot(e_pos_x, e_pos_y, label='estimada')
plt.legend()

plt.subplot(223)
plt.plot(velocidad, label='real')
#plt.plot(e_pos_x, e_pos_y, label='estimada')
plt.legend()

plt.subplot(224)
plt.plot(realPosX, realPosY)

fig, ax1 = plt.subplots()
ax1.plot(velocidad, 'r', label='velocity')
ax2 = ax1.twinx()
ax2.plot(realPosX, label='X position')
fig.tight_layout()
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
