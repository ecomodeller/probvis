import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.distributions import norm
from scipy import integrate
import properscoring

"""
# Skill assessment

## Accuracy vs precision
"""

st.image("accuracy_precision.png")

"""
## Continous ranked probability score


$ crps(F,y) = \int_{-\infty}^\infty{[F(t) - H(t-y)]^2 dt} $
"""

st.sidebar.header("Parameters")

with st.sidebar:
    loc = st.slider("Mean", min_value=-2.0, max_value=2.0, value=0.0)
    scale = st.slider("Std", min_value=.1, max_value=2.0, value=0.5)
    yobs = st.slider("Obs", min_value=-2.0, max_value=2.0, value=0.0)

fig, ax = plt.subplots()
t = np.linspace(-5,5,200)
dist = norm(loc=loc, scale=scale)
yt = dist.cdf(t)
yt2 = (yt-np.heaviside(t-yobs,yobs))**2
ax.plot(t, yt, label='cdf')
ax.fill_between(t, 0, yt2, label='g')
ax.set_ylim(0,1)
ax.axvline(yobs, label='Observed', linestyle='dashed')
ax.legend(loc='upper left')
crps = properscoring.crps_quadrature(yobs,dist)
#crps_t = np.trapz(yt2, t)
#ax.title(f"CRPS: {crps:.3f}, {crps_t=:.3f})
ax.set_title(f"CRPS: {crps:.3f}")

st.pyplot(fig)