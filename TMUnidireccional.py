#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:56:50 2019

@author: fernando
"""

#Use esta Máquina de Turing responsablemente

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
    cintaAux = [n for i,n in enumerate(cinta) if i%2==0]
    print("\n-------\n")
    detencion = False
    cintaDerecha = [n for i,n in enumerate(cinta) if i%2==0]
    cintaIzquierda = [n for i,n in enumerate(cinta) if i%2==1]
    cintaCursor = [u"\u2588"]
    cintaCursorDerecha = [n for i,n in enumerate(cintaCursor) if i%2==0]
    cintaCursorIzquierda = []
    posicionCursor = 0
    estadoMaquina = 1
    numeroUnos1 = 0
    numeroUnos2 = 0
    numeroUnos = 0
    print("La posición inicial del programa es: ", int(posicionCursor/2), 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[posicionCursor])
    print(cintaCursorDerecha)
    print(cintaDerecha)
    print(cintaIzquierda)
    print(cintaCursorIzquierda)
    print("\n-------\n")
    while(not(detencion)):
        cuadActual = []
        for cuad in TM:
            a0 = int(cuad[0])
            if((a0 == estadoMaquina) and (cuad[1] == cinta[posicionCursor])):
                cuadActual.extend(cuad)
                break
                
        if(cuadActual == []):
            detencion = True
        
        if(not(detencion)): 
        
        #Movimientos derecha e izquierda
            if(cuadActual[2]=="R" or cuadActual[2]=="L"):
                cintaCursor[posicionCursor] = "-"
                if(cuadActual[2] == "R" and posicionCursor%2==0):
                    posicionCursor = posicionCursor + 2 
                    if(len(cintaCursor)<posicionCursor):
                        cintaCursor.append("-")
                        cintaCursor.append(u"\u2588")
                    elif(len(cintaCursor) == posicionCursor):
                        cinta.append(u"\u2588")
                    else:
                        cintaCursor[posicionCursor] = u"\u2588"
                elif(cuadActual[2] == "R" and posicionCursor == 1): 
                    posicionCursor = 0
                    cintaCursor[posicionCursor] = u"\u2588"
                elif(cuadActual[2] == "R" and posicionCursor%2==1 and posicionCursor!=1):
                    posicionCursor = posicionCursor - 2
                    cintaCursor[posicionCursor] = u"\u2588"
                elif(cuadActual[2] == "L" and posicionCursor==0):
                    posicionCursor = 1
                    if(len(cintaCursor)-1<posicionCursor):
                        cintaCursor.append(u"\u2588")
                    else:
                        cintaCursor[posicionCursor] = u"\u2588"
                elif(cuadActual[2] == "L" and posicionCursor%2==1):    
                    posicionCursor = posicionCursor + 2
                    if(len(cintaCursor) < posicionCursor):
                        cintaCursor.append("-")
                        cintaCursor.append(u"\u2588")
                    elif(len(cintaCursor) == posicionCursor):
                        cintaCursor.append(u"\u2588")
                    else:
                        cinta[posicionCursor] = u"\u2588"
                elif(cuadActual[2] == "L" and posicionCursor%2==0 and posicionCursor>0):
                    posicionCursor = posicionCursor - 2
                    cintaCursor[posicionCursor] = u"\u2588"
            else:
                cinta[posicionCursor] = cuadActual[2]
        
            #Agrega más espacio si es necesario
            if(len(cinta)-1<posicionCursor):
                cinta.append("B")
                cinta.append("B")
              
        #Actualiza el estado de la máquina y regresa un ¡reporte exclusivo!   
            estadoMaquina = int(cuadActual[3]) 
            if(posicionCursor%2==0):
                print("La posición del programa es: ", int(posicionCursor/2), 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[posicionCursor], "\n")
            else:
                print("La posición del programa es: ", -int(((posicionCursor+1)/2)), 
                "\n el estado: ", estadoMaquina, 
                "\n marcando el símbolo: ", cinta[posicionCursor], "\n")
            
            #Se muestra la cinta en su versión izquierda y derecha
            cintaDerecha = [n for i,n in enumerate(cinta) if i%2==0]
            cintaIzquierda = [n for i,n in enumerate(cinta) if i%2==1]
            cintaCursorDerecha = [n for i,n in enumerate(cintaCursor) if i%2==0]
            cintaCursorIzquierda = [n for i,n in enumerate(cintaCursor) if i%2==1]
            print("Cinta derecha e izquierda respectivamente (la primera posición de la cinta derecha es cero y \n la primera de la cinta izquierda es -1)\n")
            print(cintaCursorDerecha)
            print(cintaDerecha)
            print(cintaIzquierda)
            print(cintaCursorIzquierda)
            print("\n-------\n")    
       
        else:
            if(posicionCursor%2==0):
                print("El programa se detuvo en\n la posición: ", int(posicionCursor/2), 
               "\n el estado: ", estadoMaquina, 
               "\n marcando el símbolo: ", cinta[posicionCursor], "\n")
            else:
                print("El programa se detuvo en\n la posición: ", -int(((posicionCursor+1)/2)), 
                "\n el estado: ", estadoMaquina, 
                "\n marcando el símbolo: ", cinta[posicionCursor], "\n")
            
            #Se muestra la cinta en su versión izquierda y derecha
            cintaDerecha = [n for i,n in enumerate(cinta) if i%2==0]
            cintaIzquierda = [n for i,n in enumerate(cinta) if i%2==1]
            cintaCursorDerecha = [n for i,n in enumerate(cintaCursor) if i%2==0]
            cintaCursorIzquierda = [n for i,n in enumerate(cintaCursor) if i%2==1]
            print("Cinta derecha e izquierda respectivamente (la primera posición de la cinta derecha es cero y \n la primera de la cinta izquierda es -1)\n")
            print(cintaCursorDerecha)
            print(cintaDerecha)
            print(cintaIzquierda)
            print(cintaCursorIzquierda)
            
            for i in range(len(cintaDerecha)):
                if(cintaDerecha[i] == "1"):
                    numeroUnos1 = int(numeroUnos1 + 1)
                    
            for i in range(len(cintaIzquierda)):
                if(cintaIzquierda[i] == "1"):
                    numeroUnos1 = int(numeroUnos1 + 1)
            
            #Muestra Numero de Unos final
            numeroUnos = int(numeroUnos1 + numeroUnos2)
            print("\nEl número de unos que produce la máquina en el input\n", cintaAux, "es", numeroUnos)
            print("\n-------\n")
            

cinta = []
TM = ConstruccTM()
VerificacionTM(TM)
cintaEntrada = input("Introduzca un input: ")        
for i in range(len(cintaEntrada)):
    cinta.insert(2*i,cintaEntrada[i])
    cinta.insert((2*i)+1,"B")  
FuncionamientoDeLaTM(cinta,TM) 