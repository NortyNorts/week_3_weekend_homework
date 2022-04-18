from secrets import choice
from models.player import *

class Game():

    def __init__(self):
        self.winner = []
        self.move_1 = "rock"
        self.move_2 = "paper"
        self.move_3 = "scissors"
        self.moves =[self.move_1,self.move_2,self.move_3]

    def play_new_game(self, player_1, player_2):
        if player_1 == self.move_1 and player_2 == self.move_2:
            self.winner.append("Player 2 wins!!! Paper beats Rock!")

        elif player_1 == self.move_1 and player_2 == self.move_3:
            self.winner.append("Player 1 wins!!! Rock beats Scissors")

        elif player_1 == self.move_2 and player_2 == self.move_3:
            self.winner.append("Player 2 wins!!! Scissors beats Paper!")

        elif player_1 == self.move_2 and player_2 == self.move_1:
            self.winner.append("Player 1 wins!!! Paper beats Rock!")
            
        elif player_1 == self.move_3 and player_2 == self.move_1:
            self.winner.append("Player 2 wins!!! Rock beats Scissors")

        elif player_1 == self.move_3 and player_2 == self.move_2:
            self.winner.append("Player 1 wins!!! Scissors beats Paper!")

        else:
            self.winner.append("Tie, play again")