from string import ascii_letters, digits
from typing import List

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from pytry.general.index_words import IndexWords


@pytest.fixture(name="index_words_data")
def input_data() -> List:
    return [
        "The Persian League is the largest sport event dedicated to the deprived areas of Iran. "
        "The Persian League promotes peace and friendship. "
        "This video was captured by one of our heroes who wishes peace."
    ]


def test_index_words_init(index_words_data: List):

    index_words = IndexWords(lambda: str(index_words_data.pop()), 1)
    assert index_words
    assert index_words.key_data


def test_index_words_main(index_words_data: List):
    index_words = IndexWords(lambda: str(index_words_data.pop()), 1)
    index_words.main()
    assert index_words.__repr__() == "2:Persian\n3:League\n15:Iran\n17:Persian\n18:League\n"


@given(st.text(ascii_letters + "., " + digits, min_size=50))
@example("KVhTsmA lWKEqwD GgnJUTlBExeZ F")
@example("A ")
@example("A. B")
@example("A, B.")
def test_index_words_main_with_hypothesis(data):
    index_words = IndexWords(lambda: str([data].pop()), 1)
    index_words.main()
    key_stats: dict = index_words.key_stats
    index_words.__repr__()
    for _, val in key_stats.items():
        assert val and "." not in val and "," not in val and all(char.isascii() for char in list(val))
