import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sprint 7 - Dashboard de vehículos", layout="wide")
st.title("Sprint 7 — Panel de control")
st.write("Análisis exploratorio de vehículos usados (dataset vehicles_us.csv).")

@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    df.columns = [c.strip().lower() for c in df.columns]
    return df

data = load_data()

st.subheader("Vista previa de datos")
st.dataframe(data.head(20))

# Filtros
st.sidebar.header("Filtros")
modelos = st.sidebar.multiselect(
    "Modelo",
    sorted(data["model"].dropna().unique()),
    default=sorted(data["model"].dropna().unique())[:20]  # para no seleccionar miles por defecto
)
data_filtrada = data[data["model"].isin(modelos)] if modelos else data

st.header("Gráficos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de precios (Histograma)")
    if st.button("Construir histograma"):
        fig = px.histogram(data_filtrada, x="price", nbins=30)
        st.plotly_chart(fig, use_container_width=True, key="hist_price")

with col2:
    st.subheader("Relación entre precio y año (Dispersión)")
    if st.button("Construir dispersión"):
        fig2 = px.scatter(
            data_filtrada.dropna(subset=["model_year", "price"]),
            x="model_year",
            y="price",
            hover_data=["model", "condition"]
        )
        st.plotly_chart(fig2, use_container_width=True, key="scatter_year_price")
