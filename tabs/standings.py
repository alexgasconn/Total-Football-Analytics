import streamlit as st
from utils.data_loader import load_standings
from utils.formatter import format_standings

@st.cache_data(show_spinner=True)
def get_standings(cfg):
    return load_standings(cfg)

def render():
    st.header("🔢 League Standings")
    cfg = st.session_state["config"]

    standings_df = get_standings(cfg)
    if standings_df.empty:
        st.warning("No standings data available.")
        return

    st.dataframe(format_standings(standings_df), use_container_width=True)
    st.caption(f"Data for season ID: {cfg['season_id']}")
