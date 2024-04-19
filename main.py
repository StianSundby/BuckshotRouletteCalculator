from GameState import GameState
from MCTSNode import MCTSNode

#initialize root node and find best move
def main():
    initialRounds = [0, 1, 0, 1, 1, 0]  #example setup
    initialState = GameState(initialRounds)
    root = MCTSNode(state=initialState)
    selectedNode = root.bestMove()

    #print best action and win rate if selectedNode exists
    if selectedNode and selectedNode.parent:
        action = selectedNode.parentMove
        winrate = selectedNode.winRate() * 100  #convert to percentage
        print(f"Best action: {action} with a win rate of {winrate:.2f}%")
    else:
        print("No valid actions could be determined.")
    
    return selectedNode

if __name__ == "__main__":
    result = main()