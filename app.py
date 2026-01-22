import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sprint 7 Dashboard", layout="wide")

st.title("Sprint 7 — Panel de control")
st.write("Dashboard de ejemplo con datos simples (puedes cambiar el dataset luego).")

# Dataset de ejemplo
data = pd.DataFrame(
    {
        "marca": ["Ford", "Toyota", "Toyota", "BMW", "Ford", "BMW"],
        "precio": [12000, 15000, 18000, 35000, 14000, 42000],
        "anio": [2012, 2016, 2018, 2020, 2014, 2021],
    }
)

st.subheader("Vista previa de datos")
st.dataframe(data)

st.sidebar.header("Filtros")
marca = st.sidebar.multiselect("Marca", sorted(data["marca"].unique()), default=sorted(data["marca"].unique()))
data_filtrada = data[data["marca"].isin(marca)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de precios")
    fig = px.histogram(data_filtrada, x="precio", nbins=10)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Precio por marca")
    fig2 = px.box(data_filtrada, x="marca", y="precio")
    st.plotly_chart(fig2, use_container_width=True)