from typing import List

import pytest

from pytry.general.world_cup_dataframe import DFScoreBoard


@pytest.fixture(name="world_cup_dataframe_data")
def input_data() -> List:
    return [
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


def test_dataframe_get_other_side(world_cup_dataframe_data: List):
    score_board = DFScoreBoard(lambda: str(world_cup_dataframe_data.pop()), 6)
    game = {"A": "1", "B": "1"}
    country = "A"
    assert score_board.get_other_side(game, country) == "B"


row = {"wins": 0, "loses": 0, "draws": 0, "goal_difference": 0, "points": 0, "count": 0}
expected = [
    ({"game": {"A": "1", "B": "1"}, "row": row, "other_side": "B"}, [0, 0, 1, 0, 1]),
    ({"game": {"A": "2", "C": "1"}, "row": row, "other_side": "C"}, [1, 0, 1, 1, 4]),
    ({"game": {"A": "1", "D": "3"}, "row": row, "other_side": "D"}, [1, 1, 1, -1, 4]),
]


@pytest.mark.parametrize("game_data, expected", expected)
def test_dataframe_update_game(game_data, expected, world_cup_dataframe_data: List):

    score_board = DFScoreBoard(lambda: str(world_cup_dataframe_data.pop()), 6)
    row = score_board.update_game(game_data["row"], "A", game_data["game"], game_data["other_side"])

    assert row["wins"] == expected[0]
    assert row["loses"] == expected[1]
    assert row["draws"] == expected[2]
    assert row["goal_difference"] == expected[3]
    assert row["points"] == expected[4]


def test_score_board_dataframe_main(world_cup_dataframe_data: List):

    score_board = DFScoreBoard(lambda: str(world_cup_dataframe_data.pop()), 6)
    score_board.main()
    assert score_board.__repr__() == (
        "Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5\n"
        "Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4\n"
        "Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3\n"
    )
