import requests
import streamlit as st

API_key = st.secrets["API_key"]

def getData(place, days, type):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"

    response = requests.get(url)
    data = response.json()

    req_data = 8 * days
    
    return data['list'][:req_data]


    