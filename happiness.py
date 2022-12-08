import streamlit as st
import pandas as pd
from plotly import express as px

st.title("In Search for Happiness.")
x_axis = st.selectbox("Select the data for the X-axis.",
                      ("GDP",
                       "Happiness",
                       "Generosity"
                       )
                      )

y_axis = st.selectbox("Select the data for the Y-axis.",
                      ("GDP",
                       "Happiness",
                       "Generosity"
                       )
                      )

st.subheader(f"{x_axis} and {y_axis}")

# Used pandas to read csv file
df = pd.read_csv("happy.csv")
print(df.columns)


# For X axis.
match x_axis:
    case "GDP":
        x_plot = df['gdp']
    case "Happiness":
        x_plot = df['happiness']
    case "Generosity":
        x_plot = df['generosity']

# For Y axis.
match y_axis:
    case "GDP":
        y_plot = df['gdp']
    case "Happiness":
        y_plot = df['happiness']
    case "Generosity":
        y_plot = df['generosity']


# Draw the graph
graph = px.scatter(x=x_plot, y=y_plot, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(graph)
