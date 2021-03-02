import csv

# boundaries: X[11800, 11860], Y[12460, 12580] NUEVO BORDE Ymin 12500


filteredTraces = []
# topPositionX = 11845.0
# bottomPositionX = 11800.0
# topPositionY = 12575.0
# bottomPositionY = 12500.0

# adjust the bounding box so we only detect the important intersection
topPositionX = 11900.0
bottomPositionX = 11600.0
topPositionY = 12600.0
bottomPositionY = 12400.0

with open('rutas_win/gps_density_19vSpeed.csv', 'r') as csvfile:
    rowReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    counter = 0
    for row in rowReader:
        x_position = float(row[2])
        y_position = float(row[3])

        if bottomPositionX <= x_position <= topPositionX and bottomPositionY <= y_position <= topPositionY:
            row.append(round(float(row[5])/3.6, 2))
            sorted_row = [x_position, y_position, row[6], row[0], row[1]]
            filteredTraces.append(sorted_row)

            counter += 1
filteredTraces = sorted(filteredTraces, key=lambda row: row[3], reverse=False)

with open('rutas_win/gps_density_19vSpeed_ordenadas.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #employee_writer = csv.writer(employee_file)

    for trace in filteredTraces:
        employee_writer.writerow(trace)
