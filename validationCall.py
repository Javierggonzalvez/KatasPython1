#!/usr/bin/python3 
# -*- coding: utf-8 -*-



"""Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y que los valide utilizando los módulos generados en los dos ejercicios anteriores."""
from validacionPassw import passwValid
from validacion import userValid

us=False
pa=False
#pedir nombre usurio
while us==False:
	user = input("introduce tu nombre de usuario : ")
	us=userValid(user)
	print(userValid(user))
#pedir passw
while pa==False:
	passw = input("introduce un password :  ")
	pa=passwValid(passw)
	print(passwValid(passw))

	
print(userValid(user))
print(passwValid(passw))
