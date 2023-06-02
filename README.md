# pytry

[![codecov.io](https://codecov.io/github/sshmo/pytry/coverage.svg?branch=master)](https://codecov.io/github/sshmo/pytry?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://sshmo.github.io/pytry/)
[![CodeQL](https://github.com/sshmo/pytry/actions/workflows/codeql.yml/badge.svg)](https://github.com/sshmo/pytry/actions/workflows/codeql.yml)
[![pre-commit](https://github.com/sshmo/pytry/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/sshmo/pytry/actions/workflows/pre-commit.yml)

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
