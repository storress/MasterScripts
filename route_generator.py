import csv
import xml.etree.ElementTree as ET
from numpy import random

tree = ET.parse('rutas_win/route_density.rou.xml')
root = tree.getroot()

vehicle_number = 0
depart_time = 0
routes = ['route_0', 'route_2']

# exp_departure_time = random.exponential(1, 318)

# TIEMPO EN RECORRER LA CALLE COMPLETA: 21s
regular_departure_time = 3

for number in range(vehicle_number, 300):

    # depart_time += exp_departure_time[number]
    depart_time += regular_departure_time
    route_selector = random.randint(0, 2)
    vehicle = ET.Element('vehicle', {'id': 'vehicle_' + str(number), 'type': 'DEFAULT_VEHTYPE',
                                     'depart': str(float(depart_time)), 'route': routes[route_selector],
                                     'departSpeed': '5.00'})

    root.append(vehicle)

tree.write('rutas_win/density_7vSpeed.rou.xml')
