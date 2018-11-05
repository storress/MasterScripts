import xml.etree.ElementTree as ET

#initialize xml trees
tree = ET.parse('rutas/rutas-sin-reemplazos0k-110k.xml')
root = tree.getroot()
filtradas = ET.parse('rutas/rutas-filtradas.xml')
rootFiltradas = filtradas.getroot()

counter = 0
#search for specific edge in list of edges
for vehicle in root.iter('vehicle'):
    for route in vehicle.iter('route'):
        edges = route.get('edges')
        #specific edge to find
        if edges.find('-32038440#12') != -1:
            counter = counter +1
            rootFiltradas.append(vehicle)

print(counter)

filtradas.write('rutas/rutas-filtradas.xml')