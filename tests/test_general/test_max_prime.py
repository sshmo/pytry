import random
from string import ascii_letters

from pytry.general.max_prime import MaxPrime


def mock_input():
    return str(random.choice([random.choice(ascii_letters), random.randint(1, 1000)]))


max_prime = MaxPrime(mock_input)


def test_get_nums():
    nums = max_prime.nums
    assert len(nums) == 10
    for num in nums:
        assert isinstance(num, int)


def test_get_prime_list():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    prime_list = max_prime.get_prime_list([1, 2, 32])
    assert len(prime_list) == len(primes)
    assert 1 not in prime_list
    for num in prime_list:
        assert num in primes
    for num in primes:
        assert num in prime_list


def test_get_prime_count():

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prime_list = [2, 3, 5, 7]
    factor_num_dict = {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1, 8: 1, 9: 1, 10: 2}

    factor_num = max_prime.get_prime_count(nums, prime_list)
    assert len(factor_num) == len(factor_num_dict)
    for key, value in factor_num.items():
        assert factor_num_dict[key] == value
    for key, value in factor_num_dict.items():
        assert factor_num[key] == value

    assert factor_num


def test_max_prime_main():

    data = [123, 43, 54, 12, 76, 84, 98, 678, 543, 231]
    max_prime = MaxPrime(lambda: str(data.pop()))
    max_prime.main()
    assert max_prime.__repr__() == "678 3"


def test_max_prime_big_number_main():

    data = [123, 43, 54, 12, 76, 84, 98, 678, 543, 231, 123451]
    max_prime = MaxPrime(lambda: str(data.pop()))
    max_prime.main()
    assert max_prime.__repr__() == "678 3"
