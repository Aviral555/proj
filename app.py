import streamlit as st
import requests

# World Bank API Base URL
WB_API_BASE_URL = "https://api.worldbank.org/v2"

# Function to fetch poverty data from the World Bank API
def fetch_poverty_data():
    url = f"{WB_API_BASE_URL}/indicator/SI.POV.DDAY?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[1]
        return data
    else:
        st.error("Failed to fetch poverty data.")
        return None

def main():
    st.title("World Poverty Comparison")

    # Fetch poverty data from the World Bank API
    data = fetch_poverty_data()

    if data is not None:
        # Create a dictionary to store country data
        country_data = {}
        for entry in data:
            country_code = entry['countryiso3code']
            poverty_value = entry['value']
            country_data[country_code] = poverty_value

        # Display a map with poverty levels
        st.map(country_data)

if __name__ == "__main__":
    main()
