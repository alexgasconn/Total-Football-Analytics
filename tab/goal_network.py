import streamlit as st
from utils.data_loader import load_match_data, load_goal_networks

@st.cache_data(show_spinner=True)
def get_goal_network(cfg):
    match_df = load_match_data(cfg)
    return load_goal_networks(match_df, cfg)

def render():
    st.header("🧠 Goal Network Events")
    cfg = st.session_state["config"]

    net_df = get_goal_network(cfg)
    if net_df.empty:
        st.warning("No goal/pass event data found.")
        return

    st.dataframe(
        net_df[['player_name', 'event_type', 'is_assist', 'goal_shot_x', 'goal_shot_y']],
        use_container_width=True
    )
    st.caption("Coming soon: interactive pass/goal network diagram.")
