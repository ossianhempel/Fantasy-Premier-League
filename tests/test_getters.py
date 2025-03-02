import requests
import json

from getters import (
    get_data,
    get_individual_player_data,
    get_entry_data,
    get_entry_personal_data,
    get_entry_gws_data,
    get_entry_transfers_data,
    get_fixtures_data,
)

def test_get_data():
    data = get_data()

    assert isinstance(data, dict), f"Data was not in expected format: {type(data)}"
    assert data["chips"], f"Data did not conform to expected format: {data.values()}"

def test_get_individual_player_data():
    data = get_individual_player_data(19)

    expected_keys = ["fixtures", "history", "history_past"]

    expected_fixtures_schema = [
        "id",
        "code",
        "team_h",
        "team_h_score",
        "team_a",
        "team_a_score",
        "event",
        "finished",
        "minutes",
        "provisional_start_time",
        "kickoff_time",
        "event_name",
        "is_home",
        "difficulty",
    ]

    expected_history_schema = [
        "element",
        "fixture",
        "opponent_team",
        "total_points",
        "was_home",
        "kickoff_time",
        "team_h_score",
        "team_a_score",
        "round",
        "modified",
        "minutes",
        "goals_scored",
        "assists",
        "clean_sheets",
        "goals_conceded",
        "own_goals",
        "penalties_saved",
        "penalties_missed",
        "yellow_cards",
        "red_cards",
        "saves",
        "bonus",
        "bps",
        "influence",
        "creativity",
        "threat",
        "ict_index",
        "starts",
        "expected_goals",
        "expected_assists",
        "expected_goal_involvements",
        "expected_goals_conceded",
        "mng_win",
        "mng_draw",
        "mng_loss",
        "mng_underdog_win",
        "mng_underdog_draw",
        "mng_clean_sheets",
        "mng_goals_scored",
        "value",
        "transfers_balance",
        "selected",
        "transfers_in",
        "transfers_out",
    ]

    expected_history_past_schema = [
        "season_name",
        "element_code",
        "start_cost",
        "end_cost",
        "total_points",
        "minutes",
        "goals_scored",
        "assists",
        "clean_sheets",
        "goals_conceded",
        "own_goals",
        "penalties_saved",
        "penalties_missed",
        "yellow_cards",
        "red_cards",
        "saves",
        "bonus",
        "bps",
        "influence",
        "creativity",
        "threat",
        "ict_index",
        "starts",
        "expected_goals",
        "expected_assists",
        "expected_goal_involvements",
        "expected_goals_conceded",
        "mng_win",
        "mng_draw",
        "mng_loss",
        "mng_underdog_win",
        "mng_underdog_draw",
        "mng_clean_sheets",
        "mng_goals_scored",
    ]

    assert isinstance(data, dict), f"Data was not in expected format: {type(data)}"
    assert data["fixtures"], f"Data did not conform to expected format: {data.values()}"
    assert list(data.keys()) == expected_keys, f"Wrong keys, got: {list(data.keys())}, was looking for: {expected_keys}"


def test_get_entry_data():
    data = get_entry_data(4)

    assert isinstance(data, dict), f"Data was not in expected format: {type(data)}"
    assert data["current"], f"Data did not conform to expected format: {data.values()}"
    assert data["past"], f"Data did not conform to expected format: {data.values()}"
    assert data["chips"], f"Data did not conform to expected format: {data.values()}"


def test_get_entry_personal_data():
    data = get_entry_personal_data(9)

    assert isinstance(data, dict), f"Data was not in expected format: {type(data)}"
    assert data["id"], f"Data did not conform to expected format: {data.values()}"
    assert data["joined_time"], f"Data did not conform to expected format: {data.values()}"
    assert data["years_active"], f"Data did not conform to expected format: {data.values()}"

def test_get_entry_gws_data():
    data = get_entry_gws_data(3, num_gws=3, start_gw=2)

    assert isinstance(data, list), f"Data was not in expected format: {type(data)}"
    assert "active_chip" in data[0], f"Data did not conform to expected format: {data[0]}"
    assert "automatic_subs" in data[1], f"Data did not conform to expected format: {data[1]}"
    assert data[1]["entry_history"], f"Data did not conform to expected format: {data.values[1]}"

def test_get_entry_transfers_data():
    data = get_entry_transfers_data(2)
    assert isinstance(data, list), f"Data was not in expected format: {type(data)}"
    assert isinstance(data[0], dict), f"Data was not in expected format: {type(data)}"

def test_get_fixtures_data():
    data = get_fixtures_data()
    
    assert isinstance(data, list), f"Data was not in expected format: {type(data)}"
    assert isinstance(data[0], dict), f"Data was not in expected format: {type(data)}"
