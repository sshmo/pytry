"""
Favorite genres.

In a survey, moviegoers were asked to list 3 of their favorite genres.
They are given 6 different genres to choose from, including:

Horror, Romance, Comedy, History, Adventure, Action.

Write a program that takes the number of people,
then takes the name of each person with their favorite genres
and prints the name of each genre and the number of people interested in that genre
in the order of the most interested in the output.
(If the level of interest in different genres is the same,
print in the order of the English alphabet in the output.)
If no genre is selected, consider its value as zero and print the name and number 0 in the output.

Input:
4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

Output:
Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1
"""

from typing import Any, Dict, List

from pytry.general.base import Base


class FavoriteGeneres(Base):
    """
    FavoriteGeneres.

    Attributes:
        input_count: int : number of genere row data.
        keys: Set[str] set of generes for which we calculate and represent statistics.
        key_data: data structure for saving genere data.
        key_stats : Any : data structure for saving genere statistics.
    """

    def __init__(self, input_func: Any) -> None:
        """
        Given the number of people; Inits FavoriteGeneres attributes.

        Args:
            input_func: a function for generating input numbers.
        """
        super().__init__(input_func)
        self.keys = set()
        self.input_count = self._get_number_of_people(input_func)
        self.key_data = self._get_key_data(input_func, self.input_count)
        for _, value in self.key_data.items():
            self.keys.update(set(value))

        self.key_stats = {}
        for genere in self.keys:
            self.key_stats[genere] = {
                "genere": genere,
                "count": 0,
            }

    @staticmethod
    def _get_number_of_people(input_func: Any) -> int:
        while True:
            num: str = input_func()
            number_of_people = int(num) if num.isdigit() else None
            if number_of_people:
                break
            print("Not a number!")
        return number_of_people

    @staticmethod
    def _get_key_data(input_func: Any, input_count: int) -> Dict[str, List[str]]:
        key_data = {}
        while True:
            data: str = input_func()
            datal_list = data.split(" ")
            name = datal_list[0]
            key_data[name] = datal_list[1:]
            if len(key_data) == input_count:
                break
        return key_data

    @staticmethod
    def fill_board(key_repr, key, row):
        """Fill genere stats data row by row."""
        key_repr += f"{key} : {row['count']}\n"
        return key_repr

    def __repr__(self) -> str:
        """Given genere_board; create genere stat representation for all generes."""
        genere_board_data: Dict = self.key_stats
        soretd_generes = sorted(
            genere_board_data, key=lambda x: (-genere_board_data[x]["count"], genere_board_data[x]["genere"])
        )
        result = ""
        for genere in soretd_generes:
            row = genere_board_data[genere]
            result = self.fill_board(result, genere, row)

        return result

    def update_stats(self, key_stats, key):
        """Update stats of a genere for a single row."""
        key_stats[key]["count"] += 1
        return key_stats

    def main(self):
        """Given genere data from the input; calculate genere stats for all generes."""
        for genere in self.keys:
            for _, list_value in self.key_data.items():
                for value in list_value:
                    if genere == value:
                        self.key_stats = self.update_stats(self.key_stats, genere)


if __name__ == "__main__":  # pragma: no cover
    favorite_genres = FavoriteGeneres(input)
    favorite_genres.main()
    print(favorite_genres)
