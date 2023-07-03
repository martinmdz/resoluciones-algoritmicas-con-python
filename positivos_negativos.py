print ("Ingrese el asterisco para salir")
while cadena != '*' :
    cadena = input("Escribe un número entero: ")
    numero = float(cadena)
    if numero == 0:
     print("El número ingresado es igual a cero")
    elif numero < 0:
     print("El número ingresado es negativo")
    elif numero > 0:
    print("El número ingresado es positivo")
else:
  print ("Se ha completado la iteracion")