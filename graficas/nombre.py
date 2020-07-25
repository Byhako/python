import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style("darkgrid")

xl = [2, 2, 2.2, 2.5, 2.8, 6]
yl = [7, 1.6, 1.3, 1.1, 1, 1]

xa = [2, 3.6, 3.8, 4.2, 4.4, 6]
ya = [1, 6.8, 7, 7, 6.8, 1]
xah = [2.54, 5.4]
yah = [3, 3]

xu = [2, 2, 2.3, 2.9, 3.71, 4.28, 5.1, 5.7, 6, 6]
yu = [7, 1.8, 1.5, 1.2, 1, 1, 1.2, 1.5, 1.8, 7]

xr = [2, 2, 2.2, 2.5, 2.9, 5.1, 5.5, 5.8, 6, 6, 5.8, 5.5, 5.1, 2]
yr = [1, 6.3, 6.6, 6.9, 7, 7, 6.9, 6.6, 6.3, 4.7, 4.4, 4.1, 4, 4]
xr2 = [4.5, 6]
yr2 = [4, 1]

plt.figure(figsize=(12, 6), dpi=80)
lineWith = 10

plt.subplot(1,5,1)
plt.plot(xl, yl, linewidth=lineWith, color='#951387')
# plt.plot(xl, yl, 'b-o', linewidth=4.0)
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.grid(True)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior

plt.subplot(1,5,2)
plt.plot(xa, ya, linewidth=lineWith, color='#951387')
plt.plot(xah, yah, linewidth=lineWith, color='#951387')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.grid(True)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior

plt.subplot(1,5,3)
plt.plot(xu, yu, linewidth=lineWith, color='#951387')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.grid(True)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior

plt.subplot(1,5,4)
plt.plot(xr, yr, linewidth=lineWith, color='#951387')
plt.plot(xr2, yr2, linewidth=lineWith, color='#951387')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.grid(True)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior

plt.subplot(1,5,5)
plt.plot(xa, ya, linewidth=lineWith, color='#951387')
plt.plot(xah, yah, linewidth=lineWith, color='#951387')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.grid(True)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none') #borra eje derecho
ax.spines['top'].set_color('none')   #borra eje superior


plt.suptitle(r"$Nombre$",size=24)
plt.show()