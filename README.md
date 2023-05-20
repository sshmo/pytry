# pytry

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
    from pytry.general.world_cup.dataframe import DFScoreBoard
    score_board = DFScoreBoard(input)
    score_board.main()
    print(score_board)
```
