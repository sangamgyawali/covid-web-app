import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot,plot

data_latest = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_state.csv")
data_latest_usc = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
df = pd.DataFrame(data_latest)
dfc = pd.DataFrame(data_latest_usc)
st.title("COVID 19 Analysis")
st.markdown("This app is a Graphical interpretetion and predicton")

by_country = df.groupby("Country_Region")
by_states = dfc.groupby("state")
by_counties = dfc.groupby("county")



chart_data = pd.DataFrame(data_latest[:], columns=['Deaths', 'Recovered', 'Active'])
st.line_chart(chart_data)

#first page (world map)

#US states
option = st.selectbox(
   'what states case details would you like to visualize?',
    ("Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona",
     "California", "Colorado", "Connecticut", "District ", "of Columbia",
     "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
     "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
     "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
     "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
     "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon",
     "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
     "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington",
     "Wisconsin", "West Virginia", "Wyoming"))
st.write('You selected:', option)
data_US = df[df['Country_Region']=='US']
selbox = dfc[dfc['state'] == option]
fig = px.bar(selbox, x= 'date', y='cases', hover_data =['date', 'cases'], height = 400)
st.write(fig)
#px.set_mapbox_access_token(open(".mapbox_token").read())
data_US = df[df['Country_Region']=='US']
st.write(data_US[:20])
data_US.dropna(subset =['Lat','Long_'], inplace = True)
midpoint = (np.average(data_US['Lat']), np.average(data_US['Long_']))
st.write(pdk.Deck(
    map_style= "mapbox://styles/mapbox/light-v9",
    initial_view_state= {
    "latitude": midpoint[0],
    "longitude":midpoint[1],
    "zoom": 5,
    "pitch": 50,
    },
    layers= [
    pdk.Layer(
    'HexagonLayer',
    data_US[['Last_Update','Lat','Long_']],
    get_position = ['latitude' ,'longitude'],
    radius= 100,
    extruded = True,
    pickable= True,
    elevation_scale =4,
    elevation_range=[0,1000],

    ),
    ]
))


side = st.sidebar.markdown("Predictions (coming soon)")

st.sidebar.markdown("Statistical Inference (coming soon)")

st.sidebar.markdown("Analysis by gender and race (coming soon)")





















