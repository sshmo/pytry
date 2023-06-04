# Usage

First download the code from pytry GitHub repository and install it:

``` sh
    git clone git@github.com:sshmo/pytry.git
    cd pytry
    pip install .
```

Usage:

``` python
    from pytry.general.world_cup_dataframe import DFScoreBoard
    score_board = DFScoreBoard(input, 6)
    score_board.main()
    print(score_board)
```
