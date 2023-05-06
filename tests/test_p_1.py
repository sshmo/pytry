import random
from string import ascii_letters

from pytry.p_1 import get_nums


def mock_input():
    return str(random.choice([random.choice(ascii_letters), random.randint(1, 1000)]))


def test_get_nums():
    nums = get_nums(mock_input)
    assert len(nums) == 10
    for num in nums:
        assert isinstance(num, int)
