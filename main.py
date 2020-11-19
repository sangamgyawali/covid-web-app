import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot

st.sidebar.title("COVID-19 Kills!")
togg = st.sidebar.radio("Lets get some insights", ('Introduction to Covid-19', 'Cases in the United States',
                                                   'How red does the World look',
                                                   'Possible Future'))
if togg == 'Introduction to Covid-19':
    st.title("COVID 19: How it all began!")
    st.write("According to Center of Disease Control and Prevention, The novel (new) coronavirus that first appeared in"
             " China had never been seen before, so it quickly gained the attention of scientists around the world."
             "Epidemiologists did field investigations to find out how the new virus started. They conducted surveys in the community"
             " and in health facilities and collected nose and throat specimens for lab analyses. These investigations showed "
             "them who was infected, when they became sick, and where they had been just before they got sick."
             "Using this information, epidemiologists determined that the virus possibly came from an animal sold at "
             "a market. The new virus was found to be a coronavirus, and coronaviruses cause a severe acute respiratory syndrome."
             " This new coronavirus is similar to SARS-CoV, so it was named SARS-CoV-2 The disease caused by the virus was named "
             "COVID-19 (COronVIrusDisease-2019) to show that it was discovered in 2019. An outbreak is called an epidemic"
             " when there is a sudden increase in cases. As COVID-19 began spreading in Wuhan, China, it became an epidemic."
             " Because the disease then spread across several countries and affected a large number of people, it was classified as a pandemic.")

if togg == 'Cases in the United States':
    data_latest_usc = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
    dfc = pd.DataFrame(data_latest_usc)
    dfc['ndate'] = pd.to_datetime(dfc.date)
    monthlydata = dfc[['ndate', 'cases', 'deaths']].copy()
    monthlydata['date'] = pd.to_datetime(monthlydata.ndate)
    dfd = monthlydata.groupby([(monthlydata['date'])])[['cases', 'deaths']].sum()
    chart_data = pd.DataFrame(dfd[:], columns=['cases', 'deaths'])
    st.title("COVID 19 Analysis of cases and deaths in the United States of America")
    st.line_chart(chart_data)
    st.write("As we can see in the graph, the cases are growing exponentially. However, when we see the line for"
             " the number of deaths, we find that they’re very low. This is a tricky concept for a pandemic as people"
             " begin to think it is easily recovered. What we all should be aware of is that it is the life of almost 250,000 "
             "people that was lost. Even one is a lot. Our first goal should be not falling inside this graph at all as 11.5 million "
             "is already a huge number. So, taking necessary precautions is our only option until a fully functional vaccine with least "
             "side effects is manufactured, and verified as safe to use.")
    st.write(" ")
    st.write("Now lets see the data statewise, Choose a state to get respective data")
    option = st.selectbox(
        ' ',
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
    selbox = dfc[dfc['state'] == option]
    fig = px.bar(selbox, x='date', y='cases', hover_data=['date', 'cases'], height=400)
    st.write('You selected:', option)
    st.write(fig)
    st.write(" ")
    st.write("This is a sad, true and present story. This disease is still being dealt with recklessly in a lot "
             "of places in the US. As we evaluate the data from every state, the cases are just rapidly going up. "
             "It is late but not too late to still prevent and ultimately end this pandemic in the US. We can end it and we all know how!")


if togg == 'How red does the World look':
    data_latest = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_state.csv")
    df = pd.DataFrame(data_latest)
    df.dropna(subset=['Lat', 'Long_'], inplace=True)
    midpoint = (np.average(df['Lat']), np.average(df['Long_']))
    mapdata = df[['Deaths', 'Lat', 'Long_']].copy()
    mapdata.rename(columns={"Lat": "latitude", "Long_": "longitude"}, inplace = True)
    mapdata.dropna(subset=["latitude", "longitude"], inplace=True)
    st.map(mapdata)
    st.write(" ")
    st.write("We can see that the red dots are all over the world. "
             "The red dots denote the spread of the virus. Even the smallest of islands are infected, as I noticed "
             "the red dots in the middle of ocean. "
             "But this is not the only spread. So, try to zoom in and out to the spread all over the world. "
             "The visualization is lacking for the places whose latitudes"
             " and longitudes were missing in the dataset. So, this is not just the problem of the United "
             "States but it has become a global problem. It is about time the novel coronavirus is taken seriously.")

if togg == 'Possible Future':
    st.title("A Linear Regression model with 96.4% accuracy...")
    st.write("...does not determine our future.")
    st.title("We do!...")
    st.write("...so lets!")