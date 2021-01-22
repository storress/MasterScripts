from os import walk
import re
import csv

mypath = "C:/Users/Salo/src/simulacion_bici/veins-veins-5.0/examples/veins/results/"
_, _, filenames = next(walk(mypath))

tests = [['scenario', 'packetLoss', 'maxSpeed', 'repetition']]

for filename in filenames:
    if '.sca' in filename:
        run_params = re.split('-#|-|,|.sca', filename)
        new_entry = [run_params[0], run_params[1], run_params[2], run_params[4]]
        tests.append(new_entry)
        with open(mypath + filename, 'r') as result:
            data = result.readlines()
        rw = ''
        ct = ''
        pt = ''
        for line in data:
            if 'node[0]' in line and 'receivedWarningTime' in line:
                rw = line.rstrip().split(' ')[3]
            if 'node[1]' in line and 'collisionTime' in line:
                ct = line.rstrip().split(' ')[3]
            if 'rsu[0]' in line and 'predictedTurn' in line:
                pt = line.rstrip().split(' ')[3]
        new_entry.extend([rw, ct, pt])

file = open('resultados1.csv', 'w+', newline='')

with file:
    write = csv.writer(file)
    write.writerows(tests)

print(len(tests))


