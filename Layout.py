import streamlit as st
import pandas as pd
import numpy as np

tab1,tab2 = st.tabs(["Chart","Widget"])

with tab1:
    st.write("Data Chart")
    df = pd.DataFrame(
        np.array([
            [1000,3500,3000,2000,1500,500,300],
            [2000,3000,1000,1500,2000,1600,2000],
            [300,500,700,400,600,760,500]
            ]),
        columns=['Januari','Febuari','Maret','April','Juni','Juli','Agustus']

    )
    st.line_chart(df)
    
with tab2:
    st.slider(
    'Select a range of values',
    min_value =0,max_value=100,key="value")
    st.write('Values:', st.session_state.value)