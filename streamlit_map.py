import streamlit as st
import pandas as pd
import numpy as np

st.header("This an example on geographical Map")
 
data = {"lat":[48.866669],
        "lon":[2.33333],
        "City": ["Paris"]}
 
df = pd.DataFrame(data)
df
st.map(data=df)
