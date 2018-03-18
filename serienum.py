#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Dados 2 números enteros pares uno inicial (A) y otro final (B), 
imprimir en pantalla una serie que muestre números de 2 en 2 dentro 
de los valores de A y de B. 
Ejemplo: para A=4 y B=10, resultado -> 4 6 8 10."""

a=int(input("Introduce numero inicial : "))
b=int(input("Introduce numero final : "))
for i in range(a,b+1,2):
	print(i)
