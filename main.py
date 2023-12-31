import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from methods import (
    Linear,
    Gradient,
    Logistic
)

from drawer.drawer import Drawer

# Declare the path csv path and sheet name
path = "API_SP.POP.TOTL_DS2_en_csv_v2_6224560.csv"



df = pd.read_csv(
    path,
    skiprows=4
)

st.title('Population Prediction')


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

index = country_available[country_available == option].index[0]

# Get the specific country
country_selected = df.iloc[index, ]

# Get the country name
country_name = country_selected.iloc[0]

years_populations = country_selected \
                    .iloc[4: -1] \
                    # .astype(np.int128)

# Create a Plotly figure
fig = Drawer.draw_data(
    x=years_populations.index,
    y=years_populations,
    country=country_name
)



st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader('Alhorithms')

data_predicted = np.arange(2020, 2050, dtype=int)

# linear interpolation

st.subheader('Linear interpolation')
st.write('''
Linear growth refers to a steady and consistent increase or progression over time where the change occurs at a constant rate. In this type of growth, the relationship between the input and output variables remains proportional.

In a linear growth scenario, if you were to graph the relationship between time (or any independent variable) on the x-axis and the quantity or value (dependent variable) on the y-axis, the resulting graph would be a straight line. This line would have a constant slope, indicating that for every unit increase in the independent variable, there is a constant increase or decrease in the dependent variable.

Mathematically, linear growth can be represented by an equation in the form of 

$$ y = m x + b $$


- y is the dependent variable,
- x is the independent variable,
- m is the slope of the line (representing the rate of change),
- b is the y-intercept (the value of  y when  x x is zero).
''')

left_co, cent_co, last_co = st.columns(3)

with cent_co: 
    st.image(
        'https://ccp.ucr.ac.cr/cursos/demografia_03/Imagenes/quinta4.gif',
        caption='Interpolation linear',
    )


df_linear = Linear.calcule(
    populations=years_populations.to_numpy().astype(int),
    years=years_populations.index.to_numpy().astype(int),
    data_predicted=data_predicted
)

fig_linear = Drawer.draw_data(
    x=data_predicted,
    y=df_linear,
    country=country_name
)


st.plotly_chart(
    fig_linear,
    use_container_width=True
)


# Geometric gradient (exponential method)
st.subheader('Geometric gradient (exponential method)')


df_gradient = Gradient.calcule(
    populations=years_populations.to_numpy().astype(int),
    years=years_populations.index.to_numpy().astype(int),
    data_predicted=data_predicted
)

fig_gradient = Drawer.draw_data(
    x=data_predicted,
    y=df_gradient,
    country=country_name
)

st.plotly_chart(
    fig_gradient,
    use_container_width=True
)



# Geometric gradient (exponential method)
st.subheader('Logistic method')


df_logistic = Logistic.calcule(
    populations=years_populations.to_numpy().astype(int),
    years=years_populations.index.to_numpy().astype(int),
    data_predicted=data_predicted
)

fig_logistic = Drawer.draw_data(
    x=data_predicted,
    y=df_logistic,
    country=country_name
)

st.plotly_chart(
    fig_logistic,
    use_container_width=True
)