import streamlit as st
import pandas as pd
import numpy as np
from helpers import init_page

def main():
    init_page()

    st.title("Data Elements")
    st.write("This page demonstrates data-related elements like tables and dataframes.")

    # Sample DataFrame
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=[f"col_{i}" for i in range(1, 6)]
    )

    st.subheader("DataFrame")
    st.dataframe(df, use_container_width=True)

    st.subheader("Table")
    st.table(df.head())

    st.subheader("Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Humidity", "45%", "-2%")
    col3.metric("Wind Speed", "10 mph", "0 mph")

    st.subheader("JSON Display")
    st.json({"sample_key": "sample_value", "numbers": [1, 2, 3]})

if __name__ == "__main__":
    main()
