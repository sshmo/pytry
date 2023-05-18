"""World Cup score board dictionary implementation."""

from typing import Any, Dict

from pytry.p_2.p_2_base import BaseScoreBoard


class DictScoreBoard(BaseScoreBoard):
    """DictScoreBoard."""

    def __init__(self, input_func: Any) -> None:
        """Given input_func; returns games, countries, initial_score_board."""
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

    def create_score_board_result(self, score_board_data: Dict[str, Dict]) -> str:
        """Given scores dictionary; create score board for all countries."""
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
    print(score_board.main())
