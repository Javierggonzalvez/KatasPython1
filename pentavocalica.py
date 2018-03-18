#!/usr/bin/python3  
# -*- coding: utf-8 -*

"""Introduce una palabra y di si es pentavocálica o no , las palabras pentavocálicas
tienen las cinco vocales por ejemplo:
albaricoque,seculariza.etc."""
x=0
palabra=input("Introduce una palabra : ")
for letra in palabra:
	if letra == "a":
		x=x+1
	if letra == "e":
		x=x+1
	if letra == "i":
		x=x+1 
	if letra == "o":
		x=x+1 
	if letra == "u":
		x=x+1
print(x)
if x >= 5:
	print("La palabra : "+palabra+":  es pentavocálica ")
elif x<5:
	print("La palabra : "+palabra+":  NO es pentavocálica ")