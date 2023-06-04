from typing import List

import pytest

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
