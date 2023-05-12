"""
The max number that has the highest number of prime factors.

Write a program that:

    reads 10 numbers from the input.
    prints the number that has the highest number of prime factors \
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

from typing import Any, Dict, List


def get_nums(input_func: Any) -> List[int]:
    """
    Given random number of input strings; returns list of 10 integer numbers.

    Args:
        input_func: a function for generating input numbers.

    Returns:
        a list of integers.
    """
    nums = []
    while True:
        num = input_func()
        num = int(num) if num.isdigit() else None
        _ = nums.append(num) if num else print("Not a number!")
        if len(nums) == 10:
            break
    return nums


def has_prime_factor(number: int, primes: List[int]) -> bool:
    """
    Given prime list, checks if number has prime factors.

    Args:
        number: an integer to check for prime factor.
        primes: list of prime factors to check.

    Returns:
        is prime or not.
    """
    for prime in primes:
        if number > prime and number % prime == 0:
            return True
    return False


def get_prime_list(nums: List[int]) -> List[int]:
    """
    Given numbers list, returns all prime numbers lower than max number.

    Args:
        nums: all input numbers.

    Returns:
        all prime numbers lower than max number.
    """
    max_num = max(nums) + 1
    primes = []
    for i in range(2, max_num):
        if not has_prime_factor(i, primes):
            primes.append(i)
    return primes


def get_prime_count(nums: List, prime_list) -> Dict[int, int]:
    """
    Given numbers list, returns count of prime factors for each number.

    Args:
        nums: all input numbers.
        prime_list: all prime numbers lower than max number.

    Returns:
        count of prime factors for each number.
    """
    factor_num = {}
    for number in nums:
        factor_num[number] = 0
        for prime in prime_list:
            if number % prime == 0:
                factor_num[number] += 1
    return factor_num


def main(input_func: Any) -> str:
    """
    Given 10 numbers from the input; prints max count of prime factors for the max number.

    Args:
        input_func: a function for generating input numbers.

    Returns:
        max count of prime factors for the max number.
    """
    numbers = get_nums(input_func)
    prime_list = get_prime_list(numbers)
    factor_count = get_prime_count(numbers, prime_list)
    max_value = max(factor_count.values())
    keys = [key for key, value in factor_count.items() if value == max_value]
    return f"{max(keys)} {max_value}"


if __name__ == "__main__":  # pragma: no cover
    print(main(input))
