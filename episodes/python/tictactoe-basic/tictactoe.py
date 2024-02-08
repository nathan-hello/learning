#goals:
#print a board, allow the player to add an x or o onto the board
#have the computer place a random x or o on the board
#then make it a proper window, play the game outside of the terminal
#save the scores to JSON, XML, and CSV format (import/export feature)

#what if the history file has just the dictionary and we make a program that interprets the dictionary and displays the history
import random
import string
import numpy as np
letter_list = list(string.ascii_lowercase)
xo_list = ['x', 'o']
player_dict = {}



def setup():
    def get_num_players():
        def hidden():
            while True:
                try:
                    num_of_players = int(input("How many players? "))
                    if num_of_players >= 2 and num_of_players <= 26:
                        break
                    else:
                        print("Choose a number between 2 and 26! ")
                except ValueError:
                    print("Choose a number between 2 and 26! \n")
        num_of_players = 2
        return num_of_players

    def get_letter_dict():
    
        #this is for the human player, player one
        #when they choose a letter, it's removed from the letter_list and xo_list

        number_of_players = get_num_players()
        # player_one = input("What letter would you like? ")
        player_one = 'x'
        letter_list.remove(player_one)
        try:
            xo_list.remove(player_one)
        except:
            pass
        player_dict[1] = player_one

        for x in range(number_of_players - 1):
            player_number = x + 2
            try:
                xo_current_choice = random.choice(xo_list)
                player_dict[player_number] = xo_current_choice
                xo_list.remove(xo_current_choice)
                letter_list.remove(xo_current_choice)
            except:
                letter_current_choice = random.choice(letter_list)
                player_dict[player_number] = letter_current_choice
                letter_list.remove(letter_current_choice)
        # print(player_dict)
        return(player_dict)

    #gets the dictionary for all players
    global all_players_dict
    all_players_dict = get_letter_dict()
    
    #grabs the player number (the key) for all players
    global all_players
    all_players = list(all_players_dict.keys())
    
    #makes a list of just the ai players
    global ai_players
    ai_players = all_players[1:]
 
    global playspace
    playspace = blank_board_state()
    
    global available_places
    available_places = list(playspace.keys())
    print(f' all_players_dict: {all_players_dict} \n all_players: {all_players} \n ai_players: {ai_players} \n playspace: {playspace} \n available_places: {available_places}')
    return
    
def blank_board_state(grid_size_square_root = 5):
    #this makes a dictionary with a value corrisponding to every
    #slot in the 2d array, making them all equal 0
    grid_size_squared = grid_size_square_root * grid_size_square_root
    blank_grid_dict = {}
    slot_number = 1
    for x in range(grid_size_squared):
        blank_grid_dict[slot_number] = 0
        slot_number = slot_number + 1
    return blank_grid_dict

def humans_choice_func(available_places):
    while True:
        humans_choice = input("what slot would you like to choose ")
        try:
            list(available_places).remove(int(humans_choice))
            # print(f'{humans_choice} was in {available_places}')
            break
        except ValueError:
            # print(f'{humans_choice} was NOT in {available_places}')
            print("Try again")
        except KeyboardInterrupt:
            raise StopIteration
        
    return int(humans_choice)

def board_logic():
    while bool(available_places) == True:
        #this could be 'while available_places' but there's extra words for clarity
        humans_choice = humans_choice_func(available_places)
        available_places.remove(humans_choice)
        playspace[humans_choice] = 1
        
        winner_check = check_for_win(playspace)
        if winner_check != None:
            printboard(playspace)
            return callwinner(winner_check)
        printboard(playspace)
        
        while bool(available_places) == True:
            for x in ai_players:
                ai_choice = random.choice(available_places)
                playspace[ai_choice] = x
                available_places.remove(ai_choice)
                
                winner_check = check_for_win(playspace)
                if winner_check != None:
                    printboard(playspace)
                    return callwinner(winner_check)
                printboard(playspace)
            break        
    printboard(playspace)
    print("It's a tie!")

def check_for_win(playspace):
    playspace = dict(playspace)
    spaces_list = list(playspace.values())
    spaces_list.insert(0, 0)
    print(spaces_list)

    #rows
    if np.all(spaces_list[1:3] == spaces_list[1]) in all_players and all(spaces_list[1:3]) != 0:
            return spaces_list[1]   
    elif np.all(spaces_list[4:6] == 4) and all(spaces_list[4:6]) != 0:
        return spaces_list[4]
    elif np.all(spaces_list[7:9] == 7) and all(spaces_list[7:9]) != 0:
        return spaces_list[7]
    #columns
    elif np.all(spaces_list[1:7:3] == 1) and all(spaces_list[1:7:3]) != 0:
        return spaces_list[1]
    elif np.all(spaces_list[2:8:3] == 2) and all(spaces_list[2:8:3]) != 0:
        return spaces_list[2]
    elif np.all(spaces_list[3:9:3] == 3) and all(spaces_list[3:9:3]) != 0:
        return spaces_list[3]
    #diagonals
    elif np.all(spaces_list[1:9:4] == 1) and all(spaces_list[1:9:4]) != 0:
        return spaces_list[1]
    elif np.all(spaces_list[3:7:2] == 3) and all(spaces_list[3:7:2]) != 0:
        return spaces_list[3]
    else:
        return None

def printboard(playspace):    
    playspace = dict(playspace)
    board = [0]
    for x in playspace.values():
        if x == 1:
            board.append("X")
        elif x == 2:
            board.append("O")
        elif x == 0:
            board.append("_")
        # print(x, board, playspace.values())

    print(f'\n  {board[1]} | {board[2]} | {board[3]}')
    print("-------------")
    print(f'  {board[4]} | {board[5]} | {board[6]}')
    print("-------------")
    print(f'  {board[7]} | {board[8]} | {board[9]}\n')


def callwinner(winner):
    winner = winner = 1
    winner = str(all_players_dict.get(winner)).upper()
    print(f'{winner} WINS!')

setup()
board_logic()

