"""Max primes.

The max number that has the highest number of prime factors.

    Write a program that:

    reads 10 numbers from the input.
    prints the number that has the highest number of prime factors
    along with the number of its prime factors in the output.
    If there are several numbers in this state, print the largest one.

    Input:
    123
    43
    54
    12
    76
    84
    98
    678
    543
    231

    Output:
    678 3
"""

from typing import Any, Dict, List, Optional

from pytry.general.base import Base


class MaxPrime(Base):
    """MaxPrime.

    Attributes:
        input_count: number of input integers.
        key_data: a list of integers.
        key_stats: key value count of prime factors for each number.
    """

    def __init__(self, input_func: Any) -> None:
        """Given random number of input strings; Inits MaxPrime attributes.

        Args:
            input_func: a function for generating input numbers.
        """
        super().__init__(input_func)
        self.input_count: int = 10

        self.key_data: List[int] = self._get_key_data(input_func, self.input_count)
        self.key_stats: Dict[int, int] = {}
        for key in self.key_data:
            self.key_stats[key] = 0

    @staticmethod
    def _get_key_data(input_func: Any, input_count: int) -> List[int]:
        key_data = []
        while True:
            num_input: str = input_func()
            num: Optional[int] = int(num_input) if num_input.isdigit() else None
            if num:
                key_data.append(num)
            else:
                print("Not a number!")
            if len(key_data) == input_count:
                break
        return key_data

    def __repr__(self) -> str:
        """Return max count of prime factors for the max number."""
        max_value = max(self.key_stats.values())
        keys = [key for key, value in self.key_stats.items() if value == max_value]
        max_number = max(keys)
        return f"{max_number} {max_value}"

    @staticmethod
    def is_prime(num: int) -> bool:
        """Check if number is prime.

        Args:
            num: an integer.

        Returns:
            true if prime else false.
        """
        return all(num % x != 0 for x in range(2, int(num**0.5) + 1)) if num > 1 else False

    def get_prime_list(self, nums: List[int]) -> List[int]:
        """Given numbers list, returns all prime numbers lower than max number.

        Args:
            nums: all input numbers.

        Returns:
            all prime numbers lower than max number.
        """
        max_num = max(nums) + 1
        primes = []
        for i in range(2, max_num):
            if self.is_prime(i):
                primes.append(i)
        return primes

    def update_stats(self, key_stats, key) -> Dict[int, int]:
        """Update count of of prime factors for a number."""
        key_stats[key] += 1
        return key_stats

    def main(self) -> None:
        """Given numbers; calculate count of prime factors for all numbers."""
        numbers = self.key_data
        prime_list = self.get_prime_list(numbers)
        for number in numbers:
            for prime in prime_list:
                if number % prime == 0:
                    self.key_stats = self.update_stats(self.key_stats, number)


if __name__ == "__main__":  # pragma: no cover
    max_prime = MaxPrime(input)
    max_prime.main()
    print(max_prime)
