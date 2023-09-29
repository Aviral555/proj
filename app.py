import streamlit as st
import pandas as pd

# Create a dummy dataset
dummy_data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population (millions)': [331, 38, 67, 83, 67],
    'GDP (trillion USD)': [21.43, 1.64, 2.83, 4.21, 2.72],
    'Poverty Rate (%)': [12.3, 8.7, 10.9, 6.2, 9.8]
}

# Create a Streamlit app
def main():
    st.title("Country Data Comparison")

    # Create a DataFrame from the dummy data
    df = pd.DataFrame(dummy_data)

    # Display the data table
    st.subheader("Dummy Country Data")
    st.write(df)

if __name__ == "__main__":
    main()
