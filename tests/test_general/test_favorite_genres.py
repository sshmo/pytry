from typing import List

import pytest

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
