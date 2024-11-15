import streamlit as st


#Page

Homepage = st.Page(page = "All_Pages/WHI.py",
                   title = "Home"
                   )

NGO_Insights = st.Page(page = "All_Pages/NGO_WHI.py",
                        title = "NGO_Dashboard"
                        )

GOVT_Insights = st.Page(page = "All_Pages/Govt_WHS.py",
                        title = "Government_Dashboard"
                        )

pg = st.navigation(pages = [Homepage,NGO_Insights,GOVT_Insights])


pg.run()
