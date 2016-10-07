# CSV Menu
import os
import csv

def menu():

    os.system('cls')

    print "~ ~ ~ ~ ~ Archivos CSV ~ ~ ~ ~ ~"

    print ("Elije una Opcion:\n")

    print ("\t1.Leer.")
    print ("\t2.Insertar.")
    print ("\t3.Salir.")


def leer():
    with open('datos.csv','r') as file:
        datos = csv.reader(file, delimiter = '|')
        for line in datos:
            print line

def insertar():
    
    nombre = str(raw_input("Ingrese nombre: "))
    email = str(raw_input("Ingrese email: "))
    telefono = str(raw_input("Ingrese telefono: "))
    
    with open('datos.csv', 'a') as file:
        datos = csv.writer(file, delimiter = '|')
        datos.writerow([nombre, email, telefono])

while True:

    menu()

    opcionMenu = int(raw_input("\nElige opcion a realizar: "))

    if opcionMenu == 1:
        print ("\nLeer archivo CSV.\n")
        leer()
        print raw_input("\nPulsa enter para continuar.")

    elif opcionMenu == 2:
        print ("\nInsertar al archivo CSV.\n")
        insertar()
        print raw_input("\nPulsa enter para continuar.")

    elif opcionMenu == 3:
		break
    else:
		print ("\nNo has ingresado ninguna opcion correcta...\n")

		print ('\t(O_O) ~ (;_;)')

		print raw_input("\n  Pulsa 3 para continuar.")



