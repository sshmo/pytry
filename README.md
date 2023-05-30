# pytry

[![codecov.io](https://codecov.io/github/sshmo/pytry/coverage.svg?branch=master)](https://codecov.io/github/sshmo/pytry?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pytry is a place to try python.

## developmant

``` sh
    make dev
```

## Test

``` sh
    make test
```

## usage

First install pytry:

``` sh
    git clone git@github.com:sshmo/pytry.git
    cd pytry
    pip install .
```

Usage:

``` python
    from pytry.general.world_cup_dataframe import DFScoreBoard
    score_board = DFScoreBoard(input)
    score_board.main()
    print(score_board)
```
