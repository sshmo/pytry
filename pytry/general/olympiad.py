"""Computer Olympiad list.

Ahmed is sending the final list of the names of those accepted
to the Computer Olympiad to the results review committee
so that the committee can print the entry cards for the final competitions,
but because a specific format was not defined for registering the names during the test,
the participants did not used standard names, besides,
the language with which they participated in the competition is written in the continuation of each name,
and the gender of the people is also specified at the beginning of each name.
The standard form of names is that the first letter of the name is uppercase
and the rest of the letters of the name are lowercase.

    Write a program that:

    reads the number, name, gender, and language of the accepted candidates
    from the input and separates the names based on their gender,
    standardizes them, and writes the language in front of each name with
    which they participated in the competition.
    (In the output, the female gender should be printed first and then the male gender.
    The names of each gender should be printed in the order of the English alphabet.)

    Input:
    4
    m.hosSein.python
    f.miNa.C
    m.aHMad.C++
    f.Sara.java

    Output:
    f Mina C
    f Sara java
    m Ahmad C++
    m Hossein python
"""

from typing import Any, Dict, List, Optional

from pytry.general.base import Base


class Olympiad(Base):
    """Olympiad.

    Attributes:
        input_count: int : number of entry people.
        key_data: data structure for saving people data.
    """

    def __init__(self, input_func: Any, default_count: Optional[int] = None) -> None:
        """Given the number of people; Inits Olympiad attributes.

        Args:
            input_func: a function for generating input numbers.
            default_count: default number of keys if input_count is not specified.
        """
        super().__init__(input_func, default_count)
        self.input_count: int
        self.key_data: Dict[str, Dict[str, str]] = self._get_key_data(input_func, self.input_count)

    @staticmethod
    def _get_key_data(input_func: Any, input_count: int) -> Dict[str, Dict[str, str]]:
        key_data: Dict[str, Dict[str, str]] = {}
        while input_count - len(key_data):
            data: str = input_func()
            data_list: List[str] = data.split(".")
            if data_list:
                program: str = data_list.pop()
                name: str = data_list.pop().capitalize()
                gender: str = data_list.pop()

            key_data[name] = {"name": name, "program": program, "gender": gender}
        return key_data

    @staticmethod
    def get_input_count(input_func: Any) -> int:
        """get_input_count."""
        return Base.get_input_count(input_func)

    def __repr__(self) -> str:
        """Given key_data; create standardized olympiad representation for all persons."""
        data_repr = ""
        data = self.key_data
        soretd_names = sorted(data, key=lambda x: (data[x]["gender"], data[x]["name"]))
        for name in soretd_names:
            data_repr += f'{data[name]["gender"]} {data[name]["name"]} {data[name]["program"]}\n'

        return data_repr.encode("utf-8", "replace").decode()

    def update_stats(self, key_stats, key):
        """Not Implemented."""

    def main(self) -> None:
        """Not Implemented."""


if __name__ == "__main__":  # pragma: no cover
    olympiad = Olympiad(input)
    print(olympiad)
