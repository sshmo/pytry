"""
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

from math import floor
from typing import List


def get_nums(input_func):
    """reads 10 numbers from the input and returns list of them"""
    nums = []
    while True:
        num = input_func()
        num = int(num) if num.isdigit() else None
        _ = nums.append(num) if num else print("Not a number!")
        if len(nums) == 10:
            break
    return nums


def has_prime_factor(number: int, primes: list):
    """given prime list, checks if number has prime factors"""

    for prime in primes:
        if number > prime and number % prime == 0:
            return True
    return False


def get_prime_list(nums: List):
    "given numbers list, returns max prime factors list"

    max_num = floor(max(nums) ** 0.5) + 1
    primes = []
    for i in range(2, max_num):
        if not has_prime_factor(i, primes):
            primes.append(i)
    return primes


def main():  # pragma: no cover
    """reads 10 numbers from the input and prints the numbers"""

    numbers = get_nums(input)
    prime_list = get_prime_list(numbers)
    print(prime_list)
    print(numbers)


if __name__ == "__main__":  # pragma: no cover
    main()
