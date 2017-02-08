#pulsos,graficos
from visual.graph import * #importa el numpy para arange y tambien a math

grafico=gdisplay(x=0, y=0, width=500, height=500, title='Pulsos', xmin=0.0, xmax=2, ymin=-2, ymax=2, background=color.white, foreground=color.black, xtitle='ejex')

pulso=gcurve(color=color.red)

for x in arange(0.,5.0,0.01):#punto flotante. range() para enteros
    y=math.sin(30*x)+math.sin(33*x) #produce pulsos
    rate(10) #hace mas lento el dibujo
    pulso.plot(pos=(x,y)) #grafica eje x y eje y
