# squashDashboard
 Python3 client for recording squash games.

This is a simple Python3 tkinter project for tracking squash games.

Usage:

Select two players from the dropdown menus, points can be added to these players through the 'add point' buttons.
The maximum score for a game is 11 points. The game is won when the first player has a two point lead over their opponent when at or above 11 points.

Once a game has been finished, the new game button will reset all game points, whilst keeping a log of all games played in the current match. Once the match has been finished, the save match button will log all of the games played in a .csv file in the same directory as the program.

Known limitations:

No current database support.
No current config file for configuring the interface.
