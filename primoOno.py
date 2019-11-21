#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Leer un Z > 20 y determinar si es primo o no

num=int(input("Introduce un numero menor a 20 : "))
if (num > 20):
	print("Necesitamos un numero menor a 20, puedes hacerlo mejor!")
else:
	if(num%2==0):
		print("El número :"+num+" es primo como tú")
	else:
		print("El número :"+ num +" NO es primo, no como tú")