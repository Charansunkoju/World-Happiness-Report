import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    df_2015 = pd.read_csv("DatasetWH/2015.csv")
    df_2016 = pd.read_csv("DatasetWH/2016.csv")
    df_2017 = pd.read_csv("DatasetWH/2017.csv")
    df_2018 = pd.read_csv("DatasetWH/2018.csv")
    df_2019 = pd.read_csv("DatasetWH/2019.csv")
    
    # Add a 'Year' column to each dataset
    df_2015["Year"] = 2015
    df_2016["Year"] = 2016
    df_2017["Year"] = 2017
    df_2018["Year"] = 2018
    df_2019["Year"] = 2019

    return df_2015, df_2016, df_2017, df_2018, df_2019

#Load Data
df_2015, df_2016, df_2017, df_2018, df_2019 = load_data()
    
#Making all columns look similar
rename_mapping = {
    'Happiness.Rank': 'happiness_rank',
    'Happiness.Score': 'happiness_score',
    'Happiness Rank':'happiness_rank',
    'Happiness Score':'happiness_score',
    'Whisker.high': 'upper_confidence_interval',
    'Upper Confidence Interval': 'upper_confidence_interval',
    'Whisker.low': 'lower_confidence_interval',
    'Lower Confidence Interval': 'lower_confidence_interval',
    'Economy..GDP.per.Capita.': 'economy_gdp_per_capita',
    'Economy (GDP per Capita)':'economy_gdp_per_capita',
    'Health..Life.Expectancy.': 'health_life_expectancy',
    'Trust..Government.Corruption.': 'trust_government_corruption',
    'Dystopia.Residual': 'dystopia_residual',
    'Dystopia Residual': 'dystopia_residual',
    'Overall rank': 'happiness_rank',
    'Country or region': 'country',
    'Country':'country',
    'Region':'region',
    'Standard Error':'standard_error',
    'Score': 'happiness_score',
    'GDP per capita': 'economy_gdp_per_capita',
    'Social support': 'family',
    'Family':'family',
    'Healthy life expectancy': 'health_life_expectancy',
    'Health (Life Expectancy)': 'health_life_expectancy',
    'Freedom to make life choices': 'freedom',
    'Freedom': 'freedom',
    'Perceptions of corruption': 'trust_government_corruption',
    'Trust (Government Corruption)': 'trust_government_corruption'
}

#Logic for standardize columns
def standardize_columns(df_2015, df_2016, df_2017, df_2018, df_2019):
    standardized_dfs = []
    
    for df in [df_2015, df_2016, df_2017, df_2018, df_2019]:
        df = df.rename(columns=rename_mapping)
        standardized_dfs.append(df)
    
    return standardized_dfs

#Merging Dataframes by keeping columns standardized
merged_df = pd.concat(standardize_columns(df_2015, df_2016, df_2017, df_2018, df_2019), axis=0, ignore_index=True)

#Logic for filling missing values in region
country_to_region = {}
for index, row in merged_df.iterrows():
    country = row['country']
    region = row['region']
    if pd.notna(region):
        if country not in country_to_region:
            country_to_region[country] = region

#Filling missing region values with the corresponding country value
merged_df['region'] = merged_df.apply(lambda row: country_to_region.get(row['country'], row['region']), axis=1)

#Drop rows with missing values
merged_df = merged_df.dropna(subset=['trust_government_corruption', 'region'])

#Drop certain columns
drop = ["standard_error","lower_confidence_interval","upper_confidence_interval"]
merged_df.drop(columns = drop,inplace=True)

st.title("Government Insights for Happiness Factors")

# Display insights within tabs
tabs = st.tabs(["Economic Stability (GDP)", "Health (Life Expectancy)", "Social Support", "Freedom", "Trust in Government"])

# year_range = merged_df['Year'].min()
# year_range1 = merged_df['Year'].max()

with tabs[0]:  # Economic Stability (GDP)
    st.header("Economic Stability (GDP per Capita)")
    st.write("Higher GDP per capita is strongly correlated with happiness.")

    # Year selection
    year = st.selectbox("Select Year", options=merged_df['Year'].unique(),key="gdp_key")
    filtered_data = merged_df[merged_df['Year'] == year]
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='economy_gdp_per_capita', y='happiness_score', hue='Year', palette='viridis', ax=ax)
    st.pyplot(fig)

with tabs[1]:  # Health (Life Expectancy)
    st.header("Health and Life Expectancy")
    st.write("Life expectancy is an essential factor in citizen happiness.")

    # Year selection
    year = st.selectbox("Select Year", options=merged_df['Year'].unique(),key="health_key")
    filtered_data = merged_df[merged_df['Year'] == year]
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='health_life_expectancy', y='happiness_score', hue='Year', palette='plasma', ax=ax)
    st.pyplot(fig)

with tabs[2]:  # Social Support
    st.header("Social Support (Family)")
    st.write("Stronger social support is associated with higher happiness.")

    # Year selection
    year = st.selectbox("Select Year", options=merged_df['Year'].unique(),key="family_key")
    filtered_data = merged_df[merged_df['Year'] == year]
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='family', y='happiness_score', hue='Year', palette='coolwarm', ax=ax)
    st.pyplot(fig)

with tabs[3]:  # Freedom
    st.header("Freedom to Make Life Choices")
    st.write("Personal freedom correlates positively with happiness.")

    # Year selection
    year = st.selectbox("Select Year", options=merged_df['Year'].unique(),key="freedom_key")
    filtered_data = merged_df[merged_df['Year'] == year]
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='freedom', y='happiness_score', hue='Year', palette='cividis', ax=ax)
    st.pyplot(fig)

with tabs[4]:  # Trust in Government
    st.header("Trust in Government (Low Corruption)")
    st.write("Higher trust in government positively impacts happiness.")
    
    # Year selection
    year = st.selectbox("Select Year", options=merged_df['Year'].unique(),key="corrupt_key")
    filtered_data = merged_df[merged_df['Year'] == year]

    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='trust_government_corruption', y='happiness_score', hue='Year', palette='magma', ax=ax)
    st.pyplot(fig)




