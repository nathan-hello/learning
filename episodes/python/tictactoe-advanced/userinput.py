def is_human_playing():
    return False
def num_of_num_human_players():
    return 0
def num_players():
    return 2
def human_player_letter(player):
    #player is going to be used for printing which player the human is inputting for
    #this function should return a single letter
    return input(f'{player} letter: ')
def get_board_size():
    return 3
def human_choice(player):
    print(f'{player} choice:')
    x = int(input("row: "))
    y = int(input("col: "))
    return (x, y)


class Errors:
    def letter_already_chosen():
        print("This letter has already been chosen")
    def bad_num_of_players():
        print("Choose a number between 2 and 26")
