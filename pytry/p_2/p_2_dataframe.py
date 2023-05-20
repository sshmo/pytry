"""World Cup score board dataframe implementation."""

import pandas as pd

from pytry.p_2.p_2_base import BaseScoreBoard


class DFScoreBoard(BaseScoreBoard):
    """
    DFScoreBoard.

    Attributes:
        games: List of games. like [{"A": "1", "B": "1"}, {"A": 1, "C": "3"}].
        countries: Set of countries. like {"A", "B", "C"}.
        score_board: score_board data structure.
    """

    def __init__(self, input_func) -> None:
        """
        Given input_func; Inits games, countries and score_board.

        Args:
            input_func: A function for generating input data.
        """
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

    def __repr__(self) -> str:
        """Given scores dataframe; create score board representation for all countries."""
        score_board_data: pd.DataFrame = self.score_board
        score_board_data = score_board_data.sort_index().sort_values(by=["points"], ascending=False)
        score_board_result = ""
        for country, row in score_board_data.iterrows():
            score_board_result = self.fill_score_board(score_board_result, country, row)

        return score_board_result


if __name__ == "__main__":  # pragma: no cover
    score_board = DFScoreBoard(input)
    score_board.main()
    print(score_board)
