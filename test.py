from math_functions import *
import csv

with open('test4.csv') as file:
    data=[tuple(line) for line in csv.reader(file)]
##for datos in data:
##    vel=float(datos[2]);
##    pos=(float(datos[0]), float(datos[1]))
##    print( probable_turn(vel, pos) )
suma=0
promedio=0
for i in range(len(data)):
    if i+2<len(data):
        vel=float(data[i][2])
        pos=(float(data[i][0]), float(data[i][1]))
        vel_actual=float(data[i+1][2])
        pos_actual=(float(data[i+1][0]), float(data[i+1][1]))
        valor_actual=probable_turn(vel, pos, vel_actual, pos_actual, promedio)
        suma=suma+valor_actual[1]
        promedio=suma/float(i+1)
        if valor_actual[0]==1:
            print("Giro detectado en tiempo " + str(i+1))
