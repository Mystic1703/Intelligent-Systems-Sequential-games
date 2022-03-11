# Intelligent-Systems-Sequential-games
Simple Python game that visualizes basic algorithms of sequential games: Minimax, MinimaxAB, MaxN and Expectimax.

This project is visualizing algorithms for sequential games, like:
1) Minimax for 2 rational players.
2) Minimax with alpha-beta cutting for two rational players.
3) MaxN - Minimax algorithm for 2 or more rational players without the possibility of forming alliances.
4) Expectimax - Expectimax algorithm with only Max and Chance nodes, presuming that all the other players play random moves.

Map is defined by two type of fields: Path tile - The tile that can be stepped on; Hole tile - The tile that can't be stepped on.
After the game is started, agents battle between each other, with their own algorithm that defines them. They play sequentially, one after another, until one of them has no
path tiles to pass onto. For each move, they form their tree of possible moves, and choose to play their best move. If defeat is inevitable, the agent plays random moves until
it is defeated. In command line arguments, beside the map that will be played on, and the agent that is choosen to play, there are two more arguments: 
1) time to think: Maximum thinking time for next move, in milliseconds;
2) max levels: Maximum tree depth of possible moves.

Game can be started by pressing SPACE, where afterwards the game will start, and each move will be animated, for every player on the map.
By pressing ESC, the program finishes.
