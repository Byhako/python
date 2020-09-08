from bokeh.plotting import figure, output_file, show
import numpy as np

if __name__ == "__main__":
    output_file('grafica.html')
    fig = figure(plot_width=800, plot_height=300)

    values = int(input('Cuantos valores? '))
    x = np.arange(0, values, 0.1)
    y = np.sin(x) + (np.sin(3*x))/(3) + (np.sin(5*x))/(5)

    fig.line(x, y, line_width=2)
    show(fig)