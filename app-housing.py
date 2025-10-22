import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')
df = pd.read_csv("housing.csv")
st.header('California Housing Data (1990) by [Zhiqian Zhang]') 
price_slider = st.slider(
    'Minimal Median House Price',
    min_value=0,
    max_value=500001,
    value=200000
)
df = df[df['MedHouseVal'] >= price_slider]
st.subheader('See more filters in the sidebar:')
st.map(df[['Latitude', 'Longitude']])  
plt.figure(figsize=(10, 6))
plt.hist(df['MedHouseVal'], bins=30, color='blue')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
st.pyplot(plt)
with st.sidebar:
    st.subheader('Filters')
    
    location_types = df['OceanProximity'].unique()
    location_filter = st.multiselect(
        'Choose the location type',
        options=location_types,
        default=list(location_types)  
    )
    df = df[df['OceanProximity'].isin(location_filter)]
    with st.sidebar:
      st.subheader('Filters')
    # 提取位置类型的唯一值
      location_types = df['OceanProximity'].unique()
      location_filter = st.multiselect(
        'Choose the location type',
        options=location_types,
        default=list(location_types)  # 默认选中所有类型
    )
    df = df[df['OceanProximity'].isin(location_filter)]
    