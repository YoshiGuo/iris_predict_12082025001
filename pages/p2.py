import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.title = ('IRIS Type predict')
# 載入模型
svm = joblib.load('models/svm.joblib')
knn = joblib.load('models/knn.joblib')
lr = joblib.load('models/LR.joblib')
rf = joblib.load('models/RF.joblib')

# 左側側邊欄
s1 = st.sidebar.selectbox('choose model', ('SVM', 
                                           'KNN',
                                           'LogisticRegression', 
                                           'RandomForest'))
if s1 == 'SVM':
    model = svm
elif s1 == 'KNN':
    model = knn
elif s1 == 'LogisticRegression':
    model = lr
elif s1 == 'RandomForest':
    model = rf    

st.image('iris.png')

# 接收使用者輸入: 4個特徵
df = pd.read_csv('iris.csv')
se1 = st.slider('花萼長度(cm)', float(df['sepal.length'].min())-0.5, 
                float(df['sepal.length'].max())+0.8, 
                float(df['sepal.length'].mean()))   
se2 = st.slider('花萼長度(cm)', float(df['sepal.width'].min())-0.5, 
                float(df['sepal.width'].max())+0.8, 
                float(df['sepal.width'].mean()))  
se3 = st.slider('花瓣長度(cm)', float(df['petal.length'].min())-0.5, 
                float(df['petal.length'].max())+0.8, 
                float(df['petal.length'].mean()))  
se4 = st.slider('花瓣長度(cm)', float(df['petal.width'].min())-0.5, 
                float(df['petal.width'].max())+0.8, 
                float(df['petal.width'].mean()))  

labels = ['Setosa', 'Versicolor', 'Virginica']   

if st.button('進行預測'): 
    X = np.array([[se1, se2, se3, se4]])
    y = model.predict(X)
    st.write(f'### 預測結果: {y}')
    st.write(f'### 品種明稱: {labels[y[0]]}')