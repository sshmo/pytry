"""base implementation."""

from abc import ABC, abstractmethod
from typing import Any, Set


class Base(ABC):
    """
    Base.

    Attributes:
        input_count: int : number of key row data.
        keys: Set[str] set of keys for which we calculate and represent statistics.
        key_data: data structure for saving key data.
        key_stats : Any : data structure for calculating key statistics.
    """

    @abstractmethod
    def __init__(self, input_func: Any) -> None:
        """
        Given input_func; Inits Base attributes.

        Args:
            input_func: A function for generating input data.
        """
        self.input_count: int
        self.keys: Set[str]
        self.key_stats: Any
        self.key_data: Any

    @staticmethod
    @abstractmethod
    def _get_key_data(input_func: Any, input_count: int):
        """get_key_data."""

    @staticmethod
    def get_input_count(input_func: Any) -> int:
        """get_input_count."""
        while True:
            num: str = input_func()
            input_count = int(num) if num.isdigit() else None
            if input_count:
                break
            print("Not a number!")
        return input_count

    def __repr__(self) -> str:  # pragma: no cover
        """Given key_stats; create key_stats representation for all keys."""
        return ""

    @abstractmethod
    def update_stats(self, key_stats, key):
        """
        Update stats of a key for a single row.

        Returns:
            updated stats for each key
        """

    @abstractmethod
    def main(self):
        """Given key_data from the input; calculates key_stats."""
