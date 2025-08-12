import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title = ('IRIS Information')
df = pd.read_csv('iris.csv')
st.write(df.head())
st.write('### 樣本散佈圖')

fix, ax = plt.subplots()
mapping = {'Setosa':0, 'Versicolor':1, 'Virginica':2}
colors = {'red', 'green', 'blue'}

tab1, tab2 = st.tabs(['依 花 萼 長 寬', '依 花 瓣 長 寬'])
with tab1:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax.scatter(subset['sepal.length'], subset['sepal.width'], label = i)# , c = colors[s]   
    ax.set_xlabel('sepal.length')
    ax.set_ylabel('sepal.width')
    ax.legend()
    st.pyplot(fix)
fix2, ax2 = plt.subplots()    
with tab2:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax2.scatter(subset['petal.length'], subset['petal.width'], label = i)# , c = colors[s]   
    ax2.set_xlabel('petal.length')
    ax2.set_ylabel('petal.width')
    ax2.legend()
    st.pyplot(fix2)