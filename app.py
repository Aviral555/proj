import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Add charts for comparison
    st.subheader("Data Comparison Charts")

    # Bar chart for Population
    st.bar_chart(df.set_index('Country')['Population (millions)'])

    # Bar chart for GDP
    st.bar_chart(df.set_index('Country')['GDP (trillion USD)'])

    # Pie chart for Poverty Rate
    st.subheader("Poverty Rate (%)")
    fig, ax = plt.subplots()
    ax.pie(df['Poverty Rate (%)'], labels=df['Country'], autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

    # Scatter plot for Population vs. GDP
    st.subheader("Scatter Plot: Population vs. GDP")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Population (millions)', y='GDP (trillion USD)')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
