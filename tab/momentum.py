import streamlit as st
from utils.data_loader import load_match_data, load_momentum
from utils.visualizer import plot_momentum

@st.cache_data(show_spinner=True)
def get_momentum(cfg):
    match_df = load_match_data(cfg)
    return load_momentum(match_df, cfg)

def render():
    st.header("📈 Match Momentum")
    cfg = st.session_state["config"]

    momentum_df = get_momentum(cfg)
    if momentum_df.empty:
        st.warning("No momentum data found.")
        return

    st.altair_chart(plot_momentum(momentum_df), use_container_width=True)
    st.dataframe(momentum_df[['game_id', 'minute', 'value']], use_container_width=True)
