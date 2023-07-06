import os
import time
import msvcrt
import numpy

precio_platinum = 1200000
precio_gold = 80000
precio_silver = 50000

concierto = numpy.zeros((10,10), int)

def ver_asiento():
    print(   " 1  2  3  4  5  6  7  8  9  10")
    for x in range(10):
        print(f"FILA {x+1}:", end="  ")
        for y in range(10):
            print(concierto[x][y], end=" ")
        print()

def ver_menu_concierto():
    print("""MENU CONCIERTO:
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganacias totales
    5. Salir""")

def validar_rut():
    while True:
        try:
            rut = int(input("Por favor ingrese su rut, sin puntos ni guion : "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! Rut no valido!")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Por favor ingrese una opcion : "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! La opcion ingresada no es correcta!")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def validar_filas():
    while True:
        try:
            fila = int(input("Ingrese la fila que desea : "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("ERROR! Fila no valida!")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def validar_columnas():
    while True:
        try:
            columna = int(input("Ingrese la fila que desea : "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("ERROR! Fila no valida!")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def cant_entradas():
    while True:
        try:
            cant_ent = int(input("Ingrese cantidad de entradas a comprar, maximo 3 : "))
            if cant_ent >= 1 and cant_ent <= 3:
                return cant_ent
            else:
                print("ERROR! El valor de entradas a exedido las 3")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def ver_opc_entrada():
    print("""VALOR ENTRADAS:
        1. PLATINUM, $120000. (Asientos del 1 al 20).
        2. GOLD, $80000. (Asientos del 21 al 50).
        3. Silver, $50000. (Asientos del 51 al 100.""")

def vali_opc_ent():
    while True:
        try:
            opc_ent = int(input("Ingrese opcion de entradas: "))
            if opc_ent in(1,2,3):
                return opc_ent
            else:
                print("ERROR! Opcion de entrada no es valida!")
        except:
            print("ERROR! Debe ingresar un numero entero!")

def comprar():
    if 0 not in concierto:
        print("NO HAY ASIENTOS DISPONIBLES EN LA SALA!")
    ver_asiento()
    ver_opc_entrada()
    vali_opc_ent()
    cant_entradas()
    while True:
        rut = validar_rut()
        fila = validar_filas()
        columna = validar_columnas()
        if [fila-1][columna-1] == 0:
            [fila-1][columna-1] = 1
            lista_ruts.append(rut)
            lista_filas.append(fila)
            lista_columnas.append(columna)
        else:
            print("El asiento esta ocupado!")

def ver_asistentes():
    print(lista_ruts)

def ganancias():
    print("""Tipo entrada | Cantidad | Total
                Platinum  |     2    | $240000
                Gold      |     4    | $320000
                Silver    |     10   | $50000
                Total     |     16   | $1060000""")






lista_ruts = []
lista_filas = []
lista_columnas = []
        






    


