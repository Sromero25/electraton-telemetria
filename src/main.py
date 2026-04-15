from sensors.sensor import leer_estado

contador = 0
while contador < 5:
	print("Lectura",contador + 1)
	resultado = leer_estado()
	print("Dato:",resultado)
	contador = contador + 1
print("Programa terminado")
