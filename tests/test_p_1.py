import random
from string import ascii_letters

from pytry.p_1 import get_nums, get_prime_list, has_prime_factor


def mock_input():
    return str(random.choice([random.choice(ascii_letters), random.randint(1, 1000)]))


def test_get_nums():
    nums = get_nums(mock_input)
    assert len(nums) == 10
    for num in nums:
        assert isinstance(num, int)


def test_has_prime_factor():
    assert not (has_prime_factor(2, [2]))
    assert has_prime_factor(4, [2])


def test_get_prime_list():
    primes = [2, 3, 5]
    prime_list = get_prime_list([1, 2, 48])
    assert len(prime_list) == len(primes)
    for num in prime_list:
        assert num in primes
    for num in primes:
        assert num in prime_list
