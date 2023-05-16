import streamlit as st
import pandas as pd

st.title( "Calculo Avanzado" ) 
st.write( "Trabajo Práctico Nº 2 - Gradiente" )

st.write("Los ingenieros José y Pablo desean dinamitar la superficie de una montaña para crear derrumbes controlados de la tierra sobre la montaña. Para ello han creado un mapa por computadora tridimensional de la montaña, el cual obedece al siguiente modelo funcional:")

st.latex(r''' 
    𝑓(𝑥, 𝑦) = 𝑥^2+x+y^2
    ''')
# 𝑓(𝑥, 𝑦) = 𝑥
# 2 + 𝑥 + 𝑦
# 2
st.write("Los ingenieros han determinado tres puntos en los cuales desean dinamitar la montaña.Los puntos elegidos son 𝑃1 = (7,8), 𝑃2 = (−4,1), 𝑃3 = (5,10).El interés en esta fase del proyecto es poder predecir la dirección de máximo descenso de la montaña para estimar la dirección en la cual se derrumbará la montaña en cada punto de la explosión. Estos datos serán necesarios para poder simular por computadora los distintos puntos de explosión")

# if t is not None:
#     textsplit = t.splitlines()

#     for x in textsplit:
#         st.write(x)
st.write("Presente un informe en donde explique las conclusiones a las cuales llegan los ingenieros José y pablo completando la siguiente tabla.")
tabla = pd.DataFrame()
columna1 = ["Puntos en la montaña","Dirección de máximo descenso"]
columna2 = ["(7,8,...)","<---,--->"]
columna3 = ["(-4,1,...)","<---,--->"]
columna4 = ["(5,10,...)","<---,--->"]

tabla['Puntos en el plano'] = columna1
tabla['P1'] = columna2
tabla['P2'] = columna3
tabla['P3'] = columna4
st.table(tabla)



