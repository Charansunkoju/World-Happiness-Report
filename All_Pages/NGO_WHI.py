import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("NGO Insights")

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


# st.subheader("Happiness and Well-Being Data Analysis (2015-2019)")
# Displaying Summary
# st.subheader("Summary Statistics by Region")
# region_summary = merged_df.groupby('region').agg({
#     'happiness_score': ['mean', 'min', 'max'],
#     'economy_gdp_per_capita': 'mean',
#     'health_life_expectancy': 'mean',
#     'trust_government_corruption': 'mean',
#     'freedom': 'mean'
# }).reset_index()
# st.dataframe(region_summary)


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the merged dataset (assuming merged_df is your loaded data)
# merged_df = ... (your dataset loading code)

# Title and Description
st.title("World Happiness Data Analysis (2015-2019)")
st.write("Select a country or year.")

# Interactive View Options
view_option = st.radio("View Data By:", ("Country", "Year"))

# Dynamic Filtering Options Based on Selection
if view_option == "Year":
    year_options = merged_df['Year'].unique()
    selected_year = st.selectbox("Select Year", year_options)
    filtered_df = merged_df[merged_df['Year'] == selected_year]

    # Plot 3: Freedom vs. Trust in Government by Region for Selected Year
    st.subheader(f"Freedom vs. Trust in Government by Region in {selected_year}")
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=filtered_df, x='freedom', y='trust_government_corruption', size='happiness_score', 
                    hue='region', sizes=(40, 400), alpha=0.7)
    plt.title(f"Freedom vs. Trust in Government in {selected_year}")
    plt.xlabel("Freedom to Make Life Choices")
    plt.ylabel("Trust in Government")
    st.pyplot(plt)

    # # Plot 4: Health vs. Happiness Score by Region for Selected Year
    # st.subheader(f"Health (Life Expectancy) vs. Happiness Score by Region in {selected_year}")
    # plt.figure(figsize=(12, 8))
    # sns.scatterplot(data=filtered_df, x='health_life_expectancy', y='happiness_score', hue='region', s=100, marker='o')
    # plt.title(f"Health vs. Happiness Score in {selected_year}")
    # plt.xlabel("Life Expectancy")
    # plt.ylabel("Happiness Score")
    # st.pyplot(plt)

    # Plot 4: Regional Heatmap of Well-Being Metrics for Selected Year
    st.subheader(f"Regional Heatmap of Well-Being Metrics in {selected_year}")
    heatmap_data = filtered_df.groupby('region')[['happiness_score', 'economy_gdp_per_capita', 
                                                  'health_life_expectancy', 'freedom', 'trust_government_corruption']].mean()
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=.5)
    plt.title(f"Well-Being Metrics by Region in {selected_year}")
    st.pyplot(plt)

    st.write("")
    
    # Plot 6: Bar Chart of Happiness Scores by Country for Selected Year
    st.subheader(f"10 Least Happy Countries in {selected_year}")
    plt.figure(figsize=(12, 8))
    sns.barplot(data=filtered_df.sort_values(by="happiness_score", ascending=False).tail(10), 
                x='happiness_score', y='country', palette="plasma")
    plt.title(f"10 Least Happy Countries in {selected_year}")
    plt.xlabel("Happiness Score")
    plt.ylabel("Country")
    st.pyplot(plt)

   

else:
    country_options = merged_df['country'].unique()
    selected_country = st.selectbox("Select Country", country_options)
    filtered_df = merged_df[merged_df['country'] == selected_country]

    # Display Happiness Score Metrics for Each Year
    st.subheader(f"Happiness Score by Year for {selected_country}")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Iterate over each year to display the happiness score as a metric
    years = filtered_df['Year'].unique()
    for i, year in enumerate(sorted(years)):
        year_df = filtered_df[filtered_df['Year'] == year]
        happiness_score = year_df['happiness_score'].values[0] if not year_df.empty else None
        if happiness_score:
            if i == 0:
                col1.metric(label=f"{year}", value=f"{happiness_score:.2f}")
            elif i == 1:
                col2.metric(label=f"{year}", value=f"{happiness_score:.2f}")
            elif i == 2:
                col3.metric(label=f"{year}", value=f"{happiness_score:.2f}")
            elif i == 3:
                col4.metric(label=f"{year}", value=f"{happiness_score:.2f}")
            elif i == 4:
                col5.metric(label=f"{year}", value=f"{happiness_score:.2f}")

    # Plot 1: Happiness Score Trend for Selected Country
    st.subheader(f"Happiness Score Trend for {selected_country}")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_df, x='Year', y='happiness_score', marker='o',color="red")
    plt.title(f"Happiness Score Over Time for {selected_country}")
    plt.xlabel("Year")
    plt.ylabel("Happiness Score")
    st.pyplot(plt)

    # Plot 2: Happiness Score vs. GDP Per Capita
    st.subheader(f"Happiness Score vs. GDP per Capita for {selected_country}")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_df, x='economy_gdp_per_capita', y='happiness_score', hue='Year',s=60, marker='o')
    plt.title(f"Happiness Score vs. GDP per Capita for {selected_country}")
    plt.xlabel("GDP per Capita")
    plt.ylabel("Happiness Score")
    st.pyplot(plt)




# st.subheader("Happiness Score Trends Over Time by Region")
# plt.figure(figsize=(14, 8))
# sns.lineplot(data=merged_df, x='Year', y='happiness_score', hue='region', marker='o')
# plt.title("Happiness Score Trends by Region (2015-2019)")
# plt.ylabel("Happiness Score")
# st.pyplot(plt)

st.subheader("Average Trust in Government by Region")
plt.figure(figsize=(12, 6))
trust_data = merged_df.groupby('region')['trust_government_corruption'].mean().sort_values()
sns.barplot(x=trust_data, y=trust_data.index, palette="viridis")
plt.xlabel("Average Trust in Government (Low to High)")
st.pyplot(plt)


