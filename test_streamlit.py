import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_cars = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

cols_num = df_cars.select_dtypes(include=['number']).columns

st.subheader('Analyse de corrélation')
corr = df_cars[cols_num].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

# Nous pouvons constater des corrélations évidentes entre les colonnes hp
# cubicinches, cylinders and weights puisqu'elles concernent la 
# partie mécanique contrairement à year et time-to-60 qui ont très peu voir pas
# de corrélations avec les colonnes citées précédemment.

pairplot = sns.pairplot(df_cars[cols_num])
st.pyplot(pairplot.fig)

#Les pairplots permettent de confirmer les corrélations vues précédemment

cols_num = ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60']
df_cars[cols_num] = df_cars[cols_num].apply(pd.to_numeric, errors='coerce')
df_cars.dropna(subset=cols_num, inplace=True)

for col in cols_num:
    st.subheader(f'Distribution de {col}')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df_cars[col], kde=True, ax=ax)
    plt.xlabel(col)
    plt.ylabel('Fréquence')
    st.pyplot(fig)

# Nous voyons ici que les courbes sont globalement descendantes
# montrant des distributions inégales sauf pour la colonne
# 0-to-60

unique_values = df_cars['continent'].unique()

for value in unique_values:
    if st.button(value):
      
        filtered_df = df_cars[df_cars['continent'] == value]
        
        st.write(filtered_df)