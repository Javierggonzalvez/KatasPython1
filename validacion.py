#!/usr/bin/python3   
# -*- coding: utf-8 -*

""" Crear un módulo para validación de nombres de usuarios. Dicho
módulo, deberá cumplir con los siguientes criterios de aceptación:

El nombre de usuario debe contener un mínimo de 6 caracteres y un
máximo de 12. El nombre de usuario debe ser alfanumérico. Nombre de
usuario con menos de 6 caracteres, retorna el mensaje "El nombre de
usuario debe contener al menos 6 caracteres". Nombre de usuario con
más de 12 caracteres, retorna el mensaje "El nombre de usuario no
puede contener más de 12 caracteres". Nombre de usuario con caracteres
distintos a los alfanuméricos, retorna el mensaje "El nombre de
usuario puede contener solo letras y números". Nombre de usuario
válido, retorna True."""
z=0
#pedir nombre usurio
user = input("introduce tu nombre de usuario : ")
#debe contener un mínimo de 6 caracteres y un máximo de 12.
cont = len(user)
if cont < 6:
	print("Usuario debe tener más de 6 caracteres. ")
	z=z+1
if cont > 12:
	print("Usuario no debe tener más de 12 caracteres. ")
	z=z+1
#contener solo letras y números". Nombre de usuario válido, retorna
if user.isspace()==False: # revisa si hay espacios en blanco
	print("Usuario no puede contener espacios. ")
	z=z+1
if user.isalnum()==False:# alpha numerico
	print("Debe ser alfa númerico, sin caracteres extraños : ")
	z=z+1
if z==0:
	print("True")