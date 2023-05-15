import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Definir la función
def f(x, y):
    return x**2 + x + y**2

# Generar los valores de x y y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# Crear una malla de coordenadas para evaluar la función
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Crear la superficie de la montaña
surface = go.Surface(x=X, y=Y, z=Z, colorscale='thermal')

# Crear los puntos de explosión
points = np.array([(7, 8), (-4, 1), (5, 10)])
x_points, y_points, z_points = points[:, 0], points[:, 1], f(points[:, 0], points[:, 1])
scatter_points = go.Scatter3d(x=x_points, y=y_points, z=z_points, mode='markers',
                              marker=dict(color='red', size=5),
                              text=["P1", "P2", "P3"])

# Calcular y agregar los vectores gradiente
gradient_vectors = np.array([(-15, -16), (7, -2), (-11, -20)])
quiver = go.Cone(x=x_points, y=y_points, z=z_points,
                 u=gradient_vectors[:, 0], v=gradient_vectors[:, 1], w=np.zeros_like(z_points),
                 sizemode="absolute", sizeref=3, showscale=False, colorscale='blues',
                 text=["Gradiente en P1", "Gradiente en P2", "Gradiente en P3"])

# Crear la figura y agregar los elementos
fig = go.Figure(data=[surface, scatter_points, quiver])

# Configurar el diseño del gráfico
fig.update_layout(
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='Altura',
        aspectratio=dict(x=1, y=1, z=0.5),
        camera=dict(eye=dict(x=-1.5, y=-1.5, z=0.8)),
    ),
    title='Superficie de la montaña con vectores gradiente',
)

# Mostrar el gráfico interactivo en Streamlit
st.plotly_chart(fig)

