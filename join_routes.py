import xml.etree.ElementTree as ET

tree = ET.parse('rutas/rutas_prueba.xml')
treeToAdd = ET.parse('rutas/rutas_prueba_agregar.xml')

root = tree.getroot()

rootToAdd =  treeToAdd.getroot()

#for child in root:
#    for test in child:
#        print(test.tag, test.attrib)


#for elem in root.iter():
#    print(elem.tag)

#prueba = [elem.tag for elem in root.iter()]
#print(prueba)
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

# for elem in rootToAdd:
#     root.append(elem)
#
# tree.write('rutas/probando_agregados.xml')

#get the tree for each routes file
rutas0k_10k = ET.parse('rutas/rutas0k-10k.xml')
rutas10k_30k = ET.parse('rutas/rutas10k-30k.xml')
rutas30k_50k = ET.parse('rutas/rutas30k-50k.xml')
rutas50k_70k = ET.parse('rutas/rutas50k-70k.xml')
rutas70k_90k = ET.parse('rutas/rutas70k-90k.xml')
rutas90k_110k = ET.parse('rutas/rutas90k-110k.xml')

#root for each routes tree
root1 = rutas0k_10k.getroot()
root2 = rutas10k_30k.getroot()
root3 = rutas30k_50k.getroot()
root4 = rutas50k_70k.getroot()
root5 = rutas70k_90k.getroot()
root6 = rutas90k_110k.getroot()

#each root except first root
rootsToAdd = [root2,root3,root4,root5,root6]

#add each element to the first tree
for root in rootsToAdd:
    for elem in root:
        root1.append(elem)

#write the tree to a new file
rutas0k_10k.write('rutas/rutas0k-110k.xml')


