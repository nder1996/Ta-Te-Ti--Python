import os
import sys
import time


def Bienvenido():
    print("\n\t        ---------------------------------")
    print("\t          Bienvenidos al juego TA-TE-TI")
    print("\t        ---------------------------------\n")

def Inicio():
    Bienvenido()   
    Tablero=[
       ["\t\t\t|","1","|","2","|","3","|"],
       ["\t\t\t|","4","|","5","|","6","|"],
       ["\t\t\t|","7","|","8","|","9","|"]
       ]
    return Tablero

def GanarFinal(Ganador,NJugador):
       print("\t     ------------------------------------------")
       print("\t        F E L I C I D A D E S  G A N A S T E ")
       print("\t     ------------------------------------------\n")
       print("\t\t   Jugador {} Con El Simbolo : {} ".format(NJugador,Ganador),"\n\n")

def Verificador(Simbolo,Tablero):
        c = 0 ; a = 3 ; b = 7 ;
        for x in range(a):
            for y in range(1,b,2):
                if Tablero[x][y] == Simbolo:
                    c+=1
                    if c==3: 
                        return True
                        a = 0 ; b = 0
                else:
                    break      
            c = 0
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 7
           for y in range(1,b,2):
                for x in range(a):
                    if Tablero[x][y] == Simbolo:
                       c+=1
                       if c==3: 
                           return True
                           a = 0 ; b = 0
                    else:
                        break
                c = 0     
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 1
           for x in range(a):
                if Tablero[x][b] == Simbolo:
                      c+=1
                      if c==3: 
                          return True
                          a = 0
                else:
                    break  
                b += 2    
        if a!=0 :
           c = 0 ; x = 0 ; b = 0
           for y in range(5,b,-2):
                if Tablero[x][y] == Simbolo:
                      c+=1
                      if c==3:
                          return True
                          b = 7
                else:
                    break  
                x += 1
        if b==0:
            c = 0
            for x in range(3):
                for y in range(1,7,2):
                    if Tablero[x][y].isdigit()==False:
                       c+=1
            if c == 9:
               return "Empate"
        return False 

def MTablero(Tab):
    os.system ("cls")
    Bienvenido()
    for i in range(3):
      for j in range(7):
          print(Tab[i][j],end=' ')
      print()

def VPosicion(Posicion,Simbolo,NJugador):
    Posicion = str(input("\n\t  Ingrese la Posicion que desea Jugardor {} -> ({}) : ".format(NJugador,Simbolo)))
    if Posicion.isdigit() == True:
        if int(Posicion)!=0 and int(Posicion)<=9:
           return str(Posicion)
        else:
           print("\t\tPOR FAVOR INGRESE SOLO OPCIONDES DEL 1 - 9")
           VPosicion(Posicion,Simbolo,NJugador)
    else:
        print("\t\tPOR FAVOR INGRESE SOLO OPCIONDES DEL 1 - 9")
        VPosicion(Posicion,Simbolo,NJugador)
                       
def Juego(Tab,Simbolo,NJugador):
     c = False ; Posicion = ""
     while c == False:
        Posicion = str(VPosicion(Posicion,Simbolo,NJugador))
        for i in range(3):
            for j in range(7):
                if Tab[i][j] == Posicion:
                    Tab[i][j]=Simbolo
                    print("\n");MTablero(Tab);print("\n")
                    return Tab
        Bienvenido()
        print("\n");MTablero(Tab);print("\n")
        print("\n\tPOR FAVOR INGRESE SU SIMBOLO EN UNA UBICACIÓN DISPONIBLE")
        c == False
        
def Menu():
    Bienvenido()
    print("""
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |  
        \n
        """)
    Opcion = int(input("\t\tIngrese El Numero 1 Para Jugar : "))
    os.system ("cls")
    TabJuego = Inicio() ; Ganar = False ; b = 9 
    print("\n");MTablero(TabJuego);print("\n") 
    if Opcion == 1:
       while Ganar == False:
          TabJuego = Juego(TabJuego,"X",1)
          Ganar = Verificador("X",TabJuego)
          if Ganar == True:
             GanarFinal("X",1)
             time.sleep(3)
             os.system ("cls")
             Menu()
          if Ganar == False:
             TabJuego = Juego(TabJuego,"O",2)
             if Verificador("O",TabJuego)==True:
                GanarFinal("O",2)
                time.sleep(3)
                os.system ("cls")
                Menu()
          if Verificador("X",TabJuego) == "Empate": 
             print("\t        -------------------------------")
             print("\t\t         HAY EMPATE")
             print("\t        -------------------------------\n")
             time.sleep(3)
             os.system ("cls")
             Menu()
    else:
        os.system ("cls")
        print("\t     POR FAVOR DIGITE El NUMERO 1 PARA JUGAR")
        Menu()


os.system ("cls")  

Menu()

import os
import sys
import time


def Bienvenido():
    print("\n\t        ---------------------------------")
    print("\t          Bienvenidos al juego TA-TE-TI")
    print("\t        ---------------------------------\n")

def Inicio():
    Bienvenido()   
    Tablero=[
       ["\t\t\t|","1","|","2","|","3","|"],
       ["\t\t\t|","4","|","5","|","6","|"],
       ["\t\t\t|","7","|","8","|","9","|"]
       ]
    return Tablero

def GanarFinal(Ganador,NJugador):
       print("\t     ------------------------------------------")
       print("\t        F E L I C I D A D E S  G A N A S T E ")
       print("\t     ------------------------------------------\n")
       print("\t\t   Jugador {} Con El Simbolo : {} ".format(NJugador,Ganador),"\n\n")

def Verificador(Simbolo,Tablero):
        c = 0 ; a = 3 ; b = 7 ;
        for x in range(a):
            for y in range(1,b,2):
                if Tablero[x][y] == Simbolo:
                    c+=1
                    if c==3: 
                        return True
                        a = 0 ; b = 0
                else:
                    break      
            c = 0
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 7
           for y in range(1,b,2):
                for x in range(a):
                    if Tablero[x][y] == Simbolo:
                       c+=1
                       if c==3: 
                           return True
                           a = 0 ; b = 0
                    else:
                        break
                c = 0     
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 1
           for x in range(a):
                if Tablero[x][b] == Simbolo:
                      c+=1
                      if c==3: 
                          return True
                          a = 0
                else:
                    break  
                b += 2    
        if a!=0 :
           c = 0 ; x = 0 ; b = 0
           for y in range(5,b,-2):
                if Tablero[x][y] == Simbolo:
                      c+=1
                      if c==3:
                          return True
                          b = 7
                else:
                    break  
                x += 1
        if b==0:
            c = 0
            for x in range(3):
                for y in range(1,7,2):
                    if Tablero[x][y].isdigit()==False:
                       c+=1
            if c == 9:
               return "Empate"
        return False 

def MTablero(Tab):
    os.system ("cls")
    Bienvenido()
    for i in range(3):
      for j in range(7):
          print(Tab[i][j],end=' ')
      print()

def VPosicion(Posicion,Simbolo,NJugador):
    Posicion = str(input("\n\t  Ingrese la Posicion que desea Jugardor {} -> ({}) : ".format(NJugador,Simbolo)))
    if Posicion.isdigit() == True:
        if int(Posicion)!=0 and int(Posicion)<=9:
           return str(Posicion)
        else:
           print("\t\tPOR FAVOR INGRESE SOLO OPCIONDES DEL 1 - 9")
           VPosicion(Posicion,Simbolo,NJugador)
    else:
        print("\t\tPOR FAVOR INGRESE SOLO OPCIONDES DEL 1 - 9")
        VPosicion(Posicion,Simbolo,NJugador)
                       
def Juego(Tab,Simbolo,NJugador):
     c = False ; Posicion = ""
     while c == False:
        Posicion = str(VPosicion(Posicion,Simbolo,NJugador))
        for i in range(3):
            for j in range(7):
                if Tab[i][j] == Posicion:
                    Tab[i][j]=Simbolo
                    print("\n");MTablero(Tab);print("\n")
                    return Tab
        Bienvenido()
        print("\n");MTablero(Tab);print("\n")
        print("\n\tPOR FAVOR INGRESE SU SIMBOLO EN UNA UBICACIÓN DISPONIBLE")
        c == False
        
def Menu():
    Bienvenido()
    print("""
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |  
        \n
        """)
    Opcion = int(input("\t\tIngrese El Numero 1 Para Jugar : "))
    os.system ("cls")
    TabJuego = Inicio() ; Ganar = False ; b = 9 
    print("\n");MTablero(TabJuego);print("\n") 
    if Opcion == 1:
       while Ganar == False:
          TabJuego = Juego(TabJuego,"X",1)
          Ganar = Verificador("X",TabJuego)
          if Ganar == True:
             GanarFinal("X",1)
             time.sleep(3)
             os.system ("cls")
             Menu()
          if Ganar == False:
             TabJuego = Juego(TabJuego,"O",2)
             if Verificador("O",TabJuego)==True:
                GanarFinal("O",2)
                time.sleep(3)
                os.system ("cls")
                Menu()
          if Verificador("X",TabJuego) == "Empate": 
             print("\t        -------------------------------")
             print("\t\t         HAY EMPATE")
             print("\t        -------------------------------\n")
             time.sleep(3)
             os.system ("cls")
             Menu()
    else:
        os.system ("cls")
        print("\t     POR FAVOR DIGITE El NUMERO 1 PARA JUGAR")
        Menu()


os.system ("cls")  

Menu()
