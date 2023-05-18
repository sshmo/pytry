"""World Cup score board dataframe implementation."""

import pandas as pd

from pytry.p_2.p_2_base import BaseScoreBoard


class DFScoreBoard(BaseScoreBoard):
    """DFScoreBoard."""

    def __init__(self, input_func) -> None:
        """Given input_func; returns games, countries, initial_score_board."""
        super().__init__(input_func)
        initial_data = []
        index_labels = []
        for country in self.countries:
            index_labels.append(country)
            initial_data.append([0, 0, 0, 0, 0])
        self.score_board = pd.DataFrame(
            initial_data, columns=["wins", "loses", "draws", "goal_difference", "points"], index=index_labels
        )

    @staticmethod
    def get_row(scores: pd.DataFrame, country: str):
        """Get row."""
        return scores.loc[country]

    def create_score_board_result(self, score_board_data: pd.DataFrame) -> str:
        """Given scores dataframe; create score board for all countries."""
        score_board_data = score_board_data.sort_index().sort_values(by=["points"], ascending=False)
        score_board_result = ""
        for country, row in score_board_data.iterrows():
            score_board_result = self.fill_score_board(score_board_result, country, row)

        return score_board_result


if __name__ == "__main__":  # pragma: no cover
    score_board = DFScoreBoard(input)
    print(score_board.main())
