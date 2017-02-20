"""
Encripta y desencripta archivos de texto plano.

Ruben E Acosta

2016-02-27
"""

import time
inicio=time.time()
#**********************************************
def codifico(cadena):
    code='abcdefghijklmnopqrstuvwxyz'
    dic={'a':12,'b':51,'c':39,'d':30,'e':57,'f':54,'g':84,
         'h':27,'i':45,'j':21,'k':18,'l':66,'m':33,'n':81,
         'o':90,'p':48,'q':69,'r':15,'s':93,'t':75,'u':24,
         'v':72,'w':87,'x':78,'y':42,'z':60,' ':13,'"':17,
         '.':19,',':23,':':29,';':31,'¿':11,'?':14,'ñ':99,
         '\n':22,'(':70,')':80,'[':14,']':16,'{':20,'}':94,
         '<':25,'>':26,'+':28,'-':32,'*':34,'/':35,'_':37,
         '¡':38,'!':41,'^':43,'=':44,'@':46,'%':47,'#':52,
         '0':59,'1':61,'2':64,'3':65,'4':67,'5':71,'6':74,
         '7':82,'8':87,'9':97,
        }
    a=[x for x in cadena]  #convierto a lista 
    i=0
    j=1
    while True:
       
        a.insert(j,code[i]) #inserto x
        i+=1
        j+=2
        if i==len(code): i=0
        if j==len(a): break
    b=''
    for i in a:            #convierto a cadena
        b+=i
    b=b[::-1]              #invierto
    
    yy=''
    for i in b:
        try:
            yy+=str(dic[i])
        except:
            yy+=str('98')
            
    return yy 

def descodifico(b):
    dic2={'12':'a','51':'b','39':'c','30':'d','57':'e',
          '54':'f','84':'g','27':'h','45':'i','21':'j',
          '18':'k','66':'l','33':'m','81':'n','90':'o',
          '48':'p','69':'q','15':'r','93':'s','75':'t',
          '24':'u','72':'v','87':'w','78':'x','42':'y',
          '60':'z','13':' ','17':'"','19':'.','23':',',
          '29':':','31':';','11':'¿','14':'?','99':'ñ',
          '22':'\n','98':'X','70':'(','80':')','14':'[',
          '16':']','20':'{','94':'}','25':'<','26':'>',
          '28':'+','32':'-','34':'*','35':'/','37':'_',
          '38':'¡','41':'!','43':'^','44':'=','46':'@',
          '47':'%','52':'#','59':'0','61':'1','64':'2',
          '65':'3','67':'4','71':'5','74':'6','82':'7',
          '87':'8','97':'9',
        }
    
    zz=''    
    for j in range(0,len(b),2):
        i=b[j]+b[j+1]
        zz+=dic2[i]    
    
    c=[x for x in zz]       #convierto a lista
    c=c[::-1] #invierto
    i=1
    while True:
        try:
            del(c[i])
            i+=1
        except:
            break
    d=''        
    for i in c:            #convierto a cadena
        d+=i
    return d 
#**********************************************      
archivo=open('archivo.txt','r')
tex=archivo.read()
texto=''
for i in tex:
    if i=='á':
        j='a'
    elif i=='é':
        j='e'
    elif i=='í':
        j='i'
    elif i=='ó':
        j='o'
    elif i=='ú':  
        j='u'
    else:
        j=i.lower() 
    texto+=j                     
code=codifico(texto)
archivo.close()

nuevo=open('nuevo.txt','w')
nuevo.write(code)
nuevo.close()

archivo=open('nuevo.txt','r')
texto=archivo.read()
code=descodifico(texto)
archivo.close()

nuevo=open('nuevo2.txt','w')
nuevo.write(code)
nuevo.close()


fin=time.time()
print('Tiempo de ejecucion: %6f' %(fin-inicio))

