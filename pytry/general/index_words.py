"""Index words.

Words that start with capital letters.

    Write a program that:

    prints index words (words that start with capital letters)
    along with the word number (nth word) from a text.
    If a word with this feature is not found in the text, it will print "None" in the output.
    You should not consider the words at the beginning of the sentence as index words.
    (number the words start from one.)

    Numbers are not counted.
    The only sign used in the sentence is the comma.
    Be sure to remove the dot or comma at the end of the word.

    Input:
    The Persian League is the largest sport event dedicated to the deprived areas of Iran.
    The Persian League promotes peace and friendship.
    This video was captured by one of our heroes who wishes peace.

    Output:
    2:Persian
    3:League
    15:Iran
    17:Persian
    18:League
"""
from typing import Any, Dict, List, Optional

from pytry.general.base import Base


class IndexWords(Base):
    """IndexWords.

    Attributes:
        input_count: number of entry data.
        key_data: input text corpus.
        key_stats:  data structure for saving index word position in the text corpus.
    """

    def __init__(self, input_func: Any, default_count: Optional[int] = None) -> None:
        """Given the number of people; Inits IndexWords attributes.

        Args:
            input_func: a function for generating input numbers.
            default_count: default number of keys if input_count is not specified.
        """
        super().__init__(input_func, default_count)
        self.input_count: int
        self.key_data: str = input_func()
        self.key_stats: Dict[int, str]

    @staticmethod
    def _get_key_data(input_func: Any, input_count: int):
        """Not Implemented."""

    def update_stats(self, key_stats, key):
        """Not Implemented."""

    def __repr__(self) -> str:
        """Given key_stats; create index word representation."""
        if not self.key_stats:
            return "None"
        word_repr = ""
        sorted_rsult = sorted(self.key_stats)
        for ind in sorted_rsult:
            word_repr += f"{ind}:{self.key_stats[ind]}\n"
        return word_repr

    @staticmethod
    def _isword(word: str) -> bool:
        return all((char.isascii() or char in ".,") for char in list(word))

    def _isvalidword(self, word: str) -> bool:
        if word and (word[0].isupper()) and self._isword(word):
            return True
        return False

    def _isvalid(self, i: int, word: str, words: List[str]) -> bool:
        if (i != 0) and not words[i - 1].endswith(".") and self._isvalidword(word):
            return True
        return False

    def main(self) -> None:
        """Given key_data; calculates index word stats."""
        words = self.key_data.split(" ")
        key_stats = {i + 1: word for i, word in enumerate(words) if self._isvalid(i, word, words)}
        self.key_stats = {k: v.replace(".", "").replace(",", "") for k, v in key_stats.items()}
