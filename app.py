import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Your Title Here")

df = pd.read_csv('sets.csv')
st.write(df)


# Create a histogram
fig_hist = px.histogram(df, x='Year')

# Create a scatterplot
fig_scatter = px.scatter(df, x='Minifigures', y='Pieces')

# Display the histogram
st.plotly_chart(fig_hist)

# Display the scatterplot
st.plotly_chart(fig_scatter)