import streamlit as st

st.set_page_config(layout="wide")

font_size = 60

font_size_subject = 25

col1,col2 = st.columns([1,4])
with col1:
    st.image("LOGO.png",width=200,use_container_width=False)
# Use the fixed font size in the HTML
with col2:
    st.markdown(f"<h1 style= 'color: #008000; font-size: {font_size}px;'>World Happiness Report</h1>",unsafe_allow_html=True)

st.write("")

st.markdown(
    f"<h4 style = 'color: #808080; font-size: {font_size_subject}px;'>The World Happiness Report is an annual publication that ranks countries based on various factors that contribute to the well-being and happiness of their citizens.</h4>",
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
        <li style='color: #000080; font-size: {font_size_2}px;'>NGO Insights from World Happiness Data</li>
        <li style='color: #000080; font-size: {font_size_2}px;'>Government Insights from World Happiness Data</li>
    </ol>
        
    """, 
    unsafe_allow_html=True
)







