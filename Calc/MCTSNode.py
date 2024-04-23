import numpy as np
from collections import defaultdict

class MCTSNode():

    #initialize MCTS Node with state, parent, and parentMove
    def __init__(self, state, parent=None, parentMove=None, mode=1):
        self.state = state
        self.parent = parent
        self.parentMove = parentMove
        self.mode = mode
        self.children = []
        self.visits = 0
        self.results = defaultdict(int)
        self.results[1] = 0 
        self.results[-1] = 0
        self.untriedMoves = self.legalMoves()
        return
    

    #return untried actions from current state
    def legalMoves(self):
        return self.state.legalMoves()


    #update statistics based on result
    def updateStats(self, result):
        self.visits += 1
        self.results[result] += 1


    #return win rate based on visit count
    def winRate(self):
        wins = self.results[1]
        if self.visits == 0:
            return 0
        return wins / self.visits


    #return difference between wins and losses
    def q(self):
        wins = self.results[1]
        losses = self.results[-1]
        return wins - losses
    

    #return number of visits
    def n(self):
        return self.visits
    

    #generate next state and corresponding child node
    def expand(self):
        action = self.untriedMoves.pop()
        nextState = self.state.move(action)
        child_node = MCTSNode(nextState, parent=self, parentMove=action, mode=self.mode)
        self.children.append(child_node)
        return child_node
    

    #check if current node is terminal
    def isTerminal(self):
        return self.state.gameOver()
    

    #simulate game until outcome and return result
    def rollout(self):
        currentRolloutState = self.state
        while not currentRolloutState.gameOver():
            possibleMoves = currentRolloutState.legalMoves()
            action = self.rolloutPolicy(possibleMoves)
            currentRolloutState = currentRolloutState.move(action)
        return currentRolloutState.gameResult()
    

    #update statistics recursively up to root node
    def backPropagate(self, result):
        self.visits += 1.
        self.results[result] += 1.
        if self.parent:
            self.parent.backPropagate(result)


    #check if all moves are explored
    def fullyExpanded(self):
        return len(self.untriedMoves) == 0
    

    #select best child based on UCB1 formula
    def bestPath(self, cParam=0.1):
        weights = [(c.q() / c.n()) + cParam * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(weights)]
    

    #select action randomly for rollout
    def rolloutPolicy(self, possibleActions):
        return possibleActions[np.random.randint(len(possibleActions))]

    
    #select node based on tree policy
    def treePolicy(self):
        currentNode = self
        while not currentNode.isTerminal():
            if not currentNode.fullyExpanded():
                return currentNode.expand()
            else:
                currentNode = currentNode.bestPath()
        return currentNode
    

    #run simulations and return best move
    def bestMove(self, simNo):
        for i in range(simNo):
            v = self.treePolicy()
            reward = v.rollout()
            v.backPropagate(reward)
        
        if self.mode == 0:
            return max(self.children, key=lambda x: x.winRate())
        elif self.mode == 1:
            return max(self.children, key=lambda x: x.q() / x.n())
        else:
            return self.bestPath(cParam=0.)
