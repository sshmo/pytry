from typing import List

import pytest

from pytry.general.favorite_genres import FavoriteGeneres


@pytest.fixture(name="data")
def input_data() -> List:
    return [
        "hossein Horror Romance Comedy",
        "mohsen Horror Action Comedy",
        "mina Adventure Action History",
        "sajjad Romance History Action",
        "4",
        "invalid number",
    ]


def test_favorite_genres_init(data: List):

    favorite_genres = FavoriteGeneres(lambda: str(data.pop()))
    assert favorite_genres
    assert favorite_genres.favorite_gen
    assert favorite_genres.number_of_people


def test_favorite_genres_main(data: List):
    favorite_genres = FavoriteGeneres(lambda: str(data.pop()))
    favorite_genres.main()
    print(favorite_genres)
    assert favorite_genres.__repr__() == (
        "Action : 3\nComedy : 2\nHistory : 2\nHorror : 2\nRomance : 2\nAdventure : 1\n"
    )
