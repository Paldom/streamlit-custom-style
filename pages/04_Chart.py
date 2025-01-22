import streamlit as st
import pandas as pd
import numpy as np
from helpers import init_page

def main():
    init_page()

    st.title("Chart Elements")
    st.write("Explore charting capabilities of Streamlit.")

    # Generate some random data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    st.subheader("Line Chart")
    st.line_chart(chart_data)

    st.subheader("Area Chart")
    st.area_chart(chart_data)

    st.subheader("Bar Chart")
    st.bar_chart(chart_data)

    st.subheader("Map Example")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"]
    )
    st.map(map_data)

    st.subheader("Scatter Chart")
    scatter_data = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
    st.scatter_chart(scatter_data)

    st.subheader("Matplotlib or Altair can also be used")
    st.write("Here you could add an Altair chart, Plotly chart, etc.")

if __name__ == "__main__":
    main()
