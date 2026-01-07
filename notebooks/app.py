import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Análisis exploratorio de vehículos en EE. UU.")

# Leer el conjunto de datos
df = pd.read_csv(
    r"C:\Users\lilia\OneDrive\Desktop\Triple_Ten\Proyecto_Sprint_7\vehicles_us.csv"
)

# Mostrar las primeras filas (opcional pero útil)
st.write("Vista previa del conjunto de datos:")
st.write(df.head())

# Botón para construir el histograma
if st.button("Mostrar histograma del odómetro"):
    fig = px.histogram(
        df,
        x="odometer",
        title="Distribución del kilometraje de los vehículos"
    )
    st.plotly_chart(fig)

import os
import streamlit as st

st.write(os.getcwd())
st.write(os.listdir())
