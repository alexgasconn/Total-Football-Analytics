import streamlit as st
from utils.data_loader import load_match_data, load_stats
from utils.formatter import format_stats_table

@st.cache_data(show_spinner=True)
def get_stats(cfg):
    match_df = load_match_data(cfg)
    return load_stats(match_df, cfg)

def render():
    st.header("🧍 Player & Team Statistics")
    cfg = st.session_state["config"]

    stats_df = get_stats(cfg)
    if stats_df.empty:
        st.warning("No stats available.")
        return

    st.dataframe(format_stats_table(stats_df), use_container_width=True)
    st.caption("Showing first-level match stats aggregated by category.")
