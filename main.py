import streamlit as st
from plotly import express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
name = st.text_input("City Name:")
days = st.slider("Forecast Days:",
                 min_value=1,
                 max_value=5,
                 help="Slide the pointer to point to a particular day/days")
data = st.selectbox("Select data to view:",
                    ("Temperature", "Sky")
                    )
st.subheader(f"{data} for the next {days} days in {name}.")

if name:
    try:
        filtered_data = get_data(name)[:8 * days]

        if data == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            graph = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(graph)
        elif data == "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[image] for image in sky_conditions]
            st.image(image_paths, width=120)
    except KeyError:
        st.info("Enter a valid city or place.")





