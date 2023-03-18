import streamlit as st
import pandas as pd
import numpy as np


st.slider(
    'Select a range of values',
    min_value =0,max_value=100,key="value")
st.write('Values:', st.session_state.value)