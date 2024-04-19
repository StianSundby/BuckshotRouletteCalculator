import numpy as np
from collections import defaultdict

class MCTSNode():
    def __init__(self, state, parent=None, parentMove=None):
        self.state = state #state of the game
        self.parent = parent #None for the root node; for other nodes, it's the node from which it is derived
        self.parentMove = parentMove #None for the root node; for other nodes, it's the action its parent carried out
        self.children = [] #contains all possible actions from the current node
        self.visits = 0 #Number of times current node is visited
        self.results = defaultdict(int)
        self.results[1] = 0 
        self.results[-1] = 0
        self.untriedMoves = self.legalMoves()
        return
    

    #returns the list of untried actions from a given state
    def legalMoves(self):
        return self.state.legalMoves()

    def updateStats(self, result):
        self.visits += 1
        self.results[result] += 1

    def winRate(self):
        wins = self.results[1]  # Assuming 1 is a win
        if self.visits == 0:
            return 0
        return wins / self.visits

    #returns the difference of wins - losses
    def q(self):
        wins = self.results[1]
        losses = self.results[-1]
        return wins - losses
    

    #returns the number of times each node is visited
    def n(self):
        return self.visits
    

    #Next state is generated depending on the action which is carried out.
    #In this step all the possible child nodes corresponding to generated 
    #states are appended to the children array and the child_node is returned. 
    #The states which are possible from the present state are all generated and 
    #the child_node corresponding to this generated state is returned.
    def expand(self):
        action = self.untriedMoves.pop()
        nextState = self.state.move(action)
        child_node = MCTSNode(nextState, parent=self, parentMove=action)
        self.children.append(child_node)
        return child_node
    

    #check if the current node is terminal or not (game over)
    def isTerminal(self):
        return self.state.gameOver()
    

    #from the current state, entire game is simulated till there is an outcome for the game
    #1 = win, 0 = tie, -1 = loss
    def rollout(self):
        currentRolloutState = self.state

        while not currentRolloutState.gameOver():
            possibleMoves = currentRolloutState.legalMoves()
            action = self.rolloutPolicy(possibleMoves)
            currentRolloutState = currentRolloutState.move(action)
        return currentRolloutState.gameResult()
    

    #all the statistics for the nodes are updated
    #untill the parent node is reached, the number of visits for each node is incremented by 1
    #if result is 1, then the win is incremented by 1
    #otherwise loss is incremented by 1
    def backPropagate(self, result):
        self.visits += 1.
        self.results[result] += 1.
        if self.parent:
            self.parent.backPropagate(result)


    #all the actions are popped out of _untried_actions one by one. empty = size is 0, I.E fully expanded
    def fullyExpanded(self):
        return len(self.untriedMoves) == 0
    
    #selects the best child out of the children array. 
    #the first term in the formula corresponds to exploitation and the second term corresponds to exploration
    def bestPath(self, cParam=0.1):
        # Calculate the weights for each child node based on the UCB1 formula (optimism in the face of uncertainty/Upper Confidence Bound),
        # which balances between exploitation and exploration in the MCTS algorithm.
        # For each child node c, calculate the weight using the UCB1 formula:
        #   - (c.q() / c.n()): The average reward (q-value) of node c divided by
        #                      the number of times node c has been visited (exploitation).
        #   - cParam * np.sqrt((2 * np.log(self.n()) / c.n())): The exploration term
        #       - np.log(self.n()): Natural logarithm of the number of times the current
        #                           node has been visited.
        #       - c.n(): Number of times node c has been visited.
        #       - cParam: Exploration parameter that controls the balance between
        #                 exploitation and exploration. A higher cParam value promotes
        #                 more exploration.
        #   - The sum of these two terms represents the UCB1 value, which guides
        #     the selection of the next child node to explore in the MCTS algorithm.
        weights = [(c.q() / c.n()) + cParam * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(weights)]
    

    #randomly selects a move out of possible moves
    def rolloutPolicy(self, possibleActions):
        return possibleActions[np.random.randint(len(possibleActions))]

    
    #selects node to run rollout()
    def treePolicy(self):
        currentNode = self
        while not currentNode.isTerminal():
            if not currentNode.fullyExpanded():
                return currentNode.expand()
            else:
                currentNode = currentNode.bestPath()
        return currentNode
    

    #returns the node corresponding to best possible move through expansion, simulation and backpropagation
    def bestMove(self):
        simNo = 100

        for i in range(simNo):
            v = self.treePolicy()
            reward = v.rollout()
            v.backPropagate(reward)
        
        return self.bestPath(cParam=0.)
