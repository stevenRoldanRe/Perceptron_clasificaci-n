import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

# Función de activación (perceptrón)
def perceptron(x1, x2, w1, w2, bias):
    return 1 if (w1 * x1 + w2 * x2 + bias) > 0 else 0

# Función para graficar el hiperplano de decisión
def plot_decision_boundary(w1, w2, bias, ax):
    x_vals = np.linspace(-10, 10, 200)
    y_vals = (-w1 * x_vals - bias) / w2
    ax.plot(x_vals, y_vals, label='Hiperplano', color='blue')

# Interacción con el mouse
def onclick(event, points, ax):
    if event.button is MouseButton.LEFT:
        x1, x2 = event.xdata, event.ydata
        if x1 is not None and x2 is not None:
            points.append((x1, x2))
            ax.scatter(x1, x2, color='black')
            plt.draw()

# Función para clasificar y graficar resultados
def classify_and_plot(points, w1, w2, bias, ax):
    for x1, x2 in points:
        classification = perceptron(x1, x2, w1, w2, bias)
        color = 'red' if classification == 1 else 'green'
        ax.scatter(x1, x2, color=color)
    plot_decision_boundary(w1, w2, bias, ax)

def main():
    # Datos de entrada
    w1 = float(input("Ingrese el valor de w1: "))
    w2 = float(input("Ingrese el valor de w2: "))
    bias = float(input("Ingrese el valor de bias: "))

    points = []

    # Configuración de la figura y el gráfico
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('Clasificación con Perceptrón')

    # Registrar el evento de clic del mouse
    cid = fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, points, ax))

    plt.show()

    # Clasificar y graficar los puntos después de haber terminado de ingresar
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('Clasificación con Perceptrón')

    classify_and_plot(points, w1, w2, bias, ax)
    plt.show()

if __name__ == '__main__':
    main()
