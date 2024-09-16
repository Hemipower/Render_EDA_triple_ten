import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Your Title Here")

df = pd.read_csv('Fuel_Consumption_Ratings_2023.csv',encoding='latin-1',on_bad_lines='skip')
st.write(df)


# Create a histogram
fig_hist = px.histogram(df, x='Make')

# Create a scatterplot
fig_scatter = px.scatter(df, x='Transmission', y='Fuel Consumption (L/100Km)')

# Display the histogram
st.plotly_chart(fig_hist)

# Display the scatterplot
st.plotly_chart(fig_scatter)