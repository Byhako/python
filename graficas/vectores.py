import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=80)
ax = plt.axes()
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')

# Nuevos ejes
ax.arrow(0, 0, 80, 0, head_width=1, head_length=2, fc='k', ec='k')
ax.arrow(0, 0, 0, 50, head_width=1, head_length=2, fc='k', ec='k')

# Vectores originales
ax.arrow(0, 0, 13.8, 18.5, head_width=1, head_length=2, fc='g', ec='g')
ax.arrow(0, 0, 58, 19.5, head_width=1, head_length=2, fc='g', ec='g')

# Vectores Proyección
ax.arrow(15, 20, 60, 20, head_width=0, head_length=0, fc='g', ec='g', linestyle=":")
ax.arrow(60, 20, 15, 20, head_width=0, head_length=0, fc='g', ec='g', linestyle=":")

# vetor suma
ax.arrow(0, 0, 73.2, 39, head_width=1, head_length=2, fc='b', ec='b')
# vetor resta
ax.arrow(15, 20, 43, 0, head_width=1, head_length=2, fc='r', ec='r')
ax.arrow(0, 0, 45, 0, head_width=1, head_length=2, fc='r', ec='r', linestyle="--", linewidth=1.5)

# Equiquetas
ax.text(77, 2, 'X', fontsize=16)
ax.text(2, 50, 'Y', fontsize=16)
ax.text(14, 16, 'Xi = (15, 20)', fontsize=12)
ax.text(54, 16, 'Xf = (60, 20)', fontsize=12)
ax.text(37, 25, 'Xi + Xf', fontsize=12, rotation=35)
ax.text(50, 21, 'Xf - Xi', color='red', fontsize=12)
ax.text(36, 2, 'Xf - Xi', color='red', fontsize=12)



plt.xlim(-1, 90)
plt.ylim(-1, 55)
plt.show()