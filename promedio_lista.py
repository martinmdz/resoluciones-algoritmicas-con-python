lista=[]
entero=int(input("Ingrese un valor (0 para finalizar): "))
while entero != 0:
    lista.append(entero)
    entero=int(input("Ingresar valor (0 para finalizar): "))
else :
    sumatoria=sum(lista)
print("La suma de los valores de la lista es: ", sumatoria)

promedio = sumatoria / len(lista)
print("El promedio es: ",promedio)   

