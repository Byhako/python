import pylab as pl
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
we=0

# Crear una figura de 8x6 puntos de tamano, 80 puntos por pulgada de resolucion
pl.figure(figsize=(8, 6), dpi=80)

##*****************************************************************************
##*****************************************************************************
pl.subplot(2,2,1)

pl.plot(X, C, color="blue", linewidth=2.0, linestyle=':',label="cosine")
pl.plot([we,we],[-np.pi,np.pi],color='k')
pl.plot([-np.pi*1.2,np.pi*1.2],[we,we],color='k')
pl.grid(True)

# Establecer limites
pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

## Ticks
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

pl.legend(loc=0)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

pl.axes([0.25,0.6,0.1,0.1])  #axes([horrizontal,vertical,ancho,alto])
pl.plot(X, S, color="red", linewidth=2.0, linestyle="--",label="sine")

# Establecer limites
pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

## Ticks
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])
##*****************************************************************************
pl.subplot(2,2,2)
pl.plot(X, C, color="blue", linewidth=2.0, linestyle='-',label="cosine")
pl.plot(X, S, color="red", linewidth=2.0, linestyle="-",label="sine")

# Establecer limites
pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

## Moviendo los ejes al centro
ax = pl.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior
ax.xaxis.set_ticks_position('bottom')  #mueve rayitas
ax.spines['bottom'].set_position(('data',0)) #mueve eje
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

## Ticks
pl.xticks([-np.pi, -np.pi/2, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$+\pi/2$', r'$+\pi$'])

pl.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])

pl.legend(loc='upper left')

## Anotacion en puntos
t = 2 * np.pi / 3
pl.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
pl.plot([0, t], [np.cos(t),np.cos(t)],color='blue',linewidth=2.5,linestyle="--")
# pinta linea punteada
pl.scatter([t, ], [np.cos(t), ], 50, color='blue') #pinta punto

pl.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
            xy=(t, np.sin(t)), xycoords='data',
            xytext=(+30, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

pl.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
pl.scatter([t, ],[np.sin(t), ], 50, color='red')

pl.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
            xy=(t, np.cos(t)), xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

## Mejorando las etiquetas

# fondo blancusco semi-transparente para las etiquetas
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.6))

##*****************************************************************************

pl.subplot(2,2,3)
pos=np.arange(6)+0.5
pl.barh(pos,(3,5,2,4,7,6),align='center',color='green')
pl.tick_params(axis='x',colors='black')
pl.tick_params(axis='y',colors='blue')
pl.yticks(pos,('ana','clara','hugo','manu','raul','reno'),rotation=30)
pl.xlabel('Indice sedimento')
pl.ylabel('Candidatos')
pl.title('Sedimento',color='b',size=10)
pl.axis([0.0,7.5,-0.5,6.5])
# axis([xmin,xmax,ymin,ymax])

##*****************************************************************************

pl.subplot(2,2,4, polar=True)

t=np.arange(0,6.5,0.01)
r=np.abs(((3/(4*np.pi))**(1/2))*np.sin(t)*np.cos(t))

pl.plot(t,r,color='r',linewidth=3)
pl.title('Y10',size=10,color='b')
pl.suptitle(r"$MATPLOTLIB$",size=30)
pl.show()
