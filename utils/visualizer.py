import altair as alt
import pandas as pd

def plot_momentum(df):
    chart = alt.Chart(df).mark_line().encode(
        x='minute:Q',
        y='value:Q',
        color='game_id:N',
        tooltip=['minute', 'value']
    ).properties(title='Match Momentum')
    return chart

def plot_shots_map(df):
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x='player_coordinates_x:Q',
        y='player_coordinates_y:Q',
        color='is_home:N',
        size='xg:Q',
        tooltip=['player_name', 'xg', 'incident_type']
    ).properties(width=400, height=300, title='Shot Map')
    return chart

def plot_standings_trend(df):
    chart = alt.Chart(df).mark_line().encode(
        x='week:O',
        y='position:Q',
        color='team_name:N'
    ).properties(title='League Position Over Time')
    return chart

def plot_odds_change(df):
    chart = alt.Chart(df).mark_line().encode(
        x='game_id:N',
        y='current_fractional_value:Q',
        color='choice_name:N'
    ).properties(title='Odds Fluctuation')
    return chart
