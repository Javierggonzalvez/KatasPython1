#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""El problema consiste en programar una aplicación que reciba como parámetro 
tres números, el valor X, el valor Y y un número N que indica hasta que valor 
se debe contar. Como salida devolverá los N primeros números naturales, pero 
sustituyendo los múltiplos de X por la letra F, los de Y por B y los de ambos por FB.

Ejemplo entrada: 2 7 15
Ejemplo salida: 1 F 3 F 5 F B F 9 F 11 F 13 FB 15"""
def fizzbuzz(x,y,n):  #funciona que recibe 3 parametros, 3 numeros
	for i in range(1,n+1,1):
		if i%x==0 and i%y==0:
			print("FB")
		elif i%x==0:
			print("f")
		elif i%y==0:
			print("b")
		else:
			print(i)
	return (x,y)



x=int(input("Introduce un multiplo : "))
y=int(input("Introduce un multiplo : "))
n=int(input("Introduce el numero hasta donde contar : "))

fizzbuzz(x,y,n)



"""Dados 2 números enteros pares uno inicial (A) y otro final (B), 
imprimir en pantalla una serie que muestre números de 2 en 2 dentro 
de los valores de A y de B. 
Ejemplo: para A=4 y B=10, resultado -> 4 6 8 10.

a=int(input("Introduce numero inicial : "))
b=int(input("Introduce numero final : "))
for i in range(a,b+1,2):
	print(i)
"""