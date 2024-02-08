from ast import Import
import string
import random
import time




def user_input():
    pw_input = {}
    #user inputs what kind of characters in their password generator they want
    pw_input['letter'] = input("Do you want letters in your password? y/n ")
    if pw_input['letter'] == 'y':
        pw_input['case'] = input("Do you all lower case, all upper case, or a mix? l/u/m ")
    elif pw_input['letter'] == 'n':
        pw_input['case'] = False
    pw_input['num'] = input("Do you want numbers? y/n ")
    pw_input['sym'] = input("Do you want symbols? y/n ")
    
    #user inputs how long the password is
    pw_input['size'] = int(input("How long do you want your password to be? 1-63 "))

    return pw_input

def password_gen():
    pw_input = user_input()
    password = []
    pw_str = ''
    for x in range(pw_input['size'] * 100):
        if pw_input['letter'] == 'y' and pw_input['case'] == 'm':
            password.append(random.choice(string.ascii_letters))
        if pw_input['letter'] == 'y' and pw_input['case'] == 'u':
            password.append(random.choice(string.ascii_uppercase))
        if pw_input['letter'] == 'y' and pw_input['case'] == 'l':
            password.append(random.choice(string.ascii_lowercase))
        if pw_input['num'] == 'y':
            password.append(random.choice(string.digits))
        if pw_input['sym'] == 'y':
            password.append(random.choice(string.punctuation))
    
    print("SCRAMBING...\nPLEASE REMAIN CALM")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    for x in range(5000):
        pw_str = ''
        
        for y in range(pw_input['size']):
            pw_str += str(random.choice(password))
        if x < 4999:
            print(pw_str)
        

    print(f'\n \n             THE COUNCIL HAS DEICDED ON A PASSWORD.\n\n{pw_str}')

password_gen()