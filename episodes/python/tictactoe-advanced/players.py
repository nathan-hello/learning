import string
import random
import csv
import userinput

def get_num_players():
    while True:
        try:
            num_of_players = userinput.num_players()
            if num_of_players >= 2 and num_of_players <= 26:
                break
            else:
                userinput.Errors.bad_num_of_players()
        except ValueError:
            userinput.Errors.bad_num_of_players()
    return num_of_players

def gen():    

    #this is for the human player, player one
    #when they choose a letter, it's removed from the letter_list and xo_list
    #in case there are no human players, make num_ai_players = num_of_players. 
    #if there are human players, then this gets subtracted

    num_of_players = get_num_players()
    num_ai_players = num_of_players
    current_player_calc = 0

    letter_list = list(string.ascii_lowercase)
    xo_list = ['x', 'o']

    open('players.csv', 'w').close()

    if userinput.is_human_playing():
    
        num_human_players = userinput.num_of_num_human_players()
        num_ai_players = num_of_players - num_human_players

        #ask user what letter, then try to remove that letter from xo_list
        #if it's already not in xo_list, remove from all string list, if it's still not there then it's not available, throw error
        #write this player in a new line in a csv file, used for later. csv formatting will be the same as the Player class
        #finally, subtract num_of_players, so the ai forloop knows how many ai to make
        #add currect_player_calc at the end so the csv starts with 0

        for player in range(num_human_players):
            current_player_calc += 1
            player_letter = userinput.human_player_letter(player)
            try:
                xo_list.remove(player_letter)
                letter_list.remove(player_letter)
            except:
                try:
                    letter_list.remove(player_letter)
                except:
                    userinput.Errors.letter_already_chosen()
            p_writer(current_player_calc, 'human', player_letter)
            current_player_calc += 1
            num_of_players -= 1

    for ai in range(num_ai_players):
        try:
            player_letter = random.choice(xo_list)
            xo_list.remove(player_letter)
            letter_list.remove(player_letter)

            p_writer(current_player_calc, 'ai', player_letter)

        except:
            player_letter = random.choice(letter_list)
            letter_list.remove(player_letter)

            p_writer(current_player_calc, 'ai', player_letter)
        current_player_calc += 1


def p_writer(calc, hum_ai, letter):
    with open('players.csv', 'a', newline='') as p:
        p_write = csv.writer(p, delimiter=',')
        p_write.writerow(['player', calc, hum_ai, letter])




