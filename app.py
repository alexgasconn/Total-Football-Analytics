import streamlit as st
from tabs import matches, players, shots, momentum, standings, odds, goal_network
from config import TOURNAMENTS
from utils.sofascore_scraper import get_season_ids

st.set_page_config(page_title="Total Football Analytics", layout="wide")

# Sidebar - Global filters
st.sidebar.title("⚙️ Configuration")

# Select tournament
tournament = st.sidebar.selectbox("Tournament", list(TOURNAMENTS.keys()))
t_info = TOURNAMENTS[tournament]  # contains "id" and "url"

# Get season list dynamically from Sofascore
@st.cache_data(ttl=3600)
def fetch_seasons(url):
    return get_season_ids(url)

season_options = fetch_seasons(t_info["url"])
season_name = st.sidebar.selectbox("Season", list(season_options.keys()))
season_id = season_options[season_name]

# Select data source
data_source = st.sidebar.selectbox("Data Source", ["sofascore", "sofavpn"])

# Estimate max matchweek (default 1–40)
week = st.sidebar.slider("Matchweek", min_value=1, max_value=40, value=1)

# Store config in session
st.session_state["config"] = {
    "tournament_id": t_info["id"],
    "season_id": season_id,
    "week": week,
    "data_source": data_source,
}

# Tabs
TABS = {
    "🏟️ Matches": matches,
    "🧍 Player Stats": players,
    "🎯 Shots & xG": shots,
    "📈 Momentum": momentum,
    "🧠 Goal Network": goal_network,
    "🔢 Standings": standings,
    "💰 Odds": odds,
}

selected_tab = st.sidebar.radio("Sections", list(TABS.keys()))
TABS[selected_tab].render()
