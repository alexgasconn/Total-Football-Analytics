from utils.sofascore_scraper import get_season_ids

# Sidebar
st.sidebar.title("⚙️ Configuration")
tournament = st.sidebar.selectbox("Tournament", list(TOURNAMENTS.keys()))
t_info = TOURNAMENTS[tournament]

@st.cache_data(ttl=3600)
def fetch_seasons(url):
    return get_season_ids(url)

season_options = fetch_seasons(t_info["url"])
season_name = st.sidebar.selectbox("Season", list(season_options.keys()))
season_id = season_options[season_name]

# Estimate matchweek range (default: 1–40)
max_week = st.sidebar.slider("Matchweek", min_value=1, max_value=40, value=1)

data_source = st.sidebar.selectbox("Data Source", ["sofascore", "sofavpn"])

st.session_state["config"] = {
    "tournament_id": t_info["id"],
    "season_id": season_id,
    "week": max_week,
    "data_source": data_source,
}
