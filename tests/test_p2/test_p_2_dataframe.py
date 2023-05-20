import pandas as pd

from pytry.p_2.p_2_dataframe import DFScoreBoard

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


def test_update_scores():
    scores = pd.DataFrame(
        data=[[0, 0, 0, 0, 0]], columns=["wins", "loses", "draws", "goal_difference", "points"], index=["A"]
    )

    game = {"A": "1", "B": "1"}
    scores = score_board.update_country_scores(scores, game, "A", "B")

    assert scores.at["A", "draws"] == 1
    assert scores.at["A", "points"] == 1
    assert scores.at["A", "goal_difference"] == 0

    game = {"A": "2", "C": "1"}
    scores = score_board.update_country_scores(scores, game, "A", "C")
    assert scores.at["A", "wins"] == 1
    assert scores.at["A", "points"] == 4
    assert scores.at["A", "goal_difference"] == 1

    game = {"A": "1", "D": "3"}
    scores = score_board.update_country_scores(scores, game, "A", "D")
    assert scores.at["A", "loses"] == 1
    assert scores.at["A", "points"] == 4
    assert scores.at["A", "goal_difference"] == -1


def test_score_board_dataframe_main():

    score_board.main()
    assert score_board.__repr__() == (
        "Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5\n"
        "Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3\n"
    )
