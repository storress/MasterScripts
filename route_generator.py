import csv
import xml.etree.ElementTree as ET
from numpy import random


tree = ET.parse('rutas_win/test.rou.xml')
root = tree.getroot()

vehicle_number = 18
depart_time = 36
routes = ['route_0', 'route_2']
exp_departure_time = random.exponential(1, 318)
for number in range(vehicle_number, 300):

    depart_time += exp_departure_time[number]
    route_selector = random.randint(0, 1)
    vehicle = ET.Element('vehicle', {'id': 'vehicle_' + str(number), 'type': 'DEFAULT_VEHTYPE',
                                     'depart': str(float(depart_time)), 'route': routes[route_selector]})

    root.append(vehicle)

tree.write('rutas_win/test_generatedExp.rou.xml')
