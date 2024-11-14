import streamlit as st

st.set_page_config(layout="wide")

# Sidebar widgets for user input
# st.sidebar.header("Happiness Score Analysis")

# Set all years and countries as default selections
# all_years = merged_df["Year"].unique()

# selected_countries = st.sidebar.multiselect("Select Countries:", options = merged_df["country"].unique(), default=["Finland"])
# selected_years = st.sidebar.multiselect("Select Years:", options= all_years, default=all_years)

# Filter data based on user selection
# filtered_data = pd.DataFrame()
# for year in selected_years:
#     df_filtered = merged_df[merged_df["country"].isin(selected_countries)]
#     filtered_data = pd.concat([filtered_data, df_filtered], ignore_index=True)


font_size = 60

font_size_subject = 25

# Use the fixed font size in the HTML
st.markdown(
    f"<h1 style='text-align: center; color: #008000; font-size: {font_size}px;'>World Happiness Report</h1>",
    unsafe_allow_html=True
)

st.write("")
st.markdown(
    f"<h4 style = 'color: #808080; font-size: {font_size_subject}px;'>The World Happiness Report is an annual publication that ranks countries based on various factors that contribute to the well-being and happiness of their citizens. The World Happiness Report data provides a comprehensive view of the factors that contribute to a country overall happiness and well-being. The data includes information on various economic, social, and environmental indicators, such as GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, and perceptions of corruption</h4>",
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")



# Define the font sizes 
font_size_1 = 40  # Larger size 
font_size_2 = 29    # Smaller size 

# Display the formatted text with sizes applied
st.markdown(
    f"""
    <h4 style='color: #4D4D4D; font-size: {font_size_1}px;'>What we will see in this Report?</h4>
    <ol>
        <li style='color: #000080; font-size: {font_size_2}px;'>NGO Insights from World Happines Data</li>
        <li style='color: #000080; font-size: {font_size_2}px;'>Government Insights from World Happines Data</li>
    </ol>
        
    """, 
    unsafe_allow_html=True
)







