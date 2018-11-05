import xml.etree.ElementTree as ET

tree = ET.parse('rutas/rutas0k-110k.xml')

root = tree.getroot()

#read all routes in <RouteDistribution> and delete all <route probability="0">


# for route in routes.findall('route'):
#     probability = int(route.find('probability').text)
#     if probability == 0:
#         routes.remove(route)
#


for routeDistribution in root.iter('routeDistribution'):
    for route in routeDistribution.findall('route'):
        if route.get('probability'):
            probability = int(route.get('probability'))
            if probability == 0:
                routeDistribution.remove(route)

tree.write('rutas/rutas-sin-reemplazos0k-110k.xml')


