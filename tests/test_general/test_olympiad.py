from typing import List

import pytest

from pytry.general.olympiad import Olympiad


@pytest.fixture(name="olympiad_data")
def input_data() -> List:
    return [
        "m.hosSein.python",
        "f.miNa.C",
        "m.aHMad.C++",
        "f.Sara.java",
        "4",
        "invalid number",
    ]


def test_olympiad_init(olympiad_data: List):

    olympiad = Olympiad(lambda: str(olympiad_data.pop()))
    assert olympiad
    assert olympiad.input_count
    assert olympiad.key_data


def test_olympiad(olympiad_data: List):
    olympiad = Olympiad(lambda: str(olympiad_data.pop()))
    assert olympiad.__repr__() == "f Mina C\nf Sara java\nm Ahmad C++\nm Hossein python\n"
