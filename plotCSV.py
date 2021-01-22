import csv
import math

import matplotlib.pyplot as plt
import time
import datetime

r = 6371000


def to_xy(point, r, cos_phi_0):
    lam = point[0]
    phi = point[1]
    return r * math.radians(lam) * cos_phi_0, r * math.radians(phi)


posX = []
posY = []
timer = 1
times = []
msg_counter = 0
filled_data = []
data = []
previous = ''
with open('trazas_reales/cleaned_logs/test2.csv', 'r') as archivo:
    reader = csv.reader(archivo, delimiter=',')
    next(reader)
    for row in reader:

        aux_x = row[3].split('.')[0]
        aux_dot_x = aux_x[:3] + '.' + aux_x[3:]

        aux_y = row[4].split('.')[0]
        aux_dot_y = aux_y[:3] + '.' + aux_y[3:]
        row[3] = aux_dot_x
        row[4] = aux_dot_y
        if row[0] != previous:
            posX.append(float(aux_dot_x))
            posY.append(float(aux_dot_y))
            times.append(timer)

            timer += 1
            previous = row[0]
        data.append(row)
i = 1
phi_0 = float(data[0][4])
cos_phi_0 = math.cos(math.radians(phi_0))
cartX = []
cartY = []

# transormando de lat,lng a X,Y
processed_data = []
for row in data:
    point = (float(row[3]), float(row[4]))
    point_xy = to_xy(point, r, cos_phi_0)
    processed_data.append([point_xy[0] + 1232000, point_xy[1] + 7857000])
    cartX.append(point_xy[0] + 1232000)
    cartY.append(point_xy[1] + 7857000)

data[0].append(datetime.datetime.fromtimestamp(float(data[0][0])) + datetime.timedelta(milliseconds=200))
processed_data[0].append((datetime.datetime.fromtimestamp(float(data[0][0])) +
                          datetime.timedelta(milliseconds=200)).timestamp())
t0 = [0]
while i < len(data):
    prev = data[i - 1]
    row = data[i]
    next_message = int(row[1]) - int(prev[1]) % 255
    if row[1] == '0' and prev[1] == '255':
        next_message = 1
    row.append(prev[5] + datetime.timedelta(milliseconds=200 * next_message))
    processed_data[i].append((prev[5] + datetime.timedelta(milliseconds=200 * next_message)).timestamp())
    distance = math.sqrt((int(row[0]) - int(prev[0])) ** 2 + (int(row[1]) - int(prev[1])) ** 2)
    time_delta = float(processed_data[i][2] - processed_data[i - 1][2])
    t0.append(t0[i-1] + time_delta)
    speed = distance / time_delta
    processed_data[i].append(speed)
    i += 1

for row in processed_data:
    print(row)
# for row in data:
#     print(row)

# Agregar milisegundos a los datos recibidos
# data[0].append(datetime.datetime.fromtimestamp(float(data[0][0])))
# while i < len(data):
#     # TODO: Agregar 200 milisegundos a mensajes contiguos dentro del mismo segundo
#     # TODO: Encontrar mensajes faltantes y asignar tiempos correctamente
#     row = data[i]
#
#     prev = data[i - 1]
#     delta_s = 0
#     if row[0] == prev[0]:
#         delta_s = 200 * (int(row[1]) - int(prev[1]))
#         row.append(datetime.datetime.fromtimestamp(float(row[0])) + datetime.timedelta(milliseconds=delta_s))
#
#     i += 1
#     print(row)
# for index, row in enumerate(data):
#     full_date = (datetime.datetime.fromtimestamp(float(row[0])) +
#                  datetime.timedelta(milliseconds=200))

# print(full_date)
# print(len(data))

x = [row[0] for row in processed_data]
y = [row[1] for row in processed_data]
v = [row[3] for row in processed_data[1:]]
t = range(1, len(processed_data))
plt.figure(1)
plt.plot(y, x)
plt.figure(2)
plt.plot(t0[1:], v)
plt.show()
# plt.plot(cartY, cartX)
# plt.plot(posY, posX)
# plt.show()
