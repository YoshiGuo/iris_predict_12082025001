import streamlit as st 
import joblib

pg = st.navigation([
                st.Page('pages/p1.py', title = 'IRIS Information'),
                st.Page('pages/p2.py', title = 'IRIS Type predict')
               ])
pg.run()