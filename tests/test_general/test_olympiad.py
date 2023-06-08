from random import choice
from typing import List

import pytest
from hypothesis import given
from hypothesis import strategies as st

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


@given(texts=st.sets(st.text(alphabet=st.characters(blacklist_characters="."))))
def test_olympiad_main_with_hypothesis(texts):
    data = []
    count = int(len(texts) / 2)
    texts = list(texts)
    for i in range(count):
        name = texts[i]
        program = texts[i + count]
        gender = choice(["f", "m"])
        data.append(".".join([gender, name, program]))

    olympiad = Olympiad(lambda: str(data.pop()), count)
    olympiad.main()
    print(olympiad.__repr__())
