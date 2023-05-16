import streamlit as st
import numpy as np
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.subheader( "Gráficos de la curva" )
# Definir la función
def f(x, y):
    return x**2 + x + y**2

# Generar los valores de x y y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# Crear una malla de coordenadas para evaluar la función
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Crear la figura y el objeto de los ejes en 3D
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie de la montaña
ax.plot_surface(X, Y, Z, cmap='terrain')

# Graficar los puntos de explosión
points = [(7, 8), (-4, 1), (5, 10)]
x_points, y_points, z_points = [], [], []
for point in points:
    x_points.append(point[0])
    y_points.append(point[1])
    z_points.append(f(point[0], point[1]))
ax.scatter(x_points, y_points, z_points, s=100, c='red', marker='o')

# Etiquetas de los puntos de explosión
labels = ['P1', 'P2', 'P3']
for i, point in enumerate(points):
    ax.text(point[0] + 1, point[1] - 1, f(point[0], point[1]), labels[i], color='red')

# Configuraciones del gráfico
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Altura')
ax.set_title('Superficie de la montaña')

# Mostrar el gráfico
st.pyplot(fig)

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

    # Crear la superficie de la montaña
    surface = go.Surface(x=X, y=Y, z=Z, colorscale='aggrnyl')

    # Crear los puntos de explosión
    points = np.array([(7, 8, f(7, 8)), (-4, 1, f(-4, 1)), (5, 10, f(5, 10))])
    scatter_points = go.Scatter3d(x=points[:, 0], y=points[:, 1], z=points[:, 2], mode='markers',
                                  marker=dict(color='red', size=5))

    # Calcular y agregar los vectores gradiente
    gradient_vectors = np.array([(-15, -16), (7, -2), (-11, -20)])
    quiver = go.Cone(x=points[:, 0], y=points[:, 1], z=points[:, 2],
                     u=gradient_vectors[:, 0], v=gradient_vectors[:, 1], w=np.zeros_like(points[:, 2]),
                     sizemode="absolute", sizeref=2, showscale=True)

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
        subtitle='Es posible hacer zoom con la rueda del mouse'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)

# Aplicar el estilo amplio a la página de Streamlit
#st.set_page_config(layout="wide")

# Título de la aplicación
st.title('Gráfico interactivo de la montaña')

# Mostrar el gráfico llamando a la función plot_mountain
plot_mountain()

