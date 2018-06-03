def printFinobacci(x):

    iteracion=0
    arreglo=[0,1]
    while (iteracion<x):
        arreglo.append(arreglo[-1]+arreglo[-2])
        iteracion +=1
    return arreglo

print(printFinobacci(100))