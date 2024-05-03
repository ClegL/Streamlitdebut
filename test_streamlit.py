import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities !")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

colonnes_num = df_weather.select_dtypes(include=['number'])

import seaborn as sns
viz_correlation = sns.heatmap(colonnes_num.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)