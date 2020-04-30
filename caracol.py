#Recorrer una matriz 3*3 en espiral

matriz = [[1,2,3],[4,5,6],[7,8,9]]

for x in matriz.__getitem__(0):
    print(x)

for y in range(1, matriz.__len__()):
    print(matriz[y].__getitem__(-1))    

contador=0
for z in reversed(matriz.__getitem__(matriz.__len__()-1)):
    contador=contador+1
    if contador==1:
        continue
    print(z)

contador=0
for z in matriz.__getitem__(matriz.__len__()-2):
    contador=contador+1
    if contador==matriz.__len__():
        break
    print(z)