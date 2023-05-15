import streamlit as st
import pandas as pd

st.write("P1 = (7, 8): Para encontrar la coordenada z correspondiente a P1, simplemente evaluamos la función f(x, y) en las coordenadas x = 7 y y = 8:")
st.latex(r'''
    f(7, 8) = 7^2 + 7 + 8^2 = 49 + 7 + 64 = 120
    ''')
st.write("P2 = (-4, 1): Evaluamos la función f(x, y) en las coordenadas x = -4 y y = 1:")
st.latex(r'''
     f(-4, 1) = (-4)^2 + (-4) + 1^2 = 16 - 4 + 1 = 13
    ''')
st.write("P3 = (5, 10): Evaluamos la función f(x, y) en las coordenadas x = 5 y y = 10:")
st.latex(r'''
    f(5, 10) = 5^2 + 5 + 10^2 = 25 + 5 + 100 = 130
    ''')

tabla = pd.DataFrame()
columna1 = ["Puntos en la montaña","Dirección de máximo descenso"]
columna2 = ["(7,8,120)","<-15,16>"]
columna3 = ["(-4,1,13)","<7,2>"]
columna4 = ["(5,10,130)","<11,20>"]

tabla['Puntos en el plano'] = columna1
tabla['P1'] = columna2
tabla['P2'] = columna3
tabla['P3'] = columna4
st.table(tabla)