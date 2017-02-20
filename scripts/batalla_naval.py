"""
Batalla naval.

Ruben E Acosta

2016-02-27
"""

import random

tablero = []
T=8

for x in range(0,T):
  tablero.append(["O"] * T)

def print_tablero(tablero):
  for fila in tablero:
    print (" ".join(fila))

print ("Juguemos as la batalla naval!\n")
print_tablero(tablero)
#***********************************************
#                   Barcos
#***********************************************
def fila(tablero):
  return random.randint(0,len(tablero)-1)

def columna(tablero):
  return random.randint(0,len(tablero[0])-1)

f=[]
c=[]

n=3  #numero de barcos
for i in range(n):
    fi=fila(tablero)
    co=columna(tablero)
    l=len(f)
    if l==0:
        f.append(fi)
        c.append(co)
    else:
        s=0
        for j in range(l):
            if f[j]==fi and c[j]==co:
                s+=1
        if s==0:
            f.append(fi)
            c.append(co)
      
#**********************************************
turnos=7
m=n
for turn in range(turnos):
    print('=============')
    print ('   Turn', turn + 1)
    print('=============\n')
    adivina_fila = int(input("Adivina fila: "))
    adivina_columna = int(input("Adivina columna: "))
    entre=0
    for i in range(m):
        if adivina_fila == f[i] and \
           adivina_columna == c[i]:
            print ('Felicitaciones! Hundiste %s de %s barcos' %(n-m+1,n))
            c.remove(c[i])
            f.remove(f[i])
            m-=1
            entre=1
            tablero[adivina_fila][adivina_columna] = "B"
            break
    if entre==0:
        if (adivina_fila not in range(T)) or \
           (adivina_columna not in range(T)):
            print ("Huy, eso ni siquiera esta en el oceano.")
        elif(tablero[adivina_fila][adivina_columna] == "X") or \
            (tablero[adivina_fila][adivina_columna] == "B"):
            print ("Ya dijiste esa.")
        else:
            print ("No tocaste mi barco!")
            tablero[adivina_fila][adivina_columna] = "X"
                
    print('')
    print_tablero(tablero)
    print('')
    if m==0:
        print ('Fin del juego.')
        print ('Genial! hundiste todos los barcos.')
        break
    if turn==turnos-1:
        print ('Fin del juego.')
        if m>1: print('Perdiste, te falto %s barcos.' %(m))
        if m==1: print ('Perdiste, te falto 1 barco.')
    