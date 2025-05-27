import pandas as pd
from datafc.sofascore import (
    match_data, match_stats_data, lineups_data, shots_data, momentum_data,
    goal_networks_data, substitutions_data, standings_data, match_odds_data
)

def load_match_data(cfg):
    try:
        return match_data(
            tournament_id=cfg["tournament_id"],
            season_id=cfg["season_id"],
            week_number=cfg["week"],
            data_source=cfg["data_source"],
            enable_json_export=False,
            enable_excel_export=False
        )
    except Exception as e:
        print(f"[load_match_data] Error: {e}")
        return pd.DataFrame()  # Return empty to prevent app crash


def load_lineups(match_df, cfg):
    return lineups_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_stats(match_df, cfg):
    return match_stats_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_shots(match_df, cfg):
    return shots_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_momentum(match_df, cfg):
    return momentum_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_goal_networks(match_df, cfg):
    return goal_networks_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_substitutions(match_df, cfg):
    return substitutions_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )

def load_standings(cfg):
    return standings_data(
        tournament_id=cfg["tournament_id"],
        season_id=cfg["season_id"],
        data_source=cfg["data_source"]
    )

def load_odds(match_df, cfg):
    return match_odds_data(
        match_df=match_df,
        data_source=cfg["data_source"]
    )
