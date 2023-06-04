"""World Cup score board dictionary."""

from typing import Any, Dict, List, Set

from pytry.general.world_cup_base import BaseScoreBoard


class DictScoreBoard(BaseScoreBoard):
    """DictScoreBoard.

    Attributes:
        games: List of games. like [{"A": "1", "B": "1"}, {"A": "1", "C": "3"}].
        keys: Set of countries. like {"A", "B", "C"}.
        key_stats: data structure for saving wins, loses, draws, goal_difference, points, count for each country.
    """

    def __init__(self, input_func: Any, default_count: int = 0) -> None:
        """Given input_func; Inits key_stats.

        Args:
            input_func: A function for generating input data.
            default_count: default number of keys if input_count is not specified.
        """
        super().__init__(input_func, default_count)
        self.key_stats: Dict[str, Dict] = {}
        for country in self.keys:
            self.key_stats[country] = {
                "country": country,
                "wins": 0,
                "loses": 0,
                "draws": 0,
                "goal_difference": 0,
                "points": 0,
                "count": 0,
            }
        self.games: List[Dict[str, str]]
        self.keys: Set[str]

    @staticmethod
    def get_row(key_stats: Dict[str, Dict], key: str):
        """Get row."""
        return key_stats[key]

    def __repr__(self) -> str:
        """Given scores dictionary; create score board representation for all countries."""
        score_board_data: Dict = self.key_stats
        soretd_countries = sorted(
            score_board_data, key=lambda x: (-score_board_data[x]["points"], score_board_data[x]["country"])
        )
        score_board_result = ""
        for country in soretd_countries:
            row = score_board_data[country]
            score_board_result = self.fill_score_board(score_board_result, country, row)

        return score_board_result


if __name__ == "__main__":  # pragma: no cover
    score_board = DictScoreBoard(input)
    score_board.main()
    print(score_board)
