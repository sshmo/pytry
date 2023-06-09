"""World Cup score board dataframe."""
from typing import Any, Dict, List, Optional, Set

import pandas as pd

from pytry.general.world_cup_base import BaseScoreBoard


class DFScoreBoard(BaseScoreBoard):
    """DFScoreBoard.

    Attributes:
        input_count: number of games.
        games: List of games. like [{"A": "1", "B": "1"}, {"A": 1, "C": "3"}].
        keys: Set of countries. like {"A", "B", "C"}.
        key_stats: data structure for saving wins, loses, draws, goal_difference, points, count for each country.
    """

    def __init__(self, input_func: Any, default_count: Optional[int] = None) -> None:
        """Given input_func; Inits key_stats.

        Args:
            input_func: A function for generating input data.
            default_count: default number of keys if input_count is not specified.
        """
        super().__init__(input_func, default_count)
        self.input_count: int
        initial_data = []
        index_labels = []
        for country in self.keys:
            index_labels.append(country)
            initial_data.append([0, 0, 0, 0, 0, 0])
        self.key_stats = pd.DataFrame(
            initial_data, columns=["wins", "loses", "draws", "goal_difference", "points", "count"], index=index_labels
        )
        self.games: List[Dict[str, str]]
        self.keys: Set[str]
        self.key_stats: pd.DataFrame

    @staticmethod
    def get_row(key_stats: pd.DataFrame, key: str):
        """Get row."""
        return key_stats.loc[key]

    def __repr__(self) -> str:
        """Given scores dataframe; create score board representation for all countries."""
        score_board_data: pd.DataFrame = self.key_stats
        score_board_data = score_board_data.sort_index().sort_values(by=["points"], ascending=False)
        score_board_result = ""
        for country, row in score_board_data.iterrows():
            score_board_result = self.fill_score_board(score_board_result, country, row)

        return score_board_result


if __name__ == "__main__":  # pragma: no cover
    score_board = DFScoreBoard(input)
    score_board.main()
    print(score_board)
