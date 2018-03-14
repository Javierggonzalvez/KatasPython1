#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Imprimir los números del 1 al 100 e 
imprimir el número excepto si se cumple 
lo siguiente: 
•   Si el número es divisible entre 3, 
entonces debe imprimir la palabra: “Get”. 
•   Si el número es divisible entre 5, 
entonces debe imprimir la palabra: “Up”. 
•   Si el número es divisible 3 y 5, 
entonces debe imprimir la palabra: “GetUp”.
Por ejemplo: 
•   Si el número es 2 va a imprimir 2. 
•   Si el número es 3 va a imprimir "Get". 
•   Si el número es 10 va a imprimir "Up". 
•	Si el número es 15 va a imprimir "GetUp"."""

x=0
while x <= 100:
	if (x%3==0):
		if  (x%5==0):
			print("GetUp")
		print("Get")
	elif (x%5==0):
		if  (x%3==0):
			print("GetUp")
		print("Up")
	else:
		print(x)
	x=x+1