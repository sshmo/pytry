"""
World Cup score board.

Iran, Portugal, Spain and Morocco are present in Group B of the World Cup.
Write a program that, upon receiving the results of the games,
will print the team name, the number of wins and losses,
and the difference in goals and points respectively in one line.
Each team should be printed in order of points in one line.
(If the points are equal, the number of wins will be considered.
If both the number of wins and the points are equal,
they will be printed in alphabetical order.)

Note: The team gets zero points in case of loss,
one point in case of draw and three points in case of win.
Goal difference is the difference between goals scored and goals conceded by a team.

Read the results of the games in the following order:
(in the sample entry, the left number corresponds to the right team.)

Input:
Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
Spain - Morocco
Portugal - Morocco
2-2
2-1
1-2
2-2
3-1
2-1

Output:
Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
"""
