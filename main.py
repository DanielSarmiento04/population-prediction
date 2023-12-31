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
st.write('''
Gradient growth, often referred to as exponential growth, signifies a pattern where the rate of increase of a quantity is proportional to its current value. In simple terms, it's growth at a compounding or accelerating rate, where the larger the current value, the faster it grows over time.

Unlike linear growth, where the increase is constant and steady, gradient growth demonstrates an accelerating or decelerating rate of change. When plotted on a graph, this type of growth results in a curve that steepens or flattens out, showcasing rapid expansion over time.

Mathematically, gradient growth can be represented by an exponential function, often in the form of  $ y = a * b^x $,  where:
         
- y represents the final value or quantity,

- a is the initial value or quantity,

- b is the growth factor or rate,

- x is time or the number of periods.
         
''')

left_co, cent_co, last_co = st.columns(3)

with cent_co: 
    st.image(
        'https://ccp.ucr.ac.cr/cursos/demografia_03/Imagenes/quinta12.gif',
        caption='Interpolation linear',
    )


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
st.write('''
Logistic growth represents a type of growth pattern where a population or a quantity initially experiences exponential or rapid growth, but eventually reaches a point where growth slows down and stabilizes. This pattern is often described as an S-shaped curve.

In logistic growth, the population or quantity starts with a period of rapid increase when resources are abundant. However, as the population approaches a certain limit or carrying capacity - the maximum population size that the environment can sustain - the growth rate gradually slows down. Eventually, the population stabilizes near the carrying capacity, resulting in a relatively constant population size.
         



         
Mathematically, logistic growth is described using the logistic equation, which can be represented as:

$$ P(t) = \\frac {K}{1 + e^{-r * t}} $$
 
Where:

- P(t) represents the population (or quantity) at time.

- K is the carrying capacity or the maximum population size the environment can sustain.

- r is the growth rate of the population.

- e is the base of the natural logarithm.

- t is time.
         
''')


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