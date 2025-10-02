import streamlit as st
import plotly.express as px

from backend import getData

st.title("Weather Forecast App")
st.markdown("Select the **Place** and **Number of Days** to see the corresponding Weather Forecast.")

place = (st.text_input("Enter the Place: ", help="Enter te place you want to see the Weather Forecast for"))
days = st.slider("Number of days: ", min_value=1, max_value=5, help="No. of Days you want to see te Weather Forecast for")

option = st.selectbox("Select Type of Data", ("Weather", "Temperature"))


if place != "":
    if days == 1:
        st.subheader(f"{option} for next 24 hours in {place.capitalize()}: ")
    else:
        st.subheader(f"{option} for the next {days * 24} hours in {place.capitalize()}: ")


    if option == "Weather":
        col1, col2, col3 = st.columns([2, 3, 2])

        for item in getData(place, days, option):
            col1.write(item['dt_txt'])
            col2.write("Temperature: " + str(item['main']['temp'] / 10)[:5] + " °C")
            col3.write(str(item['weather'][0]['description']).title())

        weather = {
            "Date & Time"
        }


    if option == "Temperature":
        x_axis = []
        y_axis = []

        for item in getData(place, days, option):
            x_axis.append(item['dt_txt'])
            y_axis.append(item['main']['temp'])

        figure = px.line(x=x_axis, y=y_axis, labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(figure)






