import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px



st.title("Fuel Consumption EDA")

df = pd.read_csv('Fuel_Consumption_Ratings_2023.csv',encoding='latin-1',on_bad_lines='skip')
df_z = df[df['Fuel Type']=='Z']
df_x = df[df['Fuel Type']=='X']
df_d = df[df['Fuel Type']=='D']
df_e = df[df['Fuel Type']=='E']

# Create a histogram
f_type = st.radio("Select a Fuel type",["Z","X","D","E"])
checkbox = st.checkbox("Check this to turn on multiple fuel mode")
if checkbox:
    if f_type =="Z":
        fig_hist = px.histogram(df_z, x='Make')
    elif f_type =="X":
        fig_hist = px.histogram(df_x, x='Make')
    elif f_type =="D":
        fig_hist = px.histogram(df_d, x='Make')
    elif f_type =="E":
        fig_hist = px.histogram(df_e, x='Make')
else:
    fig_hist = px.histogram(df, x='Make')

# Create a scatterplot
fig_scatter = px.scatter(df, x='Transmission', y='Fuel Consumption (L/100Km)')

# Display the histogram
st.plotly_chart(fig_hist)

# Display the scatterplot
st.plotly_chart(fig_scatter)