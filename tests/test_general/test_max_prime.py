import random
from string import ascii_letters

import pytest

from pytry.general.max_prime import MaxPrime


def mock_input():
    return str(random.choice([random.choice(ascii_letters), random.randint(1, 1000)]))


max_prime = MaxPrime(mock_input, 10)


def test_invalid_default():
    with pytest.raises(ValueError) as excinfo:
        MaxPrime(mock_input, -1)
    assert str(excinfo.value) == "Invalid value for default count: -1"


def test_get_nums():
    nums = max_prime.key_data
    assert len(nums) == 10
    for num in nums:
        assert isinstance(num, int)


def test_get_prime_list():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    prime_list = max_prime.get_prime_list([1, 2, 32])
    assert len(prime_list) == len(primes)
    assert 1 not in prime_list
    assert all([False for x in primes if x not in prime_list])


def test_get_prime_count():

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    max_prime = MaxPrime(lambda: str(data.pop()), 10)
    factor_num_dict = {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1, 8: 1, 9: 1, 10: 2}
    max_prime.main()
    assert len(max_prime.key_stats) == len(factor_num_dict)
    assert all([factor_num_dict[key] == value for key, value in max_prime.key_stats.items()])


def test_max_prime_main():

    data = [123, 43, 54, 12, 76, 84, 98, 678, 543, 231]
    max_prime = MaxPrime(lambda: str(data.pop()), 10)
    max_prime.main()
    assert max_prime.__repr__() == "678 3"


def test_max_prime_big_number_main():

    data = [123, 43, 54, 12, 76, 84, 98, 678, 543, 231, 123451]
    max_prime = MaxPrime(lambda: str(data.pop()), 10)
    max_prime.main()
    assert max_prime.__repr__() == "678 3"
