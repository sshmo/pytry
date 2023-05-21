import pandas as pd
import pytest

from pytry.general.world_cup.dataframe import DFScoreBoard

data = [
    "2-2",
    "2-1",
    "1-2",
    "2-2",
    "3-1",
    "2-1",
    "Iran - Spain",
    "Iran - Portugal",
    "Iran - Morocco",
    "Spain - Portugal",
    "Spain - Morocco",
    "Portugal - Morocco",
]

score_board = DFScoreBoard(lambda: str(data.pop()))


def test_get_other_side():
    game = {"A": "1", "B": "1"}
    country = "A"
    assert score_board.get_other_side(game, country) == "B"


scores = pd.DataFrame(
    data=[[0, 0, 0, 0, 0]], columns=["wins", "loses", "draws", "goal_difference", "points"], index=["A"]
)
expected = [
    ([{"A": "1", "B": "1"}, scores, "B"], [0, 0, 1, 0, 1]),
    ([{"A": "2", "C": "1"}, scores, "C"], [1, 0, 1, 1, 4]),
    ([{"A": "1", "D": "3"}, scores, "D"], [1, 1, 1, -1, 4]),
]


@pytest.mark.parametrize("game_data, expected", expected)
def test_update_scores(game_data, expected):

    scores = score_board.update_country_scores(game_data[1], game_data[0], "A", game_data[2])

    assert scores.at["A", "wins"] == expected[0]
    assert scores.at["A", "loses"] == expected[1]
    assert scores.at["A", "draws"] == expected[2]
    assert scores.at["A", "goal_difference"] == expected[3]
    assert scores.at["A", "points"] == expected[4]


def test_score_board_dataframe_main():

    score_board.main()
    assert score_board.__repr__() == (
        "Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5\n"
        "Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3\n"
    )
