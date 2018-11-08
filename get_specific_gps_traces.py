import csv

# boundaries: X[11700, 11860], Y[12460, 12580]


filteredTraces = []
topPositionX = 11860.0
bottomPositionX = 11700.0
topPositionY = 12580.0
bottomPositionY = 12460.0

with open('rutas/trazas_gps_filtradas_100ms.txt', 'rb') as csvfile:
    rowReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    counter = 0
    for row in rowReader:
        x_position = float(row[2])
        y_position = float(row[3])

        if bottomPositionX <= x_position <= topPositionX and bottomPositionY <= y_position <= topPositionY:
            row.append(round(float(row[5])/3.6, 2))
            filteredTraces.append(row)

            counter += 1
filteredTraces = sorted(filteredTraces, key=lambda row: row[0], reverse=True)

with open('rutas/important_intersection_traces_100ms.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for trace in filteredTraces:
        employee_writer.writerow(trace)
