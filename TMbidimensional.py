#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:56:30 2019

@author: fernando
"""

#Use esta Máquina de Turing responsablemente (y bajo su propio riesgo)

import copy

def ConstruccTM():
    TM = []
    numInstrucc = int(input("Elija la cantidad de instrucciones de la máquina. "))
    
    for i in range(numInstrucc):
        cuad = []
        print("\nIntroduzca una cuádrupla")
        cuad.append(input("Introduzca el estado ACTUAL: "))
        cuad.append(input("Introduzca el símbolo ACTUAL: "))
        cuad.append(input("Introduzca el símbolo o movimiento A CAMBIAR: "))
        cuad.append(input("Introduzca el estado A CAMBIAR: "))
        TM.append(cuad)
    return TM    
        

def VerificacionTM(TM):
    verificador = True
    
    for cuad in TM:
        for cuadAux in TM: 
            if(cuad[0]==cuadAux[0] and cuad[1]==cuadAux[1] and not(cuad==cuadAux)):
                   print("La instrucciones", cuad, cuadAux, "no son válidas.")
                   verificador = False 
                   break
        if(verificador):
             continue
        else:
             break
         
    return verificador            

def FuncionamientoDeLaTM(cinta,TM):
    cintaAux = copy.deepcopy(cinta)
    cintaAux2 = []
    cintaCursor = [u"\u2588"]
    print("\n-------\n")
    detencion = False
    posicionCursor = 0
    cursorCinta = 0
    estadoMaquina = 1
    numeroUnos = 0
    print("La posición inicial del programa es: ", posicionCursor, 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[cursorCinta], "\n")
    print(cintaCursor)
    print(cinta)
    print("\n-------\n")
    while(not(detencion)):
        cintaAux2 = []
        cuadActual = []
        for cuad in TM:
            a0 = int(cuad[0])
            if((a0 == estadoMaquina) and (cuad[1] == cinta[cursorCinta])):
                cuadActual.extend(cuad)
                break
                
        if(cuadActual == []):
            detencion = True
        
        if(not(detencion)): 
        
        #Movimientos derecha e izquierda
            if(cuadActual[2] == "R"):
                cintaCursor[cursorCinta] = "-"
                posicionCursor = posicionCursor + 1 
                cursorCinta = cursorCinta + 1
                if(len(cintaCursor)-1<cursorCinta):
                    cintaCursor.append(u"\u2588")
                else:
                    cintaCursor[cursorCinta] = u"\u2588"
                    
            elif(cuadActual[2] == "L"):
                if(cursorCinta==0):
                    cintaAux2.append("B")
                    for elemento in cinta:
                        cintaAux2.append(elemento)
                    cinta = cintaAux2
                    posicionCursor = posicionCursor - 1
                else:
                    cintaCursor[cursorCinta] = "-"
                    posicionCursor = posicionCursor - 1
                    cursorCinta = cursorCinta - 1
                    cintaCursor.append(u"\u2588")
                    
         #Cuando no hay movimientos izquierda y derecha
            if(cuadActual[2]!="R" and cuadActual[2]!="L"):
                cinta[cursorCinta] = cuadActual[2]
        
        #Agrega más espacio si es necesario
            if(len(cinta)-1<cursorCinta):
                cinta.append("B")
        
        #Actualiza el estado de la máquina y regresa un ¡reporte exclusivo!   
            estadoMaquina = int(cuadActual[3]) 
            print("La posición del programa es: ", posicionCursor, 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[cursorCinta],
               "\n donde el cursorCinta está en: ", cursorCinta)
            
            print("\n")
            print(cintaCursor)
            print(cinta)
            print("\n-------\n")
            
       
        else:
            break
        
    print("El programa se detuvo en\n la posición: ", posicionCursor, 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[posicionCursor],
               "\n donde el cursorCinta está en: ", cursorCinta)
            
    print("\n")
    print(cintaCursor)
    print(cinta)
            
    for i in range(len(cinta)):
        if(cinta[i] == "1"):
            numeroUnos = numeroUnos + 1
           
    print("\nEl número de unos que produce la máquina en el input\n", cintaAux, "es", numeroUnos)
    print("\n-------\n")
                  

cinta = []
TM = ConstruccTM()
VerificacionTM(TM)
cintaEntrada = input("Introduzca un input: ") 
for simbolo in cintaEntrada:
    cinta.append(simbolo)
FuncionamientoDeLaTM(cinta,TM) 