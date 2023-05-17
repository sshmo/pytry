"""World Cup score board base implementation."""

import re
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Set, Tuple


class BaseScoreBoard(ABC):
    """BaseScoreBoard."""

    @staticmethod
    def get_data(input_func: Any, game_count: int = 6) -> Tuple[List[Dict], Set[str]]:
        """
        Given input strings; returns games.

        Args:
            input_func: A function for generating input data.

        Returns:
            List of games. like [{"A": 1, "B": 1}, {"A": 1, "C": 3}].
            Set of countries. like {"A", "B", "C"}.
        """
        games = []
        country_pairs = []
        countries = set()
        scores = []

        while True:
            raw_country_pair: str = input_func()
            if re.match(r"\w+\s-\s\w+", raw_country_pair):
                country_pair = raw_country_pair.split(" - ")
                country_pairs.append(country_pair)
            if len(country_pairs) == game_count:
                break

        while True:
            raw_scores: str = input_func()
            if re.match(r"\d+-\d+", raw_scores):
                scores.append(raw_scores.split("-"))
            if len(scores) == game_count:
                break

        for i in range(0, game_count):
            games.append({country_pairs[i][0]: scores[i][0], country_pairs[i][1]: scores[i][1]})
            countries.add(country_pairs[i][0])
            countries.add(country_pairs[i][1])

        return games, countries

    @staticmethod
    def get_other_side(game: Dict[str, str], country: str) -> str:
        """
        Get other side in a game.

        Args:
            game: a dictionary like {"A": 1, "B": 1}.
            country: the country which the scores are calculated for like "A".

        Returns:
            the the other country like "B"
        """
        game_sides: List = list(game.keys())
        game_sides.remove(country)
        other_side = game_sides[0]
        return other_side

    @staticmethod
    @abstractmethod
    def initialize_score_board_data(countries):
        """Given games and countries; initialize scores for all countries."""

    @staticmethod
    @abstractmethod
    def get_row(scores, country: str):  # pragma: no cover
        """Get row."""
        return {}

    def update_country_scores(self, scores, game: Dict[str, str], country: str, other_side: str):
        """
        Update scores of a country for a single game.

        Args:
            scores: score board data structure for each country.
            game: a dictionary like {"A": 1, "B": 1}.
            country: the country which the scores are calculated for like "A".
            other_side: the other country like "B".

        Returns:
            updated scores for each country
        """
        row = self.get_row(scores, country)

        goal_difference = int(game[country]) - int(game[other_side])
        row["goal_difference"] += goal_difference
        if goal_difference == 0:
            row["draws"] += 1
            row["points"] += 1
        elif goal_difference > 0:
            row["wins"] += 1
            row["points"] += 3
        elif goal_difference < 0:
            row["loses"] += 1

        return scores

    def create_score_board_data(self, scores, games, countries):
        """Given games and countries; calculate scores for all countries."""
        for country in countries:
            for game in games:
                if country in game:
                    other_side = self.get_other_side(game, country)
                    scores = self.update_country_scores(scores, game, country, other_side)

        return scores

    @staticmethod
    def fill_score_board(score_board_result, country, row):
        """fill_score_board data."""
        score_board_result += (
            f"{country}  "
            f"wins:{row['wins']} , "
            f"loses:{row['loses']} , "
            f"draws:{row['draws']} , "
            f"goal difference:{row['goal_difference']} , "
            f"points:{row['points']}\n"
        )
        return score_board_result

    @abstractmethod
    def create_score_board_result(self, score_board_data):
        """Given scores; create score board for all countries."""

    def main(self, input_func: Any):
        """Given data from the input; prints score board result."""
        games, countries = self.get_data(input_func)
        initial_scores = self.initialize_score_board_data(countries)
        score_board_data = self.create_score_board_data(initial_scores, games, countries)
        score_board_result = self.create_score_board_result(score_board_data)

        return score_board_result
