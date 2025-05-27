import streamlit as st
from tabs import matches, players, shots, momentum, standings, odds, goal_network
from config import TOURNAMENTS, SEASONS

st.set_page_config(page_title="Total Football Analytics", layout="wide")

# Sidebar - Global filters
st.sidebar.title("⚙️ Configuration")
tournament = st.sidebar.selectbox("Tournament", TOURNAMENTS.keys())
season_id = st.sidebar.selectbox("Season", SEASONS[tournament])
data_source = st.sidebar.selectbox("Data Source", ["sofascore", "sofavpn"])
week = st.sidebar.number_input("Matchweek", min_value=1, value=1)

# Store config in session
st.session_state["config"] = {
    "tournament_id": TOURNAMENTS[tournament],
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
