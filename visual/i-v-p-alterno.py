


#CORRIENTE Y VOLTAJE CON UNA SEnAL ALTERNA Y LA POTENCIA.


from pylab import *
from numpy import *
 
t=arange(-2.0,2.0,0.01) #tiempo
w=10  #frecuencia angular
fase=60

i=5*sin(w*t) #corriente
v=10*cos(w*t+fase) #voltaje
p=v*i #potencia

title('CORRIENTE, VOLTAJE Y POTENCIA ALTERNO')

plot(t,i,'r')
plot(t,v,'y')
plot(t,p,'g')

ylabel('TIEMPO')
axis([-2.0,2.0,-20.0,35.0])
show()
