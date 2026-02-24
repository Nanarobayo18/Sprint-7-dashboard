import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sprint 7 Dashboard", layout="wide")

st.title("Sprint 7 — Panel de control")
st.write("Dashboard de ejemplo con datos simples (puedes cambiar el dataset luego).")

# Cargar dataset real
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    df.columns = [c.strip().lower() for c in df.columns]
    return df

data = load_data()

st.subheader("Vista previa de datos")
st.dataframe(data)

st.sidebar.header("Filtros")
modelos = st.sidebar.multiselect(
    "Modelo",
    sorted(data["model"].dropna().unique()),
    default=sorted(data["model"].dropna().unique())
)

data_filtrada = data[data["model"].isin(modelos)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de precios")
    fig = px.histogram(data_filtrada, x="price", nbins=10)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Precio por marca")
    fig2 = px.box(data_filtrada, x="model", y="price")
    st.plotly_chart(fig2, use_container_width=True)
