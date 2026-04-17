import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Análisis exploratorio de vehículos en EE. UU.")

# Leer el conjunto de datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar las primeras filas (opcional pero útil)
st.write("Vista previa del conjunto de datos:")
st.write(df.head())

#Ajusta el histograma
if st.button("Mostrar histograma de precios"):
    fig_hist = px.histogram(
        df,
        x="price",
        nbins=50,
        labels={"price": "Precio (USD)"},
        title="Distribución de precios"
    )
    st.plotly_chart(fig_hist)
    
#Gráfico de dispersión
if st.button("Mostrar relación precio vs kilometraje"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        labels={
            "odometer": "Kilometraje",
            "price": "Precio (USD)"
        },
        title="Relación entre kilometraje y precio",
        opacity=0.5
    )
    st.plotly_chart(fig_scatter)

streamlit run app.py
