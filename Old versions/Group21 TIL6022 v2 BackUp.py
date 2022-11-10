#!/usr/bin/env python
# coding: utf-8

# # Research Question:
# **How did Covid-19 affect the passenger air traffic in the Netherlands?**
# 
# *Time scope:*
# January 2019 - August 2022
# (Covid-19 begin datum, toen nog geen meetgegevens, dus nemen data vanaf xx-xx-xxxx)
# 2019 is our base case scenario, the impact of Covid on the number of passenger is measured by comparing a given month in the pandemic with the corresponding month in the base case scenario.
# 
# *Spatial scope:* 
# All passengers related to the following airports fall inside the scope: Amsterdam Airport Schiphol, Rotterdam The Hague Airport, Eindhoven Airport, Maastricht Aachen Airport and Groningen Airport Eelde. It has been decided to consider the number of passenger instead of flights. The reasoning behind this is that the number of flights might not be representative as airlines operated empty flights in order to keep their airport slot during Covid-19 (https://nos.nl/artikel/2412154-die-duizenden-lege-vluchten-zijn-volgens-luchthavenkoepel-helemaal-niet-nodig). 
# 
# *Definitions:*
# As stated in the reasearch question, only passenger air traffic is considered; cargo and mail air traffic fall outside the scope of this research. Moreover, our hypothesis is that mail and cargo air traffic have been less affected by Covid-19. Passenger air traffic is measured in number of passenger (not in number of flights). 
# 
# 
# # Subquestions: 
# **Subquestion 1**
# 
# How has the number of air traffic passengers developed in the considered time and spatial scope?
# 
# *Hypothesis:* It is expected that the number of passengers is dependent on the governmental regulations in place. In times of strict regulations, it is expected that the number of air passengers is low. When Covid-19 measurements where low, it is expected that the number of passengers is broadly comparable to the number of passengers before Covid-19.  
# 
# 
# **Subquestion 2**
# 
# How has the number of new Covid-19 cases developed in the considered time in the Netherlands?
# 
# *Hypothesis:* It is expected that the number of Covid infections is dependent on seasonality and the regualtions in place. 
# 
# 
# **Subquestion 3**
# 
# Are there relative differences in the development of air traffic passengers between the considered airports in the Netherlands?
# 
# *Hypothesis:* Groningen airport is mainly focused on pleasure flights (BRON), therefore it is expected that the number of passengers has been less affected compared to other airports. 
# 
# 
# **Subquestion 4**
# 
# How has COVID-19 impacted air traffic from and to various regions / continents?
# 
# *Hypothesis:* It is expected that number of air passengers on intercontinental flights has been more affected than EUROPEAN FLIGHTS?

# # Project Group - 
# 
# Members: Eva Lijnen, Chaja Swab, Willemijn Dietz, Veerle van Citters, Noa Zijlmans
# 
# Student numbers: 4570812, 4661753, 5868130, 5871026, 4957024 

# # Research Objective
# 
# *Requires data modeling and quantitative research in Transport, Infrastructure & Logistics*

# # Discussion:
# 
# - Covid cases: niet bekend / betrouwbaar in begin van pandemie (definieer tijdsperiode). 
# - Seasonality: take into accoutn
# - 'Yearly' growth of air traffic not incorporated between 2019-2022
# - External factors outside the scope: high costs / inflation / recession, fear of Covid, personnel shortages
# - July misschien niet representative 

# # Contribution Statement
# 
# *Be specific. Some of the tasks can be coding (expect everyone to do this), background research, conceptualisation, visualisation, data analysis, data modelling*

# **Author 1**:
# 
# **Author 2**:
# 
# **Author 3**:

# # Data Used

# 

# # Data Pipeline

# 

# In[51]:


## Here al the necessairy libary's are imported 

get_ipython().run_line_magic('matplotlib', 'notebook')


from urllib.request import urlopen
from plotly.offline import init_notebook_mode
import plotly.express as px
import plotly.graph_objects as go
import json
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.io as pio
import geopandas as gpd
from plotly.graph_objs import *

##The first datafile is loaded in here 

filepath = '/Users/chaja/Project-TIL6022-Group-21/Monthly_figures_on_aviation_10102022_111323.csv'

airtraffic_df = pd.read_csv(filepath, sep=";")


# # Subquestion 1

# In[52]:


#DATA CLEANING: 

#SELECT CORRECT TIMESPAN

#Convert Periods column to datetime
#This one needs to be uncommenten en then again ###
airtraffic_df['Periods'] = airtraffic_df['Periods'].str.replace('*', '')
airtraffic_df['Periods'] = pd.to_datetime(airtraffic_df['Periods'], format = '%Y %B', errors = 'coerce') 

#airtraffic_df['Periods'].info()
airtraffic_df['Periods']

#Select rows that fall within our timespan
at_df_timespan = airtraffic_df[airtraffic_df['Periods'] >= '2018-01-01']

#Check for NaN values
#There are no NaN values 
#at_df_timespan.isnull().sum().sum()

at_df_timespan


# In[53]:



# Always at the first day of the month the data is collacted therefor we use those points.

get_ipython().run_line_magic('matplotlib', 'inline')
#Show basic figure via plotly for the amount of air traffic passengers over time
fig = px.line(at_df_timespan, x="Periods", y='Commercial air traffic/Passengers/Total passengers/Total passengers (number)',
              color='Airports', title='Amount of air traffic passengers')


#Lines are added to highlight to show when there where normaly peaks for the amount of air traffic passangers
fig.add_vline(x='2018-07-01', line_dash = 'dash', line_width = 0.5, line_color = 'green')
fig.add_annotation(x='2018-07-01', y=0.93, yref='paper', text='01 July 2018: Annual summer peek', font_size=8, ax=90, ay=-50)

fig.add_vline(x='2019-07-01', line_dash = 'dash', line_width = 0.5, line_color = 'green')
fig.add_annotation(x='2019-07-01', y=0.93, yref='paper', text='01 July 2019: Annual summer peek', font_size=8, ax=50, ay=-35)

#A line is added to highlight when covid started
fig.add_vline(x='2020-03-01', line_dash = 'dash', line_width = 0.5, line_color = 'red')
fig.add_annotation(x='2020-03-01', y=0.32, yref='paper', text='01 March 2020: COVID in the world', font_size=8, ax=70, ay=-70)
#hier ff bronnetje bijgooien

#Here we added a line when the first lockdown in the Netherlands/ Europe started 
fig.add_vline(x='2020-04-01', line_dash = 'dash', line_width = 0.5, line_color = 'red')
fig.add_annotation(x='2020-04-01', y=0.06, yref='paper', text='01 April 2020: Lockdown in NL + Europe', font_size=8, ax=0, ay=12)

fig.show()


# # Subquestion 2:
# 
# Filtered and prepared the data. Use of new_cases_smoothed --> justification based on source.
# Only Covid-19 measurements that have a direct impact on travelling, have been considered in this subquestion.

# In[54]:


# Import world Covid Data

filepath2 = '/Users/chaja/Project-TIL6022-Group-21/owid-covid-data.csv'



covid_world_df = pd.read_csv(filepath2, sep=",")
covid_world_df['date'] = pd.to_datetime(covid_world_df['date'], format='%Y-%m-%d %H:%M:%S')
covid_world_df

# Preparing the full data set for furhter use
# Filtering on Covid new cases for the Netherlands

covid_nl_total_df = covid_world_df[
    covid_world_df['location'] == 'Netherlands'
]

# Full data set:
# covid_nl_total_df

# Filtering for relevant columns and dropping NAN cells
covid_nl_df = covid_nl_total_df.iloc[:, [2,3,6]]
covid_nl_clean_df = covid_nl_df.dropna()
covid_nl_clean_df


# In[21]:


fig = px.line(covid_nl_clean_df, x="date", y="new_cases_smoothed", animation_group="new_cases_smoothed", hover_name="new_cases_smoothed", range_y=[0,130000], title = "Covid New Cases in the Netherlands")
fig.add_vline(x= "2020-03-15", line_dash = 'dash', line_width = 0.5, line_color = 'red', name='Lockdown')
fig.add_annotation(x="2020-03-15", y=1, yref="paper", text="15 March 2020: Lockdown")

fig.add_vline(x= "2020-06-01", line_dash = 'dash', line_width = 0.5, line_color = 'green', name='Easening of measures')
fig.add_annotation(x="2020-06-01", y=0.7, yref="paper", text="1 June 2020: Easening of measures")

fig.add_vline(x= "2020-10-14", line_dash = 'dash', line_width = 0.5, line_color = 'orange', name='Partial lockdown')
fig.add_annotation(x="2020-10-14", y=0.87, yref="paper", text="10 Oct 2020: Partial lockdown")

fig.add_vline(x= "2020-12-14", line_dash = 'dash', line_width = 0.5, line_color = 'red')
fig.add_annotation(x="2020-12-14", y=1, yref="paper", text="14 Dec 2020: Lockdown")

fig.add_vline(x= "2021-02-08", line_color = 'green', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2021-02-08", y=0.7, yref="paper", text="8 Feb 2020: Easening of measures")

fig.add_vline(x= "2021-12-19", line_color = 'red', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2021-12-19", y=1, yref="paper", text="19 Dec 2021: Lockdown")

fig.add_vline(x= "2022-01-10", line_color = 'green', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2022-01-10", y=0.7, yref="paper", text="10 Jan 2022: Easening of measures")

fig.update_layout(xaxis_title= 'Date', yaxis_title = 'New Cases Smoothed')
fig.layout.plot_bgcolor='#f0f5f5'
fig.show()


# In[22]:


N = 944
s = np.linspace(-1, 1, N)
xx = s + s ** 2
yy = s - s ** 2

fig = go.Figure(
    data=[go.Scatter(x=covid_nl_clean_df['date'], y=covid_nl_clean_df['new_cases_smoothed'],
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=covid_nl_clean_df['date'], y=covid_nl_clean_df['new_cases_smoothed'],
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[np.min(covid_nl_clean_df['date']),np.max(covid_nl_clean_df['date']) ], autorange=False, zeroline=False),
        yaxis=dict(range=[np.min(covid_nl_clean_df['new_cases_smoothed']),np.max(covid_nl_clean_df['new_cases_smoothed']) ], autorange=False, zeroline=False),
        title_text="Covid Cases", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[covid_nl_clean_df.iloc[k,1]],
            y=[covid_nl_clean_df.iloc[k,2]],
            mode="markers",
            marker=dict(color="red", size=15))])

        for k in range(N)]
)

# fig.show()

fig.add_vline(x= "2020-03-15", line_dash = 'dash', line_width = 0.5, line_color = 'red', name='Lockdown')
fig.add_annotation(x="2020-03-15", y=1, yref="paper", text="15 March 2020: Lockdown")

fig.add_vline(x= "2020-06-01", line_dash = 'dash', line_width = 0.5, line_color = 'green', name='Easening of measures')
fig.add_annotation(x="2020-06-01", y=0.7, yref="paper", text="1 June 2020: Easening of measures")

fig.add_vline(x= "2020-10-14", line_dash = 'dash', line_width = 0.5, line_color = 'orange', name='Partial lockdown')
fig.add_annotation(x="2020-10-14", y=0.87, yref="paper", text="10 Oct 2020: Partial lockdown")

fig.add_vline(x= "2020-12-14", line_dash = 'dash', line_width = 0.5, line_color = 'red')
fig.add_annotation(x="2020-12-14", y=1, yref="paper", text="14 Dec 2020: Lockdown")

fig.add_vline(x= "2021-02-08", line_color = 'green', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2021-02-08", y=0.7, yref="paper", text="8 Feb 2021: Easening of measures")

fig.add_vline(x= "2021-12-19", line_color = 'red', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2021-12-19", y=1, yref="paper", text="19 Dec 2021: Lockdown")

fig.add_vline(x= "2022-01-10", line_color = 'green', line_width = 0.5, line_dash ='dash')
fig.add_annotation(x="2022-01-10", y=0.7, yref="paper", text="10 Jan 2022: Easening of measures")

fig.update_layout(xaxis_title= 'Date', yaxis_title = 'New Cases Smoothed')
fig.layout.plot_bgcolor='#f0f5f5'
fig.show()


# In[55]:


import plotly.express as px
import plotly.graph_objects as go

#The figure is scaled for the max and the min value of the new cases smoothed. New cases smoothed is used so the cases are on the rightfull days instead of the information processing delay
df = px.data.stocks()
dmax = covid_nl_clean_df['new_cases_smoothed'].values.max()
dmin = covid_nl_clean_df['new_cases_smoothed'].values.min()
fig = go.Figure()

#The different lines are added for the different moments the measerments were strengthend or eased.
#Added to the lines is when hoovering over them, the dateand how many new cases there were that day. 
#The measurment color shows if it is an easing or a strengthing measerment is. 
fig.add_trace(go.Scatter(x=covid_nl_clean_df.date, y=covid_nl_clean_df['new_cases_smoothed'], mode='lines', name='New Covid Cases NL', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}'+'<br>New Cases: %{y: "%m/%d/%Y}'))
fig.add_trace(go.Scatter(x=['2020-03-15','2020-03-15'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='red', width=2, dash='dash'),
                         legendgroup = 'Lockdown', name='Lockdown', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}'))
fig.add_trace(go.Scatter(x=['2020-12-14','2020-12-14'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='red', width=2, dash='dash'),
                         legendgroup='Lockdown', name='Lockdown', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}', showlegend=False))
fig.add_trace(go.Scatter(x=['2021-12-19','2021-12-19'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='red', width=2, dash='dash'),
                         legendgroup='Lockdown', name='Lockdown', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}',showlegend=False))

fig.add_trace(go.Scatter(x=['2020-10-10','2020-10-10'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='orange', width=2, dash='dash'),
                         legendgroup='Partial Lockdown', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}',name='Partial Lockdown'))                         

fig.add_trace(go.Scatter(x=['2020-06-01','2020-06-01'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='green', width=2, dash='dash'),
                         legendgroup='Easening of Measures', hovertemplate =
                        'Date: %{x: "%m/%d/%Y}',name='Easening of Measures'))
fig.add_trace(go.Scatter(x=['2021-02-08','2021-02-08'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='green', width=2, dash='dash'),
                         legendgroup='Easening of Measures', name='Easening of Measures',hovertemplate =
                        'Date: %{x: "%m/%d/%Y}', showlegend=False))
fig.add_trace(go.Scatter(x=['2022-01-10','2022-01-10'], 
                         y=[dmin,dmax], 
                         mode='lines', 
                         line=dict(color='green', width=2, dash='dash'),
                         legendgroup='Easening of Measures', name='Easening of Measures', 
                         hovertemplate ='Date: %{x: "%m/%d/%Y}',showlegend=False))                
# fig.update_traces(mode="lines", hovertemplate=None)
# fig.update_layout(hovermode="x")

# The figure is updated with titles and a legend is added
fig.update_layout(title='New Covid Cases in the Netherlands', xaxis_title= 'Date', yaxis_title = 'New Cases Smoothed')                                                 
fig.update_layout(legend=dict(groupclick="toggleitem"))
fig.layout.plot_bgcolor='#f0f5f5'
# fig.update_layout(hovermode="x unified")
fig.show()


# #Subquestion 3
# 

# In[56]:


#What unique values are in Airports column
at_df_timespan['Airports'].unique()

#Create 6 dataframes to work with
#Extract column: Commercial air traffic/Passengers/Total passengers/Total passengers (number)
at_df_total = at_df_timespan[at_df_timespan['Airports'] == 'Total Dutch airports']
at_df_total = at_df_total[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]

at_df_schiphol = at_df_timespan[at_df_timespan['Airports'] == 'Amsterdam Airport Schiphol']
at_df_schiphol = at_df_schiphol[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]

at_df_rotterdam = at_df_timespan[at_df_timespan['Airports'] == 'Rotterdam The Hague Airport']
at_df_rotterdam = at_df_rotterdam[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]

at_df_eindhoven = at_df_timespan[at_df_timespan['Airports'] == 'Eindhoven Airport']
at_df_eindhoven = at_df_eindhoven[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]

at_df_maastricht = at_df_timespan[at_df_timespan['Airports'] == 'Maastricht Aachen Airport']
at_df_maastricht = at_df_maastricht[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]

at_df_groningen = at_df_timespan[at_df_timespan['Airports'] == 'Groningen Airport Eelde']
at_df_groningen = at_df_groningen[['Commercial air traffic/Passengers/Total passengers/Total passengers (number)', 'Periods', 'Airports']]


#Rename all passenger columns to shorter name 
at_df_total = at_df_total.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})
at_df_schiphol = at_df_schiphol.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})
at_df_rotterdam = at_df_rotterdam.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})
at_df_eindhoven = at_df_eindhoven.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})
at_df_maastricht = at_df_maastricht.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})
at_df_groningen = at_df_groningen.rename(columns={'Commercial air traffic/Passengers/Total passengers/Total passengers (number)': 'Number of Passengers'})


#CREATE BASE YEAR COLUMN 

#Create list of 2018 number of passengers
total_base_year_2018 = at_df_total['Number of Passengers'].to_list()
total_base_year_2018 = total_base_year_2018[0:12]
total_base_year = []

schiphol_base_year_2018 = at_df_schiphol['Number of Passengers'].to_list()
schiphol_base_year_2018 = schiphol_base_year_2018[0:12]
schiphol_base_year = []

rotterdam_base_year_2018 = at_df_rotterdam['Number of Passengers'].to_list()
rotterdam_base_year_2018 = rotterdam_base_year_2018[0:12]
rotterdam_base_year = []

eindhoven_base_year_2018 = at_df_eindhoven['Number of Passengers'].to_list()
eindhoven_base_year_2018 = eindhoven_base_year_2018[0:12]
eindhoven_base_year = []

maastricht_base_year_2018 = at_df_maastricht['Number of Passengers'].to_list()
maastricht_base_year_2018 = maastricht_base_year_2018[0:12]
maastricht_base_year = []

groningen_base_year_2018 = at_df_groningen['Number of Passengers'].to_list()
groningen_base_year_2018 = groningen_base_year_2018[0:12]
groningen_base_year = []

#Create 5 times base year list
total_base_year = total_base_year_2018 * 5
schiphol_base_year = schiphol_base_year_2018 * 5
rotterdam_base_year = rotterdam_base_year_2018 * 5 
eindhoven_base_year = eindhoven_base_year_2018 * 5
maastricht_base_year = maastricht_base_year_2018 * 5
groningen_base_year = groningen_base_year_2018 * 5

#Strip elements from base year
#Base year needs to have the same length as dataframe column 
total_base_year = total_base_year[: len(at_df_total.index)]
schiphol_base_year = schiphol_base_year[: len(at_df_schiphol.index)]
rotterdam_base_year = rotterdam_base_year[: len(at_df_rotterdam.index)]
eindhoven_base_year = eindhoven_base_year[: len(at_df_eindhoven.index)]
maastricht_base_year = maastricht_base_year[: len(at_df_maastricht.index)]
groningen_base_year = groningen_base_year[: len(at_df_groningen.index)]


#Create column in dataframe with this base year
at_df_total['Previous number passengers (2018)'] = total_base_year
at_df_schiphol['Previous number passengers (2018)'] = schiphol_base_year
at_df_rotterdam['Previous number passengers (2018)'] = rotterdam_base_year
at_df_eindhoven['Previous number passengers (2018)'] = eindhoven_base_year
at_df_maastricht['Previous number passengers (2018)'] = maastricht_base_year
at_df_groningen['Previous number passengers (2018)'] = groningen_base_year

#Create percentage column 
at_df_total['Percentage incline/decline'] = ((at_df_total['Number of Passengers'] - at_df_total['Previous number passengers (2018)'])/at_df_total['Previous number passengers (2018)'])*100
at_df_schiphol['Percentage incline/decline'] = ((at_df_schiphol['Number of Passengers'] - at_df_schiphol['Previous number passengers (2018)'])/at_df_schiphol['Previous number passengers (2018)'])*100
at_df_rotterdam['Percentage incline/decline'] = ((at_df_rotterdam['Number of Passengers'] - at_df_rotterdam['Previous number passengers (2018)'])/at_df_rotterdam['Previous number passengers (2018)'])*100
at_df_eindhoven['Percentage incline/decline'] = ((at_df_eindhoven['Number of Passengers'] - at_df_eindhoven['Previous number passengers (2018)'])/at_df_eindhoven['Previous number passengers (2018)'])*100
at_df_maastricht['Percentage incline/decline'] = ((at_df_maastricht['Number of Passengers'] - at_df_maastricht['Previous number passengers (2018)'])/at_df_maastricht['Previous number passengers (2018)'])*100
at_df_groningen['Percentage incline/decline'] = ((at_df_groningen['Number of Passengers'] - at_df_groningen['Previous number passengers (2018)'])/at_df_groningen['Previous number passengers (2018)'])*100

#Set index to periods to make plotting easier
at_df_total = at_df_total.set_index('Periods')
at_df_schiphol = at_df_schiphol.set_index('Periods')
at_df_rotterdam = at_df_rotterdam.set_index('Periods')
at_df_eindhoven = at_df_eindhoven.set_index('Periods')
at_df_maastricht = at_df_maastricht.set_index('Periods')
at_df_groningen = at_df_groningen.set_index('Periods')

#at_df_eindhoven.head(56)
at_df_rotterdam.head(48)


#Concat all 6 dataframes into 1 dataframe
at_df_complete = pd.concat([at_df_total, at_df_schiphol, at_df_rotterdam, at_df_eindhoven, at_df_maastricht, at_df_groningen])
at_df_complete.head(36)


# In[ ]:





# In[57]:



#Figure is added with the relative incline/ decline of the airport
fig = px.line(at_df_complete, y='Percentage incline/decline',
              color='Airports', title='Amount of air traffic passengers', width=1500, height=1200)



fig.show()


# In[58]:


#CREATE CORRECT DATAFRAME

#Extract only the total dutch airports
#Extract the coloms needed. These are period and the number of passengers split over the different continents 
q4_at_total = at_df_timespan[at_df_timespan['Airports'] == 'Total Dutch airports']
q4_at_total = q4_at_total[['Periods', 
'Commercial air traffic/Passengers/Country of origin/destination/Europe/Europe total (number)', 
#'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/America (number)',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/North America (number)',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/Central America (number)',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/South America (number)', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Asia/Asia (number)', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Oceania (number)', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Africa/Africa (number)']]

# rename the colomns to names that are not so long 
q4_at_total = q4_at_total.rename(columns={'Commercial air traffic/Passengers/Country of origin/destination/Europe/Europe total (number)': 'Europe', 
#'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/America (number)': 'America', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/North America (number)' : 'North America',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/Central America (number)' : 'Central America',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/America/South America (number)' : 'South America',
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Asia/Asia (number)': 'Asia', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Oceania (number)': 'Oceania', 
'Commercial air traffic/Passengers/Country of origin/destination/Intercontinental/Africa/Africa (number)' : 'Africa'  })

# The continent north america is divided in the dataset in north and central. Here it is combinnend to north america 
q4_at_total['NorthCentralAmerica'] = q4_at_total['North America'] + q4_at_total['Central America']
del q4_at_total['North America']
del q4_at_total['Central America']

#q4_at_total.head(50)


# In[59]:


#CREATE PER CONTINENT BASE YEAR COLUMN 

#Base year columns are needed to see the relative change in the different airports over the time 

#EUROPE
base_year_europe_2018 = q4_at_total['Europe'].to_list()
base_year_europe_2018 = base_year_europe_2018[0:12]
base_year_europe = []

base_year_europe = base_year_europe_2018 * 5
base_year_europe = base_year_europe[: len(q4_at_total.index)]
q4_at_total['Base year Europe (2018)'] = base_year_europe
q4_at_total['Percentage Europe'] = (q4_at_total['Europe'] - q4_at_total['Base year Europe (2018)'])/q4_at_total['Base year Europe (2018)'] * 100

#NORTHCENTRALAMERICA
base_year_ncamerica_2018 = q4_at_total['NorthCentralAmerica'].to_list()
base_year_ncamerica_2018 = base_year_ncamerica_2018[0:12]
base_year_ncamerica = []

base_year_ncamerica = base_year_ncamerica_2018 * 5
base_year_ncamerica = base_year_ncamerica[: len(q4_at_total.index)]
q4_at_total['Base year NorthCentralAmerica (2018)'] = base_year_ncamerica
q4_at_total['Percentage NorthCentralAmerica'] = (q4_at_total['NorthCentralAmerica'] - q4_at_total['Base year NorthCentralAmerica (2018)'])/q4_at_total['Base year NorthCentralAmerica (2018)'] * 100

#SOUTH AMERICA
base_year_southamerica_2018 = q4_at_total['South America'].to_list()
base_year_southamerica_2018 = base_year_southamerica_2018[0:12]
base_year_southamerica = []

base_year_southamerica = base_year_southamerica_2018 * 5
base_year_southamerica = base_year_southamerica[: len(q4_at_total.index)]
q4_at_total['Base year South America (2018)'] = base_year_southamerica
q4_at_total['Percentage South America'] = (q4_at_total['South America'] - q4_at_total['Base year South America (2018)'])/q4_at_total['Base year South America (2018)'] * 100

#ASIA
base_year_asia_2018 = q4_at_total['Asia'].to_list()
base_year_asia_2018 = base_year_asia_2018[0:12]
base_year_asia = []

base_year_asia = base_year_asia_2018 * 5
base_year_asia = base_year_asia[: len(q4_at_total.index)]
q4_at_total['Base year Asia (2018)'] = base_year_asia
q4_at_total['Percentage Asia'] = (q4_at_total['Asia'] - q4_at_total['Base year Asia (2018)'])/q4_at_total['Base year Asia (2018)'] * 100

#OCEANIA
base_year_oceania_2018 = q4_at_total['Oceania'].to_list()
base_year_oceania_2018 = base_year_oceania_2018[0:12]
base_year_oceania = []

base_year_oceania = base_year_oceania_2018 * 5
base_year_oceania = base_year_oceania[: len(q4_at_total.index)]
q4_at_total['Base year Oceania (2018)'] = base_year_oceania
q4_at_total['Percentage Oceania'] = (q4_at_total['Oceania'] - q4_at_total['Base year Oceania (2018)'])/q4_at_total['Base year Oceania (2018)'] * 100

#AFRICA
base_year_africa_2018 = q4_at_total['Africa'].to_list()
base_year_africa_2018 = base_year_africa_2018[0:12]
base_year_africa = []

base_year_africa = base_year_africa_2018 * 5
base_year_africa = base_year_africa[: len(q4_at_total.index)]
q4_at_total['Base year Africa (2018)'] = base_year_africa
q4_at_total['Percentage Africa'] = (q4_at_total['Africa'] - q4_at_total['Base year Africa (2018)'])/q4_at_total['Base year Africa (2018)'] * 100

#q4_at_total


# In[60]:


#DATAFRAME WITH ONLY PERIOD AND PERCENTAGE PER CONTINENT
q4_at_percentage = q4_at_total
q4_at_percentage = q4_at_percentage[['Periods', 
'Percentage Europe',
'Percentage NorthCentralAmerica',
'Percentage South America',
'Percentage Asia',
'Percentage Oceania',
'Percentage Africa']]

q4_at_percentage = q4_at_percentage.set_index('Periods')
q4_at_percentage.head()


# In[67]:


#this figure shows the relative change for the different continents over the time

fig = px.line(q4_at_percentage, y = ['Percentage Europe', 'Percentage NorthCentralAmerica', 'Percentage South America', 'Percentage Asia', 'Percentage Oceania', 'Percentage Africa'])
fig.update_layout(title='Relative change of the number of passengers per continent', xaxis_title= 'Date', yaxis_title = '% incline or decline') 
fig.show()

#Tekst bij figuure


# 
