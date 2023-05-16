import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.subheader( "Desarrollo :rocket:" )
st.write("El primer paso es encontrar el gradiente de la función de superficie dada, ya que el gradiente nos dará la dirección y magnitud de máximo crecimiento de la función en cada punto. El gradiente de una función de dos variables, como en este caso, se representa como un vector con dos componentes: la derivada parcial con respecto a 'x' y la derivada parcial con respecto a 'y'.")
st.write("Para encontrar el gradiente de la función")
st.latex(r''' 
    𝑓(𝑥, 𝑦) = 𝑥^2+x+y^2
    ''')
st.divider()
st.write("Calculamos las derivadas parciales de la función con respecto a ‘x’ y ‘y’ por separado.")
st.write("La derivada parcial con respecto a ‘x’ es:")
st.write("∂f/∂x = 2x + 1")
st.write("La derivada parcial con respecto a ‘y’ es:")
st.write("∂f/∂y = 2y")
st.divider()
st.write("Ahora que tenemos las derivadas parciales, podemos calcular el gradiente:")
st.latex(r'''
    ∇f(x, y) = (∂f/∂x, ∂f/∂y) = (2x + 1, 2y)
    ''')
st.write("El vector gradiente (∇f) representa la dirección y la magnitud de máximo crecimiento de la función ‘f(x, y)’ en cada punto.")

st.write("En el punto P1 = (7, 8):")
st.latex(r'''
    ∇f(7, 8) = (2(7) + 1, 2(8)) = (15, 16)
    ''')
st.write("En el punto P2 = (-4, 1):")
st.latex(r'''
     ∇f(-4, 1) = (2(-4) + 1, 2(1)) = (-7, 2)
    ''')
st.write("En el punto P3 = (5, 10):")
st.latex(r'''
    ∇f(5, 10) = (2(5) + 1, 2(10)) = (11, 20)
    ''')
st.divider()
st.write("Ahora, para determinar la dirección de máximo descenso en cada punto de explosión, debemos encontrar el vector negativo del gradiente (-∇f). Esto se debe a que el gradiente apunta en la dirección de máximo crecimiento, mientras que queremos determinar la dirección de máximo descenso.")
st.write("Entonces, la dirección de máximo descenso en el punto P1 es el vector (-15, -16), en el punto P2 es el vector (7, -2), y en el punto P3 es el vector (-11, -20). Estos vectores representan la dirección en la cual se derrumbará la montaña en cada punto de explosión")
#GRÁFICO 2D

def plot_mountain():
    # Definir la función
    def f(x, y):
        return x**2 + x + y**2

    # Generar los valores de x y y
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)

    # Crear una malla de coordenadas para evaluar la función
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Configurar el gráfico
    fig, ax = plt.subplots()
    levels = 20
    cmap = 'terrain'
    ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Superficie de la montaña')
    ax.grid(True)

    # Graficar los puntos de explosión
    points = [(7, 8), (-4, 1), (5, 10)]
    for point in points:
        ax.plot(point[0], point[1], 'ro')

    # Etiquetas de los puntos de explosión
    labels = ['P1', 'P2', 'P3']
    for i, point in enumerate(points):
        ax.text(point[0] + 0.5, point[1] - 0.5, labels[i], color='red')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Aplicar el estilo amplio a la página de Streamlit
#st.set_page_config(layout="wide")

# Título de la aplicación
st.title('Gráfico de la montaña, curvas de nivel')

# Mostrar el gráfico llamando a la función plot_mountain
plot_mountain()


