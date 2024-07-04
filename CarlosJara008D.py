import os
import time
from random import *
import csv

comunas = ["San Bernardo", "Calera De Tango", "Buin"]
nro_pedido = randint(1, 100)

try:
    with open ("datosPedidos.csv", "x") as pedidos:
        pedidosW = csv.writer(pedidos)
        pedidosW.writerow(["Nro.Ped", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"])
except FileExistsError:
    pass

def reg_pedido():
    global nro_pedido
    nro_pedido = int(nro_pedido)
    nro_pedido += 1
    cant5 = 0
    cant10 = 0
    cant20 = 0
    while True:
        try:
            cliente = input("Ingrese su nombre y apellido: ")
            direccion = input("Ingrese la dirección de su calle: ")
            sector = input("Ingrese su comuna de residencia: ")
            sector = sector.title()
            if sector != "San Bernardo" and sector != "Calera De Tango" and sector != "Buin":
                print("Solo puede ordenar dentro de los sectores San Bernardo, Calera De Tango o Buin.")
                break
            while True:
                try:
                    orden = int(input(f"¿Qué tipo de saco desea pedir?\n1. Saco de 5 kilos\n2. Saco de 10 kilos\n3. Saco de 20 kilos\n4. Finalizar\n"))
                    if orden == 1:
                        cant = int(input("Ingrese la cantidad de sacos de 5 kilos que desea: "))
                        cant5 += cant
                    elif orden == 2:
                        cant = int(input("Ingrese la cantidad de sacos de 10 kilos que desea:"))
                        cant10 += cant
                    elif orden == 3:
                        cant = int(input("Ingrese la cantidad de sacos de 20 kilos que desea:"))
                        cant20 += cant
                    elif orden == 4:
                        break
                    else:
                        print("Debe ingresar un valor dentro del rango (1-4)")
                except ValueError:
                    print("Valor ingresado incorrecto, vuelva a intentarlo")
            nro_pedido = str(nro_pedido)
            cant5 = str(cant5)
            cant10 = str(cant10)
            cant20 = str(cant20)
            with open ("datosPedidos.csv", "a") as pedidos:
                pedidosW = csv.writer(pedidos)
                pedidosW.writerow([nro_pedido, cliente, direccion, sector, cant5, cant10, cant20])
            break
        except ValueError:
            print("Valor ingresado incorrecto, vuelva a intentarlo")   

def listado():
    with open ("datosPedidos.csv", "r") as pedidos:
        pedidosR = csv.reader(pedidos)
        for i in pedidosR:
            print(*i)

def hoja():
    while True:
        try:
            with open ("datosPedidos.csv", "r", newline="") as pedidos:
                pedidosR = csv.reader(pedidos)
                pedidosR = next(pedidosR)
                op = int(input("Seleccione una comuna:\n1. San Bernardo\n2. Calera De Tango\n3. Buin\n"))
                if op == 1:
                    if pedidosR[3] == "San Bernardo":
                        with open ("SanBernardo.txt", "w") as sanBernardo:
                            sanBernardo.write(sanBernardo)
                            sanBernardo(pedidosR)
                    break                     
                elif op == 2:
                    if pedidosR[3] == "Calera De Tango":
                        with open ("CaleraDeTango.txt", "w") as calera:
                            calera.write(calera)
                            calera(calera)
                    break     
                elif op == 3:
                    if pedidosR[3] == "Buin":
                        with open ("Buin.txt", "w") as buin:
                            buin.write(buin)
                            buin(buin)
                    break
                else:
                    print("Debe ingresar un valor dentro del rango (1-3)")
        except ValueError:
                print("Valor ingresado incorrecto, vuelva a intentarlo")
        
def menu():
    while True:
        try:
            op = int(input("1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Salir del programa\n"))
            if op == 1:
                reg_pedido()
            elif op == 2:
                listado()
            elif op == 3:
                hoja()
            elif op == 4:
                print("Gracias por usar el programa.")
                break
            else:
                print("Debe ingresar un valor dentro del rango (1-4)")
        except ValueError:
            print("Valor ingresado incorrecto, vuelva a intentarlo")

menu()