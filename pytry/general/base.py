"""Base implementation."""

from abc import ABC, abstractmethod
from typing import Any, Optional, Set


class Base(ABC):
    """Base.

    Attributes:
        input_count: number of entry data.
        keys: set of keys for which we calculate and represent statistics.
        key_data: data structure for saving key data.
        key_stats: data structure for calculating key statistics.
    """

    @abstractmethod
    def __init__(self, input_func: Any, default_count: Optional[int]) -> None:
        """Given input_func; Inits Base attributes.

        Args:
            input_func: A function for generating input data.
            default_count: default number of keys if input_count is not specified.
        """
        if isinstance(default_count, int) and default_count < 0:
            raise ValueError(f"Invalid value for default count: {default_count}")
        self.input_count: int = default_count if default_count is not None else self.get_input_count(input_func)
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
            if input_count and input_count > 0:
                break
            print("Invalid number!")
        return input_count

    def __repr__(self) -> str:  # pragma: no cover
        """Given key_stats; create key_stats representation for all keys."""
        return ""

    @abstractmethod
    def update_stats(self, key_stats, key) -> Any:
        """Update stats of a key for a single row.

        Returns:
            updated stats for each key
        """

    @abstractmethod
    def main(self) -> None:
        """Given key_data from the input; calculates key_stats."""
