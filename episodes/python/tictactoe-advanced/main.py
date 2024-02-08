import string
import random
import csv 
import players
import userinput
import os
os.chdir('tictactoe-advanced/')


class Player:
    def __init__(self, player_number, human_ai, letter):
        self.human_ai = human_ai
        self.letter = letter
        self.player_number = player_number

    def debug(self):
        print(f'{self.letter} is {self.human_ai} and is number {self.player_number}')
    def choice(self):
        if self.human_ai == 'human':
            print(f'{self.letter} is {self.human_ai} and is number {self.player_number}')
            userinput.human_choice()
        if self.human_ai == 'ai':
            print(f'{self.letter} is {self.human_ai} and is number {self.player_number}')
            choice = (random.choice(range(3)),random.choice(range(3)))
            return choice
            
            pass
    def call_win():
        pass

    pass

#TODO: get available places, figure out how to print board
#manipulate board in a ai/human agnostic way (it just takes the input from their respective classes)
#get available_spaces but in a matrix instead of a dictionary (i'll have to use the current board state instead of a another list/dict)
#save player or ai's choice to a dictionary or something to track who is where
class Board:

    def setup():
        global board
        board = [[0 for y in range(3)] for y in range(3)]
        print(board)
    # @staticmethod
    def manipulate(pdict):
        for key in pdict:
            choice_tuple = pdict[key].choice()
            print(choice_tuple[0])
            board.insert(choice_tuple[0], key)
            print(board)
            
            pass
        pass
    


def p_dict():
    #this makes an object out of every row of the CSV made in players.py
    #it then puts that object in a dictionary value, with the key being the corresponding player number
    #to call the object, you would use pdict()[<player_number>].method()
    with open('players.csv', newline='') as p_csv:
        players = list(csv.reader(p_csv, delimiter=','))
    player_obj_dict = {}
    for row in players:
        player_obj = Player(row[1], row[2], row[3])
        player_obj_dict[int(row[1])] = player_obj
    return player_obj_dict


def main():
    players.gen()
    pd = p_dict()
    # for key in pd:
    #     pd[key].debug()
    Board.setup()
    Board.manipulate(pd)


            







if __name__ == '__main__':
    main()