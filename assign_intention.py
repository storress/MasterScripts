import csv
import xml.etree.ElementTree as ET



#initialize xml trees
tree = ET.parse('rutas/rutas-filtradas.xml')
root = tree.getroot()
rows = []
right = '-32038440#12 -319929498#2'
straight = '-32038440#12 -32038440#10'
left = '-32038440#12 319929498#3'

with open('rutas/normalized_gps_routes.csv', 'rb') as csvfile:
    rowReader = csv.reader(csvfile, delimiter=',')
    i = 0
    current_route = ''
    intention = ''
    for row in rowReader:
        rows.append(row)

    while i < len(rows) - 1:

        route_id = rows[i][3]
        if current_route == route_id:
            rows[i].append(intention)
            i += 1
            continue

        for vehicle in root.iter('vehicle'):
            if vehicle.attrib['id'] == route_id:
                current_route = route_id
                for route in vehicle.iter('route'):
                    edges = route.get('edges')
                    if edges.find(right) != -1:
                        #print('gira a la derecha')
                        intention = '1'
                        rows[i].append(intention)

                    elif straight != -1:
                        #print('sigue recto')
                        intention = '2'
                        rows[i].append(intention)

                    elif left != -1:
                        #print('gira a la izquierda')

                        rows[i].append(intention)

        #print(rows[i])

        # edges = route.get('edges')
        # print(edges)
        i += 1

with open('rutas/routes_with_intention.csv', mode='w') as routes_file:
    routes_writer = csv.writer(routes_file)

    for route_row in rows:
        routes_writer.writerow(route_row)
