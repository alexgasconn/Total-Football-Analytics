import streamlit as st
from utils.data_loader import load_match_data, load_odds
from utils.visualizer import plot_odds_change

@st.cache_data(show_spinner=True)
def get_odds(cfg):
    match_df = load_match_data(cfg)
    return load_odds(match_df, cfg)

def render():
    st.header("💰 Betting Odds Tracker")
    cfg = st.session_state["config"]

    odds_df = get_odds(cfg)
    if odds_df.empty:
        st.warning("No odds data available.")
        return

    st.altair_chart(plot_odds_change(odds_df), use_container_width=True)
    st.dataframe(
        odds_df[['game_id', 'market_name', 'choice_name', 'initial_fractional_value', 'current_fractional_value']],
        use_container_width=True
    )
