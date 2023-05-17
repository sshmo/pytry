"""World Cup score board dictionary implementation."""

from typing import Dict, Set

from pytry.p_2.p_2_base import BaseScoreBoard


class DictScoreBoard(BaseScoreBoard):
    """DictScoreBoard."""

    @staticmethod
    def get_row(scores: Dict[str, Dict], country: str):
        """Get row."""
        return scores[country]

    @staticmethod
    def initialize_score_board_data(countries: Set[str]) -> Dict[str, Dict]:
        """Given games and countries; initialize scores for all countries."""
        scores = {}
        for country in countries:
            scores[country] = {"country": country, "wins": 0, "loses": 0, "draws": 0, "goal_difference": 0, "points": 0}

        return scores

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


score_board = DictScoreBoard()

if __name__ == "__main__":  # pragma: no cover
    print(score_board.main(input))
