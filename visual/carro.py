from numpy import *

dato=zeros((6,3),float)
vel=zeros((6,5),float)
pen=zeros((6,5),float)
fre=zeros((6,5),float)
rea=zeros((6,5),float)
dis=zeros((6,5),float)
i=0
learchivo=open('autos.dat','r')
for line in learchivo:
    line=line.split()
            
    if i>0:
        dato[i,0]=float(line[0])
        dato[i,1]=float(line[1])
        dato[i,2]=float(line[2])
        

    i=i+1

learchivo.close() 
print''     
print 'vel(m)         pensado(m)    frenado(m)     reaccion(s)      distancia(m)'
print''
for i in range(1,6):
	vel[i,0]=0.44*dato[i,0]
	pen[i,1]=0.31*dato[i,1]
	fre[i,2]=0.31*dato[i,2]
	rea[i,3]=pen[i,1]/vel[i,0]
	dis[i,4]=pen[i,1]+fre[i,2]
	print vel[i,0],'   |   ',pen[i,1],'   |   ',fre[i,2],'   |   ',rea[i,3],'   |   ',dis[i,4]
	
print''

escribir=open('carro.dat','w')
escribir.write('   vel(m)           pensado(m)     frenado(m)          reaccion(s)              distancia(m)\n')
escribir.write('  \n')
for i in range(1,6):
        escribir.write("%8.1f %17.1f %14.1f %19.1f %27.1f \n"% (vel[i,0],pen[i,1],fre[i,2],rea[i,3],dis[i,4]))

escribir.close()    	
	
	
	
	
	
	
	
	
	
	
	
	
	
