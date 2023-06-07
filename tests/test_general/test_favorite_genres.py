from copy import deepcopy
from random import choice, randint
from typing import List

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from pytry.general.favorite_genres import FavoriteGeneres


@pytest.fixture(name="favorite_genres_data")
def input_data() -> List:
    return [
        "hossein Horror Romance Comedy",
        "mohsen Horror Action Comedy",
        "mina Adventure Action History",
        "sajjad Romance History Action",
        "4",
        "invalid number",
    ]


def test_favorite_genres_init(favorite_genres_data: List):

    favorite_genres = FavoriteGeneres(lambda: str(favorite_genres_data.pop()))
    assert favorite_genres
    assert favorite_genres.key_data
    assert favorite_genres.input_count


def test_favorite_genres_main(favorite_genres_data: List):
    favorite_genres = FavoriteGeneres(lambda: str(favorite_genres_data.pop()))
    favorite_genres.main()
    assert favorite_genres.__repr__() == (
        "Action : 3\nComedy : 2\nHistory : 2\nHorror : 2\nRomance : 2\nAdventure : 1\n"
    )


@given(st.sets(st.text(alphabet=st.characters(blacklist_characters=" "))), st.integers(min_value=0, max_value=6))
@example({}, 0)
@example({""}, 0)
@example({"", "n',"}, 2)
def test_favorite_genres_main_with_hypothesis(names, n_choice):

    genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]

    total = 0
    data = []
    for name in names:
        choices = []
        genres_copy = deepcopy(genres)
        for _ in range(randint(0, n_choice)):
            gen_choice = choice(genres_copy)
            genres_copy.remove(gen_choice)
            choices.append(gen_choice)
            total += 1
        data.append(" ".join([name] + choices))
    print(data)

    favorite_genres = FavoriteGeneres(lambda: str(data.pop()), len(names))
    favorite_genres.main()
    print(favorite_genres.__repr__())
    assert total == sum([value["count"] for value in favorite_genres.key_stats.values()])
