from numpy import *
import matplotlib.pyplot as plt

t=arange(0,6.3,0.01)
r=((sin(t)*sqrt(abs(cos(t))))/(sin(t)+7/5))-2*sin(t)+2
plt.subplot(111, polar=True)
plt.plot(t,r,color='r',linewidth=7)
plt.title('Natalia',size=24,color='b')
plt.show()