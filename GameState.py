class GameState:
    def __init__(self, rounds, player_turn=0):
        self.rounds = rounds #e.g., [0, 1, 0, 1, 1, 0]
        self.index = 0
        self.lives = [2, 2]
        self.turn = player_turn


    #return legal moves based on current state
    def legalMoves(self):
        if self.index < len(self.rounds):
            return ["shoot_self", "shoot_opponent"]
        return [] #no actions available if all rounds are spent
    

    #check if the game is over
    def gameOver(self):
        return any(life <= 0 for life in self.lives) or self.index >= len(self.rounds)
    

    #return game result: -1 for lose, 1 for win, 0 for not over
    def gameResult(self):
        if self.lives[0] <= 0:
            return -1
        elif self.lives[1] <= 0:
            return 1
        return 0
    

    #move to the next state based on the action taken
    def move(self, action):
        nextState = GameState(self.rounds.copy(), 1 - self.turn)
        nextState.lives = self.lives.copy()
        nextState.index = self.index + 1

        round = self.rounds[self.index]

        if action == "shoot_opponent":
            if round == 1:
                nextState.lives[1 - self.turn] -= 1

        elif action == "shoot_self":
            if round == 1:
                nextState.lives[self.turn] -= 1
            else:
                #blank, the current player gets another turn
                nextState.turn = self.turn

        return nextState