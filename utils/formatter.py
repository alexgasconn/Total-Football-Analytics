import pandas as pd

def format_match_table(df):
    df = df.copy()
    df['Kickoff'] = pd.to_datetime(df['start_timestamp'], unit='s')
    df['Score'] = df['home_score_display'].astype(str) + ' - ' + df['away_score_display'].astype(str)
    return df[['home_team', 'away_team', 'Score', 'Kickoff', 'status']]

def format_stats_table(df):
    df = df.copy()
    return df.pivot_table(
        index=['stat_name'],
        values=['home_team_stat', 'away_team_stat'],
        aggfunc='first'
    )

def format_standings(df):
    df = df.copy()
    return df[['position', 'team_name', 'matches', 'wins', 'draws', 'losses', 'scores_for', 'scores_against', 'points']]
