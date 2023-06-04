"""World Cup score board base.

Iran, Portugal, Spain and Morocco are present in Group B of the World Cup.

    Write a program that:

    upon receiving the results of the games,
    will print the team name, the number of wins and losses,
    and the difference in goals and points respectively in one line.
    Each team should be printed in order of points in one line.
    (If the points are equal, the number of wins will be considered.
    If both the number of wins and the points are equal,
    they will be printed in alphabetical order.)

    Note: The team gets zero points in case of loss,
    one point in case of draw and three points in case of win.
    Goal difference is the difference between goals scored and goals conceded by a team.

    Read the results of the games in the following order:
    (in the sample entry, the left number corresponds to the right team.)

    Input:
    Iran - Spain
    Iran - Portugal
    Iran - Morocco
    Spain - Portugal
    Spain - Morocco
    Portugal - Morocco
    2-2
    2-1
    1-2
    2-2
    3-1
    2-1

    Output:
    Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
    Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
    Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
    Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""

import re
from abc import abstractmethod
from typing import Any, Dict, List, Optional, Set

from pytry.general.base import Base


class BaseScoreBoard(Base):
    """BaseScoreBoard.

    Attributes:
        input_count: number of games.
        games: List of games. like [{"A": "1", "B": "1"}, {"A": "1", "C": "3"}].
        keys: Set of countries. like {"A", "B", "C"}.
        key_stats: data structure for saving wins, loses, draws, goal_difference, points, count for each country.
    """

    @abstractmethod
    def __init__(self, input_func: Any, default_count: Optional[int] = None) -> None:
        """Given input_func; Inits games, BaseScoreBoard attributes.

        Args:
            input_func: A function for generating input data.
            default_count: default number of keys if input_count is not specified.
        """
        super().__init__(input_func, default_count)
        self.input_count: int
        games = []
        countries = set()
        country_pairs = self._get_country_pairs(input_func, self.input_count)
        scores = self._get_key_data(input_func, self.input_count)

        for i in range(0, self.input_count):
            games.append({country_pairs[i][0]: scores[i][0], country_pairs[i][1]: scores[i][1]})
            countries.add(country_pairs[i][0])
            countries.add(country_pairs[i][1])

        self.games: List[Dict[str, str]] = games
        self.keys: Set[str] = countries
        self.key_stats: Any

    @staticmethod
    def _get_country_pairs(input_func: Any, input_count: int) -> List[List[str]]:
        country_pairs = []
        while True:
            raw_country_pair: str = input_func()
            if re.match(r"\w+\s-\s\w+", raw_country_pair):
                country_pair = raw_country_pair.split(" - ")
                country_pairs.append(country_pair)
            if len(country_pairs) == input_count:
                break
        return country_pairs

    @staticmethod
    def _get_key_data(input_func: Any, input_count: int):
        scores = []
        while True:
            raw_scores: str = input_func()
            if re.match(r"\d+-\d+", raw_scores):
                scores.append(raw_scores.split("-"))
            if len(scores) == input_count:
                break
        return scores

    @staticmethod
    @abstractmethod
    def get_row(key_stats, key: str):  # pragma: no cover
        """Get row."""
        return {}

    @staticmethod
    def get_other_side(game: Dict[str, str], country: str) -> str:
        """Get other side in a game.

        Args:
            game: a dictionary like {"A": "1", "B": "1"}.
            country: the country which the scores are calculated for like "A".

        Returns:
            the the other country like "B"
        """
        game_sides: List = list(game.keys())
        game_sides.remove(country)
        other_side = game_sides[0]
        return other_side

    @staticmethod
    def _update_game_stats(row, goal_difference):
        if goal_difference == 0:
            row["draws"] += 1
            row["points"] += 1
        elif goal_difference > 0:
            row["wins"] += 1
            row["points"] += 3
        elif goal_difference < 0:
            row["loses"] += 1
        return row

    def update_game(self, row: Dict, key: str, game: Dict, other_side: str) -> Dict:
        """Update stats of a country for a single game.

        Args:
            row: data structure for each country.
            game: a dictionary like {"A": "1", "B": "1"}.
            key: the country which the scores are calculated for like "A".
            other_side: the other country like "B".

        Returns:
            updated stats for the country row
        """
        if game and other_side:
            goal_difference = int(game[key]) - int(game[other_side])
            row["goal_difference"] += goal_difference
            row = self._update_game_stats(row, goal_difference)

        return row

    def update_stats(self, key_stats: Any, key: str, game=None, other_side: str = "") -> Any:
        """Update key_stats for a single game.

        Args:
            key_stats: score board data structure for each country.
            game: a dictionary like {"A": "1", "B": "1"}.
            key: the country which the scores are calculated for like "A".
            other_side: the other country like "B".

        Returns:
            updated scores for each country
        """
        row = self.get_row(key_stats, key)
        row["count"] += 1
        row = self.update_game(row, key, game, other_side)

        return key_stats

    @staticmethod
    def fill_score_board(score_board_result, country, row):
        """Fill score board data row by row."""
        score_board_result += (
            f"{country}  "
            f"wins:{row['wins']} , "
            f"loses:{row['loses']} , "
            f"draws:{row['draws']} , "
            f"goal difference:{row['goal_difference']} , "
            f"points:{row['points']}\n"
        )
        return score_board_result

    def main(self) -> None:
        """Given data from the input; calculates score board."""
        score_board, games, countries = self.key_stats, self.games, self.keys
        for country in countries:
            for game in games:
                if country in game:
                    other_side = self.get_other_side(game, country)
                    score_board = self.update_stats(score_board, country, game, other_side)
        self.key_stats = score_board
