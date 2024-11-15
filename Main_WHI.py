import streamlit as st


#Page

Homepage = st.Page(page = "C:/Users/91814/OneDrive/World Health Index/All_Pages/WHI.py",
                   title = "Home"
                   )

NGO_Insights = st.Page(page = "C:/Users/91814/OneDrive/World Health Index/All_Pages/NGO_WHI.py",
                        title = "NGO_Dashboard"
                        )

GOVT_Insights = st.Page(page = "C:/Users/91814/OneDrive/World Health Index/All_Pages/Govt_WHS.py",
                        title = "Government_Dashboard"
                        )

pg = st.navigation(pages = [Homepage,NGO_Insights,GOVT_Insights])


pg.run()