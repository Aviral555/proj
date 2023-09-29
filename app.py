import streamlit as st
import requests
import pandas as pd

# Function to fetch COVID-19 data from the disease.sh API
def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to fetch COVID-19 data.")
        return None

def main():
    st.title("COVID-19 Data Comparison")

    # Fetch COVID-19 data from the disease.sh API
    data = fetch_covid_data()

    if data is not None:
        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Select relevant columns
        columns = ['country', 'cases', 'deaths', 'recovered']
        df = df[columns]

        # Display the data table
        st.subheader("COVID-19 Data by Country")
        st.write(df)

if __name__ == "__main__":
    main()
