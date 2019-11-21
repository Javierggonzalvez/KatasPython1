#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys

if len(sys.argv) == 2:
	num = int(sys.argv[1]) 
	if num < 0 or num > 9999:
		print("Error - Númer0 es incorrecto ")
		print("Ejemplo: descomposicion.py [0-9999] ")
	else:
		#Aqui va la logica del programa!
		cadena = str(num) #numero a cadana para utilizar len y saber el num caracteres
		longitud=len(cadena) #numero caracteres que forman el num.

		for i in range(longitud): # la longuitud es 4 dara 4 vueltas
			print("{:04d".format(int(cadena[longitud-1-i] * 10 ** i))
			#pasamos num a 4digitos	 #volvemos d cadena a num sn error

else:

	print("Error - Argumentos incorrectos ")
	print("Ejemplo: descomposicion.py [0-9999] ")