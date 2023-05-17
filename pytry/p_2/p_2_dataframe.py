"""World Cup score board dataframe implementation."""

from typing import Set

import pandas as pd

from pytry.p_2.p_2_base import BaseScoreBoard


class DFScoreBoard(BaseScoreBoard):
    """DFScoreBoard."""

    @staticmethod
    def get_row(scores: pd.DataFrame, country: str):
        """Get row."""
        return scores.loc[country]

    @staticmethod
    def initialize_score_board_data(countries: Set[str]) -> pd.DataFrame:
        """Given games and countries; initialize scores for all countries."""
        initial_data = []
        index_labels = []
        for country in countries:
            index_labels.append(country)
            initial_data.append([0, 0, 0, 0, 0])
        scores = pd.DataFrame(
            initial_data, columns=["wins", "loses", "draws", "goal_difference", "points"], index=index_labels
        )
        return scores

    def create_score_board_result(self, score_board_data: pd.DataFrame) -> str:
        """Given scores dataframe; create score board for all countries."""
        score_board_data = score_board_data.sort_index().sort_values(by=["points"], ascending=False)
        score_board_result = ""
        for country, row in score_board_data.iterrows():
            score_board_result = self.fill_score_board(score_board_result, country, row)

        return score_board_result


score_board = DFScoreBoard()

if __name__ == "__main__":  # pragma: no cover
    print(score_board.main(input))
