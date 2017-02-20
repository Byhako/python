"""
Me das una fecha y te digo si sera año bifiesto, cuantos dias an 
pasado desde el 15/10/1582, y la fecha en el calendario juliano.

Ruben E Acosta

2016-02-27
"""

import time

print('**************************************************')
print('Enter a date after 14/10/1582 and before 1/1/3700')
print('**************************************************')
A=int(input('Enter the year: '))
if A<1582: print('WRONG YEAR')
M=int(input('Enter the month: '))
if M>12: print('WRONG MONTH')
D=int(input('Enter the day: '))
inicio=time.time()
if D<1 or D>31:  print('WRONG DAY')
if A==1582 and M<=9: print('WRONG DATE')
m=M
if A>1582:
    a=A-1583
else:
    a=0
    if m==9:
        dm1=0
    elif m==10:
        dm1=16
    elif m==11:
        dm1=46

da=int(a*365.242198074) #dias en el numero de años
#dias en meses
if m==1:
    dm=0
elif m==2:
    dm=31
elif m==3:
    dm=59
elif m==4:
    dm=90
elif m==5:
    dm=120
elif m==6:
    dm=151
elif m==7:
    dm=181
elif m==8:
    dm=212
elif m==9:
    dm=243
elif m==10:
    dm=273
elif m==11:
    dm=304
elif m==12:
    dm=334

if A==1582:
    if m==10:
        dm=0
    elif m==11:
        dm=16
    elif m==12:
        dm=46

#verifico si es bisiesto
bi=0
if A%4==0:
    if A%400==0:
        bi=1
    elif A%100!=0:
        bi=1

if bi==1:
    dm=dm+1
    print('Gregorian Leap year')
    print('')
else:
    print('')
##**************************************************
#numero de dias total desde fecha hasta 15/10/1582
if A>1582:
    dg=da+dm+D+77
elif A==1582 and m==10:
    dg=da+dm+D-15
else:
    dg=da+dm+D
print('Gregorian Days:',dg)

if A<3000:
    d=int(dg*365.248/365.246599+1)
else:
    d=int(dg*365.248/365.246599)
print('Julian Days:   ',d)

###*************************************************
#Calculamos el ano juliano
if d<149:
    ano=1582
    anos=0
else:
    anos=int((d-148)/365.25)
    ano=anos+1583
if ano%4!=0:
    ban=1
    
else:
    ban=0
   
print('Julian year: ',ano)

#dias restantes en ano
if ano==1582:
    dr=217+d
else:
    dr=d-148-int(anos*365.25)


#DETERMINO EL MES

if dr>0 and dr<32:
    mes=1
elif dr>31 and dr<62:
    mes=2
elif dr>61 and dr<93:
    mes=3
elif dr>92 and dr<123:
    mes=4
elif dr>122 and dr<152:
    mes=5
elif dr>152 and dr<183:
    mes=6
elif dr>182 and dr<214:
    mes=7
elif dr>213 and dr<244:
    mes=8
elif dr>243 and dr<275:
    mes=9
elif dr>274 and dr<305:
    mes=10
elif dr>304 and dr<336:
    mes=11
elif dr>335:
        mes=12

#hallo cantidad de dias en esos meses
if mes==1:
    dm2=0
elif mes==2:
    dm2=31
elif mes==3:
    dm2=61
elif mes==4:
    dm2=92
elif mes==5:
    dm2=122
elif mes==6:
    dm2=152
elif mes==7:
    dm2=182
elif mes==8:
    dm2=213
elif mes==9:
    dm2=243
elif mes==10:
    dm2=274
elif mes==11:
    dm2=304
elif mes==12:
    dm2=335

df=int(dr-dm2)
print('')
print('*************************')
print('Gregorian calendar date: ')
print('D:',D,'M:',m,'Y:',A,'\n')
print('Julian calendar date: ')
print('D:',df,'M:',mes,'Y:',ano)
print('*************************','\n')

"""
El calendario juliano es usado entre 46 ac y el 4 de octubre de 1582

El calendario juliano toma el año como de 325.25 dias exactos. Este desface hace que se adelante 11.23 minutos por año y entre el año 325dc y 1582dc se acumula un desface de 9.87 dias entre el año tropical y el calendario juliano, pero se aproxima a 10 dias de desface.

Únicamente en el año 46 ac, se contaron 445 días, en vez de los 365 normales, para corregir los desfases del calendario anterior, y se le llamó año de la confusión. Para ello, se agregaron dos meses, entre noviembre y diciembre, uno de 33 días y otro de 34, además del mes intercalado en febrero.

Luego pasaron muchas cosas con la iglesia y el calendario se modifico mucho hasta que se estandarizo en el 44 dc!

Antes de 153dc al año comenzaba el 1 de marzo, pero a partir de este año comienza el 1 de enero.

En el año 321 d. C., el emperador Constantino I el Grande implantó la semana de siete días.

El calendario juliano cuenta como bisiestos uno de cada cuatro años, incluso los seculares. Con este calendario se comete un error de 3 días cada 400 años.

El año tropico dura 365.242198074 dias o 365 dias, 5 horas, 48 minutos, 45.25 segundos.

El calendario gragoriano aproxima el año a 365.2425 dias.

Calendario gregoriano desde el 15 de octubre de 1582.

El primer año bisiesto en calendario gregoriano es 1584.

Un año es bisiesto si es divisible entre 4, excepto el último de cada siglo (aquel divisible por 100), salvo que este último sea divisible por 400.

El papa Gregorio XIII, asesorado por el astrónomo jesuita Christopher Clavius promulgó,el 24 de febrero de 1582, la bula Inter gravísimas en la que establecía que tras el, jueves 4 de octubre de 1582 seguiría el viernes 15 de octubre de 1582. Por tal razón, las fechas del 5 de octubre de 1582 al 14 de octubre de 1582 no existen.

Hay 77 dias entre el 15/10/1582 y 1/1/1583

ya que los meses estan en diferente orden, trabajo por separado para el año 1582 y para los demas.

Primero determino el numero de dias total que hay entre la fecha dada y el 15/10/1582

En el total de dias (d) sumo 77, porque hay 77 dias desde el 15/10/1582 hasta fin de año en gregoriano, y el calculo de las otras cantidades es desde fecha hasta el 1/1/1583.

En linea 68 pongo d<149, porque en calendario juliano fantan 148 dias para acabar el año desde el 4/10 por eso mismo lo resto en la linea 72 y en la 79.

En linea 77 sumo 217 pues hay 217 dias desde inicio de año hasta 4/10.

df,  son los dias que quedan luego de restar la cantidad de dias en meses acumulados al total de dias que teniamos en el año (dias restantes.)
"""
fin=time.time()
print('Tiempo de ejecucion: ', fin-inicio) 