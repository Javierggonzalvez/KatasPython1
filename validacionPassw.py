#!/usr/bin/python3 
# -*- coding: utf-8 -*-
#MODULO para uso de validation.py
"""Crear un módulo para validación de contraseñas. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:

La contraseña debe contener un mínimo de 8 caracteres. Una contraseña
debe contener letras minúsculas, mayúsculas, números y al menos 1
carácter no alfanumérico."""

def passwValid(passw):
	cont = len(passw)
	z=0
	if cont < 8:
		print("El password ha de contener mas de 8 caracteres : ")
		z=z+1
	#contener : "
	if passw.isalnum()==True:# No alpha numerico
		print("Debe contener algun caracter extraño : ")
		z=z+1
	if passw.islower(): 
	    print("Pon una mayúscula x lo menos : ")
	    z=z+1
	if passw.isupper():
		print(" pon una minuscula x lo menos : ")
	if z==0:
		return(True)
	if z!=0:
		return(False)