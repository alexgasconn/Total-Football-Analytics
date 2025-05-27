import streamlit as st
from utils.data_loader import load_match_data, load_shots
from utils.visualizer import plot_shots_map

@st.cache_data(show_spinner=True)
def get_shots(cfg):
    match_df = load_match_data(cfg)
    return load_shots(match_df, cfg)

def render():
    st.header("🎯 Shot Map & xG")
    cfg = st.session_state["config"]

    shots_df = get_shots(cfg)
    if shots_df.empty:
        st.warning("No shot data available.")
        return

    st.altair_chart(plot_shots_map(shots_df), use_container_width=True)
    st.dataframe(
        shots_df[['player_name', 'xg', 'incident_type', 'player_coordinates_x', 'player_coordinates_y']],
        use_container_width=True
    )
