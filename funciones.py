#!usr/bin/env python
#-*- coding: utf-8 -*- 

#conding-----------
import os
#operative system
#cls windows
#clear linux, MacOS
def menu():	
	os.system("cls")
	print "---------este es mi blog-----------"
	print "seleccione una de nuestras operaciones"
	print "1. suma"
	print "2. resta"
	print "3. multiplicacion"
	print "4. division"

	Noopcion = raw_input("ingrese numero de opcion")
	if Noopcion == "1":
		os.system("cls")
		print "seleccionaste suma"
		suma()
	elif Noopcion == "2":
		print "seleccionaste resta"
		resta()
	elif Noopcion == "3":
		print "seleccionaste multiplicacion"
		multiplicacion()
	elif Noopcion == "4":
		print "seleccionaste division"
		division()
	else: 
		print ("ingresaste un numero de opcion invalido, intentelo de nuevo")	

def suma():
	Dato1 = input("ingrese numero")
	Dato2 = input("ingrese numero")
	ab=Dato1+Dato2
	print "tu resultado es "+ str(ab)
	#a=1
	#b=2
	#print a+b

#def resta():
	#c=3
	#d=1
	#print c-d
#def multiplicacion():
	#e=4
	#f=5
	#print e*f
#def division():
	#g=5
	#h=6
	#print g/h	

# tarea ----------------ciclo while---------------------------	
	






menu()
