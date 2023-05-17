"""
World Cup score board.

Iran, Portugal, Spain and Morocco are present in Group B of the World Cup.
Write a program that, upon receiving the results of the games,
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

from typing import Any, Dict, List, Set, Tuple


class ScoreBoard:
    """ScoreBoard."""

    @staticmethod
    def get_data(input_func: Any) -> Tuple[List[Dict], Set[str]]:
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

        for _ in range(0, 6):
            raw_country_pair: str = input_func()
            country_pair = raw_country_pair.split(" - ")
            country_pairs.append(country_pair)

        for _ in range(0, 6):
            raw_scores: str = input_func()
            scores.append(raw_scores.split("-"))

        for i in range(0, 6):
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
    def update_scores(scores: Dict[str, Dict], game: Dict[str, str], country: str, other_side: str) -> Dict[str, Dict]:
        """
        Update scores of a country for a single game.

        Args:
            scores: a dictionary of score board results for each country.
            game: a dictionary like {"A": 1, "B": 1}.
            country: the country which the scores are calculated for like "A".
            other_side: the the other country like "B".

        Returns:
            the the other country like "B"
        """
        goal_difference = int(game[country]) - int(game[other_side])
        scores[country]["goal_difference"] += goal_difference
        if goal_difference == 0:
            scores[country]["draws"] += 1
            scores[country]["points"] += 1
        elif goal_difference > 0:
            scores[country]["wins"] += 1
            scores[country]["points"] += 3
        elif goal_difference < 0:
            scores[country]["loses"] += 1

        return scores

    def create_score_board_data(self, games: List[Dict[str, str]], countries: Set[str]) -> Dict[str, Dict]:
        """Given games and countries; calculate scores for all countries."""
        scores = {}
        for country in countries:
            scores[country] = {"country": country, "wins": 0, "loses": 0, "draws": 0, "goal_difference": 0, "points": 0}

            for game in games:
                if country in game:
                    other_side = self.get_other_side(game, country)
                    scores = self.update_scores(scores, game, country, other_side)

        return scores

    @staticmethod
    def create_score_board_result(soretd_countries: List, scores: Dict[str, Dict]) -> str:
        """Given scores; create score board for all countries."""
        score_board_result = ""
        for country in soretd_countries:
            score_board_result += (
                f"{country}  "
                f"wins:{scores[country]['wins']} , "
                f"loses:{scores[country]['loses']} , "
                f"draws:{scores[country]['draws']} , "
                f"goal difference:{scores[country]['goal_difference']} , "
                f"points:{scores[country]['points']}\n"
            )

        return score_board_result

    def main(self, input_func: Any) -> str:
        """Given data from the input; prints score board result."""
        games, countries = self.get_data(input_func)
        scores = self.create_score_board_data(games, countries)
        soretd_countries = sorted(scores, key=lambda x: (-scores[x]["points"], scores[x]["country"]))
        score_board_result = self.create_score_board_result(soretd_countries, scores)

        return score_board_result


score_board = ScoreBoard()

if __name__ == "__main__":  # pragma: no cover
    print(score_board.main(input))
