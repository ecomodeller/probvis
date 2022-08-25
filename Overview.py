import streamlit as st
from scipy.stats import norm, uniform
import numpy as np
import pandas as pd
import plotly.express as px

"""
# Probilistic forecasting in practice
"""


x = np.linspace(-5,5,501)

df = pd.DataFrame(dict(x=x))
df = df.set_index("x")

df['pdf_norm'] = norm.pdf(x)
df['cdf_norm'] = norm.cdf(x)
df['pdf_uniform'] = uniform(-2,4).pdf(x)
df['cdf_uniform'] = uniform(-2,4).cdf(x)

fig = px.line(df)

st.plotly_chart(fig)