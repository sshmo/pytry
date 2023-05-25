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


class FavoriteGeneres:
    """
    FavoriteGeneres.

    Attributes:
        generes: List of generes.
        number_of_people: number of people.
        genere_board: genere_board data structure.
    """

    def __init__(self, input_func: Any) -> None:
        """
        Given the number of people; Inits number_of_people, favorite_gen and genere_board.

        Args:
            input_func: a function for generating input numbers.
        """
        self.generes = set()
        self.number_of_people = self._get_number_of_people(input_func)
        self.favorite_gen = self._get_favorite_gen(input_func, self.number_of_people)
        for _, value in self.favorite_gen.items():
            self.generes.update(set(value))

        self.genere_board = {}
        for genere in self.generes:
            self.genere_board[genere] = {
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
    def _get_favorite_gen(input_func: Any, number_of_people: int) -> Dict[str, List[str]]:
        favorite_gen = {}
        while True:
            data: str = input_func()
            datal_list = data.split(" ")
            name = datal_list[0]
            favorite_gen[name] = datal_list[1:]
            if len(favorite_gen) == number_of_people:
                break
        return favorite_gen

    def __repr__(self) -> str:
        """Given genere_board; create genere_board representation for all generes."""
        genere_board_data: Dict = self.genere_board
        soretd_generes = sorted(
            genere_board_data, key=lambda x: (-genere_board_data[x]["count"], genere_board_data[x]["genere"])
        )
        result = ""
        for genere in soretd_generes:
            result += f"{genere} : {self.genere_board[genere]['count']}\n"

        return result

    def main(self):
        """Given data from the input; create genere board representation for all generes."""
        for genere in self.generes:
            for _, list_value in self.favorite_gen.items():
                for value in list_value:
                    if genere == value:
                        self.genere_board[genere]["count"] += 1


if __name__ == "__main__":  # pragma: no cover
    favorite_genres = FavoriteGeneres(input)
    favorite_genres.main()
    print(favorite_genres)
