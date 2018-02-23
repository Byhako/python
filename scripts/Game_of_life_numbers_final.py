# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import os

def Game(img):
    dimy, dimx = img.shape
    # 1: Vivo
    # 0: Muerto
    img_aux = img.copy()
    for y in range(dimy):
        for x in range(dimx):
            suma = np.sum(img[max(y - 1, 0):min(y + 2, dimy), max(x - 1, 0):min(x + 2, dimx)]) - img[y, x]
            if img[y,x] == 1:
                # Está vivo
                if suma < 2 or suma > 3:
                    # Si hay menos de 2 vivos alrededor, muere por soledad
                    # Si hay más de 3 vivos alrededor, muere por sobrepoblación
                    img_aux[y,x] = 0
                    # Si hay 2 o 3 vivos alrededor, sobrevive
            elif suma == 3:
                # Está muerto
                # Si hay exactamente 3 vivos alrededor, nace "por reproducción"
                img_aux[y,x] = 1
    return img_aux

def CreateNumbers(ax, img):
    dimy, dimx = img.shape
    for y in range(dimy):
        for x in range(dimx):
            if img[y, x]==1:
                ax.text(x - 0.5, y + 0.5, str(1), color="lime", fontsize=8)#, fontweight='bold')

# BEGIN

path = './GOF_figures'
if not os.path.exists(path):
    os.makedirs(path)

# Frames number
frames = 40

# Grid dimensions
dimx = 50
dimy = 25

# Null matrix for dark background
img_null = np.zeros((dimy,dimx))

# Initial conditions
img = np.random.randint(2, size=(dimy,dimx))

# Init file names
files = []

for i in range(frames):
    plt.style.use('dark_background')
    plt.delaxes()
    fig = plt.figure()#figsize=(10,15), dpi=90)
    ax = fig.add_subplot(111)
    plt.axis('off')
    plt.subplots_adjust(left=-0.4, bottom=-0.2, right=1.4, top=1.2)
    plt.tight_layout()
    ax.imshow(img_null, cmap=plt.get_cmap('gray'), vmin=0, vmax=1, animated=True)
    img = Game(img)
    CreateNumbers(ax, img)
    fname = str(100 + i)
    plt.savefig(fname, bbox_inches='tight')
    files.append(fname)
    plt.close('all')
    print(i)
