import streamlit as st

# 1. Set the Page Config (Global for the app)
# NOTE: You must remove st.set_page_config from Home.py, Analysis.py, and team.py
st.set_page_config(page_title="QARM Dashboard", page_icon="📈", layout="wide")

# 2. Define the Pages
# The first argument is the filename. Since they are in the same folder, just use the name.
home_page = st.Page("Home.py", title="Home", icon="🏠", default=True)
analysis_page = st.Page("Analysis.py", title="Portfolio Optimizer", icon="📊")
team_page = st.Page("team.py", title="Meet the Team", icon="👥")

# 3. Setup Navigation
pg = st.navigation([home_page, analysis_page, team_page])

# --- Run the App ---
pg.run()