# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 2020

@author: Haedong Kim
"""

import json
import datetime
import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.figure_factory as ff
from urllib.request import urlopen


# set up
pio.renderers.default = "browser"

# load data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:counties = json.load(response)
df = pd.read_csv('./county_data_new.csv', dtype={'year': int, 'county_code': str})
df = df.sort_values(by=['year'])
ndeath = df['death_all']
min_death = np.min(ndeath)
max_death = np.max(ndeath)

# # subset of df
# idx = np.where(df['year'] == '2017')
# idx = idx[0].tolist()
# df_sub = df.loc[idx, ['year', 'county_code', 'death_all']]

# # plotting
# # other mapbox_style: carto-positron, carto-darkmatter
# fig = px.choropleth_mapbox(df_sub, geojson=counties, locations='county_code', color='death_all',
#                             color_continuous_scale="Inferno",
#                             range_color=(0, 1100),
#                             mapbox_style="open-street-map",
#                             zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
#                             opacity=0.5)
# fig.show()

fig = px.choropleth_mapbox(df, geojson=counties, locations='county_code', color='death_all',
                           color_continuous_scale="Inferno",
                           range_color=(min_death, max_death),
                           mapbox_style="open-street-map",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           animation_frame = 'year')
fig.show()
