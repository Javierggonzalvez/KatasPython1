#!/usr/bin/python3 
# -*- coding: utf-8 -*-

"""Desarrola un guion que reciba un número indeterminado de 
parámetros (como mínimo uno). El guion deberá clasificar los 
argumentos según sean ficheros, directorios u otros y guardar 
los nombres en tres archivos (ficheros.txt, directorio.txt y otros.txt). 
Para finalizar debe mostrar mensajes indicando cuantos eran ficheros
 y mostrar sus nombres, cuantos eran directorios y mostrarlos y 
 cuantos eran otros y mostrarlos."""

import os
route = input("Introduce una ruta : ")

def ls(route = '.'):
	return listdir(ruta)
"""
content  = ls(route == getcwd())
for element in content:
	if os.path.isfile(element):
		f = open("files.txt","w")
		f.write("- "+ element)
		f.close()
	if os.path.isdir(element):
		fdir = open("files.txt","w")
		fdir.write("- "+ element)
		fdir.close()
	print (element)"""

#NO CABAT!!!!!!!!!!!!!!!!!!!!!NO ME COJE BIEN