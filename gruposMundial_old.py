#!/usr/bin/python3  
# -*- coding: utf-8 -*

""" Se trata de simular el software creado para tal objeto que según
se van extrayendo las bolas correspondientes a cada país decide a qué
grupo se asigna cumpliendo las restricciones que establece la
competición. Éstas se pueden encontrar fácilmente por la red.

Si no voy equivocado son:

Hay 32 países, de distintas confederaciones: Europa, Sudamérica,
Norteamérica, África, Asia-Oceanía

Hay 4 bombos, con 8 bolas/países cada uno, que ya tienen asignadas las
correspondientes bolas/países según una clasificación establecida por
la FIFA

Hay 8 grupos resultantes del sorteo, con 4 países por grupo
(A,B,C,D,E,F,G,H)

La bola de Rusia, en el bombo número 1, es de distinto color y va a
ser sacada en primer lugar, y asignada al grupo A

Se sacan el resto de las bolas del bombo 1, luego del bombo 2 y así
sucesivamente, de forma aleatoria

Para cada bola extraída se asigna a cada grupo por orden sucesivamente
(A, B, C, ...) siempre y cuando se cumplan la restricción siguiente:

En un grupo no puede haber más de un país de la misma confederación,
salvo por la confederación de Europa que puede haber máximo 2 países
de Europa en el mismo grupo. Si un país no se puede asignar al grupo
correspondiente, se intenta al siguiente grupo por orden, y así
sucesivamente, de forma circular, hasta ser asignado a un grupo. """

"""equipos: Rusia, Brasil, Irán, Japón, México, Bélgica, Corea del
Sur, Arabia Saudí, Inglaterra, Alemania, España, Nigeria, Costa
Rica, Egipto, Polonia, Serbia, Islandia, Francia, Portugal,
Uruguay, Colombia, Argentina, Panamá, Senegal, Marruecos, Túnez,
Suiza, Croacia, Suecia, Dinamarca, Australia y Perú."""
import random 

#creación de los grupos en listas
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
#junto listas grupos en una sola
grupo_all=[a,b,c,d,e,f,g,h]
#creo lista de listas con los equipos
bombo1=["rusia", "argentina", "brasil", "portugal", "alemania", "bélgica", "polonia", "francia"]
bombo2=["españa", "inglaterra", "colombia", "méxico", "Uruguay", "Perú", "suiza", "croacia"]
bombo3=["islandia", "costa_rica", "egipto", "irán", "Dinamarca", "Suecia", "Túnez", "Senegal"]
bombo4=["Serbia", "Nigeria", "Japón", "Panamá", "corea_del_sur", "Arabia_saudí", "Marruecos", "Australia"]
#junto listas equipos en una sola
bomboAll=[bombo1,bombo2,bombo3,bombo4] 
contador=32
#bucle while para sorteo bombo, 32 equipos 32 bolas a sacar.
while contador !=1: 
#funcion random para el sorteo

	#random entre 1 a 4 incluidos(eleccion de bombo)
	bombo=(random.randint(0,3))
	
	#random entre equipo 1 a equip 8 incluidos (elección equipo) 
	pais=(random.randint(0,7))

	#random entre grupo_a - grupo_h 8 grupos donde iran los equipos
	grupo=(random.randint(0,7))

	#despues del sorteo númerico usamos los num random para bombo y pais
	#insertamos equipo al grupo
	#grupo_all.append(bombo,[pais])
	#grupo_all[grupo].append
	print(bomboAll[pais])

	contador=contador-1



	#print (grupo_all)
	"""
	#funcion random para el sorteo bombo B
	#bombo=(random.randint(0,3)) #random entre 1 a 4 incluidos
	pais=(random.randint(0,7)) #random entre equipo 1 a equip 8 incluidos
	#despues del sorteo númerico usamos los num random para bombo y pais
	"""
	#grupo_all.append(bombo2[pais]) # insertamos equipo al grupo
	#print(grupo_all)
	"""#funcion random para el sorteo bombo c """
	#bombo=(random.randint(0,3)) #random entre 1 a 4 incluidos
	#pais=(random.randint(0,7)) #random entre equipo 1 a equip 8 incluidos
	#despues del sorteo númerico usamos los num random para bombo y pais
	#grupo_c.append(bombo3[pais]) # insertamos equipo al grupo
	#print (grupo_c)
	#funcion random para el sorteo bombo d
	#bombo=(random.randint(0,3)) #random entre 1 a 4 incluidos
	#pais=(random.randint(0,7)) #random entre equipo 1 a equip 8 incluidos
	#despues del sorteo númerico usamos los num random para bombo y pais
	#grupo_d.append(bombo3[pais]) # insertamos equipo al grupo
	#print (grupo_d)