import streamlit as st
from utils.data_loader import load_match_data
from utils.formatter import format_match_table

@st.cache_data(show_spinner=True)
def get_data(cfg):
    return load_match_data(cfg)

def render():
    st.header("🏟️ Match Overview")
    cfg = st.session_state["config"]

    match_df = get_data(cfg)
    if match_df.empty:
        st.warning("No match data available for selected options.")
        return

    st.dataframe(format_match_table(match_df), use_container_width=True)
    st.caption(f"Total matches: {len(match_df)}")
