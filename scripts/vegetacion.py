"""
conda install mkl mkl-service
Detection of vegetation
**Parallelo**
Ruben E Acosta
"""
import numpy as np
import cv2
from skimage import io, color

f1 = io.imread('image.png')
dim = f1.shape

x = np.array([335,804,594])
y = np.array([357,316,550])

xmax = max(x)
ymax = max(y)
xmin = min(x)
ymin = min(y)
lx = xmax-xmin
ly = ymax-ymin

f2 = np.zeros((ly,lx,4))
f3 = np.ones((ly, lx, 4))
f3 = f1[ymin:ymax,xmin:xmax]
mask = np.zeros(f3.shape[:2],dtype = 'uint8')

X = x - xmin
Y = y - ymin
rc = np.array((X,Y)).T

cv2.drawContours(mask,[rc],0,1,-1)

for i in range(ly):
  for j in range(lx):
    r = f3[i,j,0]
    g = f3[i,j,1]
    b = f3[i,j,2]
    if(g<=r or g<=b):
      pass
    else:
      
      f2[i,j,0] = 250
      f2[i,j,2] = 90
      f2[i,j,3] = 0.5

f2[:,:,0] = f2[:,:,0]*mask
f2[:,:,1] = f2[:,:,1]*mask
f2[:,:,2] = f2[:,:,2]*mask
f2[:,:,3] = f2[:,:,3]*mask

io.imshow(f3)
io.imshow(f2)

io.show()
