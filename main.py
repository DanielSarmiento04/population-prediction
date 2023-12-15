import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Declare the path csv path and sheet name
path = "API_SP.POP.TOTL_DS2_en_csv_v2_6224560.csv"



df = pd.read_csv(
    path,
    skiprows=4
)

st.write("""
# Prediction Populations

""")


st.dataframe(
    df,
    width=2000
)

country_available = df['Country Name']

option = st.selectbox(
    'Select a Country',
    country_available,
    index=248
)

# Get the specific country
country_selected = df.iloc[248, ]

# Get the country name
country_name = country_selected.iloc[0]

years_populations = country_selected \
                    .iloc[4: -1] \
                    # .astype(np.int128)

# Create a Plotly figure
fig = go.Figure()

# Add a trace for the line graph
fig.add_trace(
    go.Scatter(
        x = years_populations.index.to_list(),
        y =  years_populations.to_list(),
        mode='lines+markers',
        name='Data'
    )
)

# Update layout
fig.update_layout(
    title='Population of ' + country_name,
    xaxis_title='years',
    yaxis_title='Millions of people',
    # bargap=0.1  # Space between bars
)




st.plotly_chart(
    fig,
    use_container_width=True
)