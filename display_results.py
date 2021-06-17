import csv
import statistics
import matplotlib.pyplot as plt


def delay_graph(testCase):
    for dato in testCase:
        predTime = float(dato[5]) - float(dato[4])
        dato.append(predTime)

    values = set(map(lambda x: x[2], testCase))
    newlist = [[y for y in testCase if y[2] == x] for x in values]
    thisGraph = []
    for paramRep in newlist:
        maxSpeed = float(paramRep[0][2])
        if maxSpeed == 12.2:
            continue
        predsTime = []
        for rep in paramRep:
            predsTime.append(rep[-1])
        thisGraph.append([maxSpeed, statistics.mean(predsTime), statistics.stdev(predsTime)])

    def first(e):
        return e[0]

    thisGraph.sort(key=first)
    return thisGraph


def pl_graph(testCase):
    for dato in testCase:
        if dato[-1] == '1':
            predTime = float(dato[5]) - float(dato[4])
            dato.append(predTime)
    values = set(map(lambda x: x[1], testCase))
    newlist = [[y for y in testCase if y[1] == x] for x in values]
    thisGraph = []
    for paramRep in newlist:
        packetLoss = float(paramRep[0][1])
        predsIntent = []
        predsTime = []
        for rep in paramRep:
            if rep[-2] == '1':
                predsIntent.append(float(rep[-2]))
                predsTime.append(float(rep[-1]))
        mean_pred = 0
        std_pred = 0
        if len(predsTime):
            mean_pred = statistics.mean(predsTime)
            std_pred = statistics.stdev(predsTime)
        thisGraph.append([packetLoss, len(predsIntent), mean_pred, std_pred])

    def first(e):
        return e[0]

    thisGraph.sort(key=first)
    return thisGraph


# Importar resultados y cargarlos en una lista
with open('resultados1.csv', 'r') as archivo:
    reader = csv.reader(archivo, delimiter=',')
    next(reader)
    data = list(reader)

waveDelay = list(filter(lambda c: c[0] == 'WaveDelay', data))
waveOnlyDelay = list(filter(lambda c: c[0] == 'WaveOnlyDelay', data))
waveLteDelay = list(filter(lambda c: c[0] == 'WaveLteDelay', data))
waveServerDelay = list(filter(lambda c: c[0] == 'WaveServerDelay', data))

graph1 = delay_graph(waveDelay)
graph2 = delay_graph(waveOnlyDelay)
graph3 = delay_graph(waveLteDelay)
graph4 = delay_graph(waveServerDelay)

# x = [row[0] for row in graph1]
# y = [row[1] for row in graph1]
# e = [row[2] for row in graph1]

# grafico 1: WaveDelay Tiempo de predicción/velocidadMáxima
# grafico 2: WaveOnlyDelay Tiempo de predicción/velocidadMáxima
# grafico 3: WaveLteDelay Tiempo de predicción/velocidadMáxima
# grafico 4: WaveServerDelay Tiempo de predicción/velocidadMáxima

plt.figure(1)
plt.errorbar([row[0] for row in graph1], [row[1] for row in graph1], [row[2] for row in graph1])
# plt.title('WaveDelay - [Car - Bike]')
plt.xlabel('Max Speed [m/s]')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(2)
plt.errorbar([row[0] for row in graph2], [row[1] for row in graph2], [row[2] for row in graph2])
# plt.title('WaveOnlyDelay - [Car - RSU - Bike]')
plt.xlabel('Max Speed [m/s]')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(3)
plt.errorbar([row[0] for row in graph3], [row[1] for row in graph3], [row[2] for row in graph3])
# plt.title('WaveLteDelay - [Car - RSU - (Lte) - Bike]')
plt.xlabel('Max Speed [m/s]')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(4)
plt.errorbar([row[0] for row in graph4], [row[1] for row in graph4], [row[2] for row in graph4])
# plt.title('WaveServerDelay - [Car - RSU - Server - Bike]')
plt.xlabel('Max Speed [m/s]')
plt.ylabel('Time to collision [s]')
plt.grid()
#plt.show()


# grafico 5: WavePacketLoss Efectividad/perdidaPaquetes
# grafico 6: WaveOnlyPacketLoss Efectividad/perdidaPaquetes
# grafico 7: WaveLtePacketLoss Efectividad/perdidaPaquetes
# grafico 8: WaveServerPacketLoss Efectividad/perdidaPaquetes

wavePacketLoss = list(filter(lambda c: c[0] == 'WavePacketLoss', data))
waveOnlyPacketLoss = list(filter(lambda c: c[0] == 'WaveOnlyPacketLoss', data))
waveLtePacketLoss = list(filter(lambda c: c[0] == 'WaveLtePacketLoss', data))
waveServerPacketLoss = list(filter(lambda c: c[0] == 'WaveServerPacketLoss', data))

graph5 = pl_graph(wavePacketLoss)
graph6 = pl_graph(waveOnlyPacketLoss)
graph7 = pl_graph(waveLtePacketLoss)
graph8 = pl_graph(waveServerPacketLoss)

plt.figure(5)
plt.plot([row[0] for row in graph5], [row[1]/100 for row in graph5])
# plt.title('WavePacketLoss - [Car - Bike]')
plt.xlabel('Packet Loss %')
plt.ylabel('Accuracy')
plt.grid()
plt.figure(6)
plt.plot([row[0] for row in graph5], [row[2] for row in graph5])
# plt.title('WavePacketLoss - [Car - Bike]')
plt.xlabel('Packet Loss %')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(7)
plt.plot([row[0] for row in graph6], [row[1]/100 for row in graph6])
# plt.title('WaveOnlyPacketLoss - [Car - RSU - Bike]')
plt.xlabel('Packet Loss %')
plt.ylabel('Accuracy')
plt.grid()
plt.figure(8)
plt.plot([row[0] for row in graph6], [row[2] for row in graph6])
plt.xlabel('Packet Loss %')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(9)
plt.plot([row[0] for row in graph7], [row[1]/100 for row in graph7])
# plt.title('WaveLtePacketLoss - [Car - RSU - (Lte) - Bike]')
plt.xlabel('Packet Loss %')
plt.ylabel('Accuracy')
plt.grid()
plt.figure(10)
plt.plot([row[0] for row in graph7], [row[2] for row in graph7])
plt.xlabel('Packet Loss %')
plt.ylabel('Time to collision [s]')
plt.grid()
plt.figure(11)
plt.plot([row[0] for row in graph8], [row[1]/100 for row in graph8])
# plt.title('WaveServerPacketLoss - [Car - RSU - Server - Bike]')
plt.xlabel('Packet Loss %')
plt.ylabel('Accuracy')
plt.grid()
plt.figure(12)
plt.plot([row[0] for row in graph8], [row[2] for row in graph8])
plt.xlabel('Packet Loss %')
plt.ylabel('Time to collision [s]')
plt.grid()

plt.show()
