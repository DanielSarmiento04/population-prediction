import streamlit as st
import pandas as pd

# Declare the path excel path and sheet name
path = "ProyeccionMunicipios2005_2020.xls"
sheetName = "Mpios"



df = pd.read_excel(
    path,
    sheet_name=sheetName,
    skiprows=8
)

st.write("""
# Prediction Populations

""")


st.dataframe(df)

