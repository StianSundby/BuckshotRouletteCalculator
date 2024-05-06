
# Buckshot Roulette Calculator

is a tool designed calculate odds for the game [Buckshot Roulette](https://store.steampowered.com/app/2835570/Buckshot_Roulette/), created by [Mike Klubnika](https://mikeklubnika.itch.io/). The game involves the player and the computer taking turns shooting a shotgun loaded with a mix of live rounds and blank rounds, randomly drawn at the beginning of each round, and inserted into the shotgun in a random order. The objective is to be the last player standing, with each live round causing the loss of a life.

Where it gets interesting is with its various items and the rule that says if you shoot yourself with a blank, you get to fire again. Probability is for me a part of math that is not at all intuitive, which is why I wanted to make this tool.


# Monte Carlo Tree Search
MCTS is a [heuristic search algorithm](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) that builds a search tree by simulating numerous random trajectories (rollouts) from the current state of the system. These rollouts help estimate the value of different actions or states by averaging their outcomes over multiple simulations.
### Key Components

- Selection: MCTS traverses the tree from the root to a leaf node using a selection policy, such as the Upper Confidence Bound (UCB1) algorithm, to balance exploration and exploitation.

- Expansion: Once a leaf node is reached, MCTS expands the tree by adding child nodes corresponding to possible actions or states from the current node.

- Simulation (Rollout): MCTS conducts a simulated rollout from the newly added node until a terminal state is reached. The rollout policy determines how actions are chosen during simulation.

- Backpropagation: After the rollout, MCTS updates the statistics of all nodes traversed during the selection phase, backpropagating the results of the simulation to their ancestors.

- Repeat: The process of selection, expansion, simulation, and backpropagation is repeated for a specified number of iterations or until a termination condition is met.


# UCB1 Formula
The Upper Confidence Bound (UCB1) formula is a key component of the Monte Carlo Tree Search (MCTS) algorithm, specifically used during the selection phase to balance exploration and exploitation. It calculates a score for each child node in the search tree, guiding the selection of nodes for further exploration.

```python
UCB1(c) = (q(c) / n(c)) + cParam * sqrt(2 * ln(N) / n(c))
```
Where:

- q(c): The average reward (or value) of node c.
- n(c): The number of times node c has been visited.
- N: The total number of visits to the parent node.
- cParam: The exploration parameter that controls the balance between exploitation and exploration. A higher value promotes more exploration.

The UCB1 formula balances two objectives:
- Exploitation: Favoring nodes with higher estimated rewards ```(q(c) / n(c))```.
- Exploration: Exploring less-visited nodes or actions ```(sqrt(2 * ln(N) / n(c)))```.

By combining these objectives, UCB1 aims to select nodes that are both promising based on past experiences and unexplored to gather more information.
## Tech Stack

**Client:** Python


## Acknowledgements
 - [Buckshot Roulette](https://store.steampowered.com/app/2835570/Buckshot_Roulette/)
 - [Mike Klubnika](https://mikeklubnika.itch.io/)
 - [Readme.so](https://readme.so)
 - [Sakura](https://github.com/oxalorg/sakura)


## License

[MIT](https://choosealicense.com/licenses/mit/)

