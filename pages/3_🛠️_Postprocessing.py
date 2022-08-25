import streamlit as st

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

def plot(s1=(-0.2, 0.2),
         s2=(0.8, 1.2),
         a =(0.5, 1.5)):

    ens = np.array([5.3 , 5.17, 2.08, 4.  , 2.83, 4.05, 2.53, 1.28, 0.8 , 1.  ])
    d = len(ens)

    hs2 = (4 / 3 / d) ** 0.4
    s2 = hs2 * s1 + s2 * a ** 2 * ens.var()
    width = np.sqrt(s2)

    fig, ax = plt.subplots()
    x = np.linspace(-2,8, 200)
    y = norm.pdf(x, loc=ens.mean(), scale=ens.std())

    yd = np.zeros_like(x)
    for i in range(d):
        yi = norm.pdf(x, loc=ens[i], scale=width)
        ax.plot(x,yi, color='gray', alpha=0.2)
        yd[:] = yd[:] + yi

    ydd = yd /d
    ax.scatter(ens, np.zeros_like(ens))
    ax.plot(x,y, label="Normal distribution",color='red')
    ax.plot(x,ydd, label="Dressed", color='blue')
    ax.set_yticks([],[])
    ax.legend(loc="upper right")
    ax.set_title(f"Bandwidth={width:.2f}")
    
    return fig

st.sidebar.header("Parameters")

with st.sidebar:
    s1 = st.slider("s1",-1.0,1.0,0.0)
    s2 = st.slider("s2",0.8,1.2,1.0)
    a = st.slider("a",0.5,1.5,1.0)

fig = plot(s1,s2,a)

st.pyplot(fig)