#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Contar los digitos de un numero real Usando solo estructuras numericas.
ej: 1234.224 cantidad digitos: 7 """

num = input("introduce un digito de las cifras que quieras: ")
c=0
for i in str(num):
	c=c+1
print (c, " Nº Digitos")
