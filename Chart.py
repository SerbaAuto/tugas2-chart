import streamlit as st
import pandas as pd
import numpy as np

st.write("Data Chart")
df = pd.DataFrame(
    np.array([
        [1000,3500,3000,2000,1500,500,300],
        [2000,3000,1000,1500,2000,1600,2000],
        [300,500,700,400,600,760,500]
        ]),
    columns=['Januari','Febuari','Maret','April','Juni','Juli','Agustus']

)
df

