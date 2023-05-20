"""World Cup score board dictionary implementation."""

from typing import Any, Dict

from pytry.general.world_cup.base import BaseScoreBoard


class DictScoreBoard(BaseScoreBoard):
    """
    DictScoreBoard.

    Attributes:
        games: List of games. like [{"A": "1", "B": "1"}, {"A": "1", "C": "3"}].
        countries: Set of countries. like {"A", "B", "C"}.
        score_board: score_board data structure.
    """

    def __init__(self, input_func: Any) -> None:
        """
        Given input_func; Inits games, countries and score_board.

        Args:
            input_func: A function for generating input data.
        """
        super().__init__(input_func)
        self.score_board = {}
        for country in self.countries:
            self.score_board[country] = {
                "country": country,
                "wins": 0,
                "loses": 0,
                "draws": 0,
                "goal_difference": 0,
                "points": 0,
            }

    @staticmethod
    def get_row(scores: Dict[str, Dict], country: str):
        """Get row."""
        return scores[country]

    def __repr__(self) -> str:
        """Given scores dictionary; create score board representation for all countries."""
        score_board_data: Dict = self.score_board
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
