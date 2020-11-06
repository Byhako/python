import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    # y = b1*x + b0
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    num = np.sum((x - m_x)*(y - m_y))
    den = np.sum((x - m_x)*x)  # x*(x - m_x) == (x - m_x)**2
    b1 = num/den
    b0 = m_y - b1*m_x
    return b0, b1

def linea(x, y):
    b0, b1 = estimate_b0_b1(x, y)
    len_x = max(x) - min(x)
    x1 = min(x) - len_x*0.1
    x2 = max(x) + len_x*0.1
    y1 = x1*b1 + b0
    y2 = x2*b1 + b0

    return [x1, x2], [y1, y2]

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7]
    y = [2,3,5,6,5,7,11]
    b0, b1 = estimate_b0_b1(x, y)
    X, Y = linea(x, y)
    print(f'b0 y b1 = {b0, b1}')

    plt.scatter(x, y, color='b', marker='o', s=30)
    plt.plot(X, Y, 'k--', label=f'y = {round(b1, 2)}*x + {round(b0, 2)}')
    plt.title('Regresión lineal', fontsize=16)
    # plt.legend(loc=0, fontsize=14)

    plt.annotate(
        f'y = {round(b1, 2)}*x + {round(b0, 2)}',
        xy=(min(x)*0.9, max(y)*0.9),
        xytext=(min(x)*0.9, max(y)*0.9),
        fontsize=14,
        color="#df1b08",
    )

    plt.show()
