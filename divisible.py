#!/usr/bin/python3 
# -*- coding: utf-8 -*-

"""Elaborar un guion que,
dado un intervalo de números  enteros positivos, 
indicado por el usuario, nos muestre cuantos números 
del intervalo son divisibles entre otro, también indicado 
por el usuario."""

divisor = int(input("Introduce una divisor : "))
start = int(input("Introduce un numero donde Empezar la cuenta : "))
end = int(input("Introduce un numero donde Acabar la cuenta : "))
x=start
for x in range(start,end+1):
	if x%divisor==0:
		print(x)
		x=x+1
