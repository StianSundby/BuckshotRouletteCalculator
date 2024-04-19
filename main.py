from GameState import GameState
from MCTSNode import MCTSNode

#initialize the root node and call the best_action function to get the best node
def main():
    initialRounds = [0, 1, 0, 1, 1, 0]  # Example setup
    initialState = GameState(initialRounds)
    root = MCTSNode(state=initialState)
    selectedNode = root.bestMove()

    # Check if a selected_node exists and print relevant information
    if selectedNode and selectedNode.parent:
        action = selectedNode.parentMove
        winrate = selectedNode.winRate() * 100  # Convert to percentage
        print(f"Best action: {action} with a win rate of {winrate:.2f}%")
    else:
        print("No valid actions could be determined.")
    
    return selectedNode

if __name__ == "__main__":
    result = main()