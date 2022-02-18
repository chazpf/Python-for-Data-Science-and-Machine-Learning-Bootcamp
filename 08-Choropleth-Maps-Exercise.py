# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples

# ## Plotly Imports

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)

# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

import pandas as pd

df = pd.read_csv('2014_World_Power_Consumption')

# ** Check the head of the DataFrame. **

df.head()

# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

data = dict(type = 'choropleth',
            locations = df['Country'],
            colorscale = 'Viridis',
            reversescale = True,
            locationmode = 'country names',
            z = df['Power Consumption KWH'],
            text = df['Country'],
            colorbar = {'title':'Power Consumption KWH'}
            )

layout = dict(title = '2014 Power Consumption',
             geo = dict(showframe=False,projection={'type':'mercator'})
             )

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

# ## USA Choropleth

# ** Import the 2012_Election_Data csv file using pandas. **

usdf = pd.read_csv('2012_Election_Data')

# ** Check the head of the DataFrame. **

usdf.head()

# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

data2 = dict(type = 'choropleth',
            locations = usdf['State Abv'],
            colorscale = 'Viridis',
            reversescale = True,
            locationmode = 'USA-states',
            z = usdf['Voting-Age Population (VAP)'],
            text = usdf['State'],
            colorbar = {'title':'Voting Age Population'}
            )

layout2 = dict(title = '2012 Election Data',
             geo = dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)')
             )

choromap = go.Figure(data = [data2],layout = layout2)
iplot(choromap,validate=False)
