import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    df_2015 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/DatasetWH/2015.csv")
    df_2016 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/DatasetWH/2016.csv")
    df_2017 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/DatasetWH/2017.csv")
    df_2018 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/DatasetWH/2018.csv")
    df_2019 = pd.read_csv("C:/Users/91814/OneDrive/Desktop/DatasetWH/2019.csv")

    # Add a 'Year' column to each dataset
    df_2015["Year"] = 2015
    df_2016["Year"] = 2016
    df_2017["Year"] = 2017
    df_2018["Year"] = 2018
    df_2019["Year"] = 2019

    return df_2015, df_2016, df_2017, df_2018, df_2019

df_2015, df_2016, df_2017, df_2018, df_2019 = load_data()

# Columns for 2015
df_2015.rename(columns={
    'Country': 'Country',
    'Region': 'Region',
    'Happiness Rank': 'Happiness Rank',
    'Happiness Score': 'Happiness Score',
    'Standard Error': 'Standard Error',
    'Economy (GDP per Capita)': 'GDP',
    'Family': 'Family',
    'Health (Life Expectancy)': 'LifeExpectancy',
    'Freedom': 'Freedom',
    'Trust (Government Corruption)': 'Trust',
    'Generosity': 'Generosity',
    'Dystopia Residual': 'DystopiaResidual'
}, inplace=True)

# Columns for 2016
df_2016.rename(columns={
    'Country': 'Country',
    'Region': 'Region',
    'Happiness Rank': 'Happiness Rank',
    'Happiness Score': 'Happiness Score',
    'Lower Confidence Interval': 'LowerCI',
    'Upper Confidence Interval': 'UpperCI',
    'Economy (GDP per Capita)': 'GDP',
    'Family': 'Family',
    'Health (Life Expectancy)': 'LifeExpectancy',
    'Freedom': 'Freedom',
    'Trust (Government Corruption)': 'Trust',
    'Generosity': 'Generosity',
    'Dystopia Residual': 'DystopiaResidual'
}, inplace=True)

# Columns for 2017
df_2017.rename(columns={
    'Country or region': 'Country',
    'Happiness.Rank': 'Happiness Rank',
    'Happiness.Score': 'Happiness Score',
    'Whisker.high': 'UpperCI',
    'Whisker.low': 'LowerCI',
    'Economy..GDP.per.Capita.': 'GDP',
    'Family': 'Family',
    'Health..Life.Expectancy.': 'LifeExpectancy',
    'Freedom': 'Freedom',
    'Generosity': 'Generosity',
    'Trust..Government.Corruption.': 'Trust',
    'Dystopia.Residual': 'DystopiaResidual'
}, inplace=True)

# Columns for 2018
df_2018.rename(columns={
    'Country or region': 'Country',
    'Overall rank': 'Happiness Rank',
    'Score': 'Happiness Score',
    'GDP per capita': 'GDP',
    'Social support': 'SocialSupport',
    'Healthy life expectancy': 'LifeExpectancy',
    'Freedom to make life choices': 'Freedom',
    'Generosity': 'Generosity',
    'Perceptions of corruption': 'Trust'
}, inplace=True)

# Columns for 2019
df_2019.rename(columns={
    'Country or region': 'Country',
    'Overall rank': 'Happiness Rank',
    'Score': 'Happiness Score',
    'GDP per capita': 'GDP',
    'Social support': 'SocialSupport',
    'Healthy life expectancy': 'LifeExpectancy',
    'Freedom to make life choices': 'Freedom',
    'Generosity': 'Generosity',
    'Perceptions of corruption': 'Trust'
}, inplace=True)



# Sidebar widgets for user input
st.sidebar.header("Happiness Score Analysis")

# Set all years and countries as default selections
all_years = [2015, 2016, 2017, 2018, 2019]

selected_countries = st.sidebar.multiselect("Select Countries:", options=df_2015['Country'].unique(), default=['Finland', 'Denmark', 'Norway'])
selected_years = st.sidebar.multiselect("Select Years:", options= all_years, default=all_years)


year_dataframes = {
    2015: df_2015,
    2016: df_2016,
    2017: df_2017,
    2018: df_2018,
    2019: df_2019
}

# Filter data based on user selection
filtered_data = pd.DataFrame()
for year in selected_years:
    df = year_dataframes[year]
    df_filtered = df[df['Country'].isin(selected_countries)]
    filtered_data = pd.concat([filtered_data, df_filtered], ignore_index=True)

# Title and description
st.title("World Happiness Report")
st.write("The World Happiness Report is an annual publication that ranks countries based on various factors that contribute to the well-being and happiness of their citizens. The World Happiness Report data provides a comprehensive view of the factors that contribute to a country's overall happiness and well-being. The data includes information on various economic, social, and environmental indicators, such as GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, and perceptions of corruption")

st.write("Analyze happiness score trends across countries and years.")

# Plot Happiness Score Trends
st.subheader("Happiness Score Trends Over Time")


plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Happiness Score', hue='Country', data=filtered_data, marker='o')
plt.title('Happiness Score Trends for Selected Countries and Years')
plt.xlabel('Year')
plt.ylabel('Happiness Score')
plt.legend(title='Country')
plt.grid(True)
    
# Display the plot in Streamlit
st.pyplot(plt)


factors = {
    'Economy (GDP per Capita)': 'Economic Factor (GDP per Capita)',
    'Family': 'Social Factor (Social Support)',
    'Health (Life Expectancy)': 'Health Factor (Life Expectancy)'
}
for factor, label in factors.items():
    if factor in filtered_data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=factor, y='Happiness Score', hue='Country', data=filtered_data)
        plt.title(f'Happiness Score vs {label}')
        plt.xlabel(label)
        plt.ylabel('Happiness Score')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(plt)


