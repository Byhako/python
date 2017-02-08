key = 's'
dic = [[],[]]

#***************************************************************
def anadir():
    a = input('Ingresa palabra en espanol: ')
    b = input('Ingresa palabra en ingles: ')
    dic[0].append(a)
    dic[1].append(b)
#***************************************************************    
def tradu(x):
    ban = input("Introduce la palabra en ingles que deseas Buscar: ")
    
    if(x==1):
        for i in range(len(dic[0])):
            con = 0
            if(ban==dic[1][i]):
                print("La traduccion de %s es %s.\n" %(dic[1][i],dic[0][i]) )
                con = 1
                break
        if(con==0):
            print("Palabra no encontrada.")        
    else:
        for i in range(len(dic[0])):
            con = 0
            if(ban==dic[0][i]):
                print("La traduccion de %s es %s.\n" %(dic[0][i],dic[1][i]) )
                con = 1
                break
        
        if(con==0):
            print("Palabra no encontrada.")        
#***************************************************************    
def traducir():
    op = 0
    while(op<1 or op>2):
        print("Elige que deseas hacer:\n")
        print("(1) Traducir ingles/espanol.")
        print("(2) Traducir espanol/ingles.\n")
        op = int(input('-->'))
    
    if(op==1):
        tradu(1)
    else:
        tradu(2)
             
#//////////////////////////////////////////////////////////////////

while(key=='s' or key=='S'):
    op = 0
    while(op<1 or op>2):
        print("Elige que deseas hacer:\n")
        print("(1) Añadir palabra al traductor.")
        print("(2) Buscar traduccion de palabra.\n")
        op = int(input('-->'))
    
    if(op==1):
        anadir()
    else:
        traducir()
    
    key = input("Otra operacion? (S/N) : ")
    print(" ")