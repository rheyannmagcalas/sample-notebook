#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install Streamlit
conda install streamlit


# In[ ]:


# Install Streamlit folium reader
conda install streamlit_folium


# In[ ]:


# Check if Streamlit is installed correctly
import streamlit as st


# ## How to use this guide
# To run streamlit:
# 1. Open a text file then copy the code from one cell and save it as *filename.py*. ***OR***  
#    Copy one cell to new Jupyter notebook then download as .py
# 
# 
# 2. In your anaconda prompt or terminal, go to the folder you saved the .py file in.
# 3. Type "streamlit run *filename.py*"
# 4. A new window should open displaying the results of the code. If not, click on the local URL.
# 5. Paste the content of a new cell in the same .py file then save. Refresh the streamlit window to view the updated output. 

# In[ ]:


# 1: Seeing your data in Streamlit with st.write
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("schools_combined.csv")

# st.write tells streamlit to write the content in the web app.
st.write(df.head())


# In[ ]:


# 2: Using magic commands
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("schools_combined.csv")

#But with magic commands, putting any variable in a new line witll be read by streamlit
top10 = df.head(10)
top10


# In[ ]:


# 3: Adding text in page
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Add title to the page
st.title("Data")
# Add section header
st.header("Public School Data in the Philippines")

# Add any text
data_load_state = st.text('Loading data...')
df = pd.read_csv("schools_combined.csv")
st.write(df.head(20))
# Customize texts using markdown
data_load_state.markdown('Loading data...**done!**')


# In[ ]:


# 4: Adding plots to Streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.title("Data")
st.header("Public School Data in the Philippines")

data_load_state = st.text('Loading data...')
df = pd.read_csv("schools_combined.csv")
st.write(df.head(20))
data_load_state.markdown('Loading data...**done!**')

grade_level = df.groupby("year_level")["enrollment"].sum()

st.header("Count of Students Per Year Level")

#Copy paste your code from Jupyter but assign plt.figure to variable

fig = plt.figure(figsize=(8,6)) 
plt.bar(grade_level.index, grade_level.values) 
plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph by plotting figure variable
plt.show()
st.pyplot(fig)


# In[ ]:


# 5: Adding interactive options: checkbox
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.title("Data")
st.header("Public School Data in the Philippines")
df = pd.read_csv("schools_combined.csv")

if st.checkbox('Show data', value=True):
    st.subheader('Data')
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.markdown('Loading data...**done!**')
    


# In[ ]:


# 6: Adding interactive options: dropdown box
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.title("Data")
st.header("Public School Data in the Philippines")
df = pd.read_csv("schools_combined.csv")

if st.checkbox('Show data', value=True):
    st.subheader('Data')
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.markdown('Loading data...**done!**')

#Create dropdown box
option = st.selectbox(
    'Which region do you want to see?',
     df['region'].unique())
'You selected: ', option

# Filter the entry in the plot
grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

# store figure in fig variable
fig = plt.figure(figsize=(8,6)) 

plt.bar(grade_level.index, grade_level.values) 

plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph
st.pyplot(fig)


# In[ ]:


# 7: Adding options to sidebar
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.title("Data")
st.header("Public School Data in the Philippines")
df = pd.read_csv("schools_combined.csv")

if st.checkbox('Show data', value=True):
    st.subheader('Data')
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.markdown('Loading data...**done!**')

# st.sidebar moves the selectbox to the side
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['region'].unique())
'You selected: ', option

grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

# store figure in fig variable
fig = plt.figure(figsize=(8,6)) 

plt.bar(grade_level.index, grade_level.values) 

plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph
st.pyplot(fig)


# In[ ]:


# 8: Creating pages

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("schools_combined.csv")

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2'])
if my_page == 'page 1':
    st.title("Data")
    st.header("Public School Data in the Philippines")
    df = pd.read_csv("schools_combined.csv")

    if st.checkbox('Show data', value=True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')
    
elif my_page == 'page 2':
    option = st.sidebar. selectbox(
        'Which number do you like best?',
         df['region'].unique())
    'You selected: ', option

    grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(grade_level.index, grade_level.values) 

    plt.title("Students in Public Schools", fontsize=16)
    plt.ylabel("Number of Enrollees", fontsize=12)
    plt.xlabel("Year Level", fontsize=12)
    year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
            "first year", "second year", "third year", "fourth year"]
    plt.xticks(range(len(grade_level.index)), year, rotation=45)

    # display graph
    st.pyplot(fig)


# In[ ]:


# 8: Reading folium in Streamlit (page 3)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import folium_static 
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("schools_combined.csv")

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2', 'page 3'])
if my_page == 'page 1':
    st.title("Data")
    st.header("Public School Data in the Philippines")
    df = pd.read_csv("schools_combined.csv")

    if st.checkbox('Show data', value=True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')
    
elif my_page == 'page 2':
    option = st.sidebar. selectbox(
        'Which number do you like best?',
         df['region'].unique())
    'You selected: ', option

    grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(grade_level.index, grade_level.values) 

    plt.title("Students in Public Schools", fontsize=16)
    plt.ylabel("Number of Enrollees", fontsize=12)
    plt.xlabel("Year Level", fontsize=12)
    year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
            "first year", "second year", "third year", "fourth year"]
    plt.xticks(range(len(grade_level.index)), year, rotation=45)

    # display graph
    st.pyplot(fig)
    
elif my_page == 'page 3':
    st.title("Geospatioal Analysis of Schools")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    schools["x"] = schools.geometry.centroid.x
    schools["y"] = schools.geometry.centroid.y
    #st.write(schools.head(20))
    # Coordinates to show
    map_center = [14.583197, 121.051538]

    # Styling the map
    mymap = folium.Map(location=map_center, height=700, width=1000, tiles="OpenStreetMap", zoom_start=14)
    option_city = st.sidebar.selectbox(
        'Which city',
        schools["Division"].unique())
    'You selected: ', option_city
    city = option_city

    df_city = schools[schools["Division"]==city]

    for i in np.arange(len(df_city)):
        lat = df_city["y"].values[i]
        lon = df_city["x"].values[i]
        name = df_city["School"].values[i]
        folium.Marker([lat, lon], popup=name).add_to(mymap)
    folium_static(mymap)


# In[ ]:


# Plotting maps using st.map (page 4)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import folium_static 
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("schools_combined.csv")

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2', 'page 3', 'page 4'])
if my_page == 'page 1':
    st.title("Data")
    st.header("Public School Data in the Philippines")
    df = pd.read_csv("schools_combined.csv")

    if st.checkbox('Show data', value=True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')
        
elif my_page == 'page 2':
    option = st.sidebar. selectbox(
        'Which number do you like best?',
         df['region'].unique())
    'You selected: ', option

    grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(grade_level.index, grade_level.values) 

    plt.title("Students in Public Schools", fontsize=16)
    plt.ylabel("Number of Enrollees", fontsize=12)
    plt.xlabel("Year Level", fontsize=12)
    year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
            "first year", "second year", "third year", "fourth year"]
    plt.xticks(range(len(grade_level.index)), year, rotation=45)

    # display graph
    st.pyplot(fig)
    
elif my_page == 'page 3':
    st.title("Geospatioal Analysis of Schools : Folium")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    schools["x"] = schools.geometry.centroid.x
    schools["y"] = schools.geometry.centroid.y
    #st.write(schools.head(20))
    # Coordinates to show
    map_center = [14.583197, 121.051538]

    # Styling the map
    mymap = folium.Map(location=map_center, height=700, width=1000, tiles="OpenStreetMap", zoom_start=14)
    option_city = st.sidebar.selectbox(
        'Which city',
        schools["Division"].unique())
    'You selected: ', option_city
    city = option_city

    df_city = schools[schools["Division"]==city]

    for i in np.arange(len(df_city)):
        lat = df_city["y"].values[i]
        lon = df_city["x"].values[i]
        name = df_city["School"].values[i]
        folium.Marker([lat, lon], popup=name).add_to(mymap)
    folium_static(mymap)
    
elif my_page == 'page 4':
    st.title("Geospatioal Analysis of Schools : st.map")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    # to plot a map using st.map, you need a column names lon and lat
    schools["lon"] = schools.geometry.centroid.x
    schools["lat"] = schools.geometry.centroid.y
    st.map(schools.head(10))


# In[ ]:


# 8: Reading geopandas in Streamlit (page 5)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import folium_static 
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("schools_combined.csv")

my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2', 'page 3', 'page 4', 'page 5'])
if my_page == 'page 1':
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.text('Loading data...done!')
    
elif my_page == 'page 2':
    option = st.sidebar. selectbox(
        'Which number do you like best?',
         df['region'].unique())
    'You selected: ', option

    grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(grade_level.index, grade_level.values) 

    plt.title("Students in Public Schools", fontsize=16)
    plt.ylabel("Number of Enrollees", fontsize=12)
    plt.xlabel("Year Level", fontsize=12)
    year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
            "first year", "second year", "third year", "fourth year"]
    plt.xticks(range(len(grade_level.index)), year, rotation=45)

    # display graph
    st.pyplot(fig)
    
elif my_page == 'page 3':
    st.title("Geospatioal Analysis of Schools : Folium")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    schools["x"] = schools.geometry.centroid.x
    schools["y"] = schools.geometry.centroid.y
    #st.write(schools.head(20))
    # Coordinates to show
    map_center = [14.583197, 121.051538]

    # Styling the map
    mymap = folium.Map(location=map_center, height=700, width=1000, tiles="OpenStreetMap", zoom_start=14)
    option_city = st.sidebar.selectbox(
        'Which city',
        schools["Division"].unique())
    'You selected: ', option_city
    city = option_city

    df_city = schools[schools["Division"]==city]

    for i in np.arange(len(df_city)):
        lat = df_city["y"].values[i]
        lon = df_city["x"].values[i]
        name = df_city["School"].values[i]
        folium.Marker([lat, lon], popup=name).add_to(mymap)
    folium_static(mymap)
    
elif my_page == 'page 4':
    st.title("Geospatioal Analysis of Schools : st.map()")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    schools["lon"] = schools.geometry.centroid.x
    schools["lat"] = schools.geometry.centroid.y
    st.map(schools)
    
elif my_page == 'page 5':
    st.title("Geospatioal Analysis of Schools : Geopandas")
    # To plot easier, a new shapefile was created with the cleaned data
    merged_data = gpd.read_file("map_data_clean.shp")
   
    # Copied from Mapping exercise
    variable = 'Total_Enro'
    vmin, vmax = merged_data["Total_Enro"].min(), merged_data["Total_Enro"].max()

    fig, ax = plt.subplots(1, figsize=(15, 10))
    merged_data.plot(column=variable, cmap='Oranges', linewidth=0.8, ax=ax, edgecolor='0.8', vmin=vmin, vmax=vmax)
    sm = plt.cm.ScalarMappable(cmap='Oranges', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    cbar = fig.colorbar(sm)
    st.pyplot(fig)

