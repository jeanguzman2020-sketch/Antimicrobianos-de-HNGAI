import streamlit as st
import pandas as pd

archivo = "Tabla_Preparacion_Antimicrobianos_HNGAI-VERSION MEJORADA.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Registro x Laboratorio y Lote"
)

st.title("Consulta Rápida de Antimicrobianos")
st.title("HNGAI")

# Antimicrobiano
antimicrobiano = st.selectbox(
    "Seleccione Antimicrobiano",
    sorted(df["Antimicrobiano"].dropna().unique())
)

df_filtrado = df[
    df["Antimicrobiano"] == antimicrobiano
]

# Laboratorio
laboratorio = st.selectbox(
    "Seleccione Laboratorio",
    sorted(df_filtrado["Laboratorio / Marca Fabricante"].dropna().unique())
)

resultado = df_filtrado[
    df_filtrado["Laboratorio / Marca Fabricante"] == laboratorio
]

if not resultado.empty:

    fila = resultado.iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Lote", str(fila["Lote"]))

        st.metric(
            "Registro Sanitario",
            str(fila["Registro Sanitario DIGEMID"])
        )

    with col2:
        fecha = pd.to_datetime(fila["Fecha Vencimiento"])

        st.metric(
            "Vencimiento",
            fecha.strftime("%d/%m/%Y")
        )

        st.metric(
            "Estado",
            str(fila["Estado del Lote"])
        )

    st.subheader("Estabilidad")

    st.write(
        "Reconstituido T° ambiente:",
        fila["Estabilidad Reconst (T° Amb)"]
    )

    st.write(
        "Diluido T° ambiente:",
        fila["Estabilidad Diluido (T° Amb)"]
    )

    st.write(
        "Diluido refrigerado:",
        fila["Estabilidad Diluido (Refrig 2-8°C)"]
    )

    st.subheader("Observaciones")

    st.info(
        str(fila["Observaciones de Ficha Técnica del Fabricante"])
    )
