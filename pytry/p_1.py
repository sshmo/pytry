"""
Write a program that:

    reads 10 numbers from the input.
    prints the number that has the highest number of divisors of the prime number \
    along with the number of its prime divisors in the output.
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


def main():  # pragma: no cover
    """reads 10 numbers from the input and prints the numbers"""

    numbers = get_nums(input)
    print(numbers)


if __name__ == "__main__":  # pragma: no cover
    main()
