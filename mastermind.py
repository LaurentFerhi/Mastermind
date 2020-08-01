# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:48:37 2020
@author: Laurent Ferhi
"""
import random

def compar_list(cpu_list, ply_list):
    '''
    Compares the items of 2 lists and returns a tuple of
    right placed, misplaced and false elements
    '''
    counter_ok, counter_misplaced, counter_false = 0,0,0
    for i in range(len(cpu_list)):
        if ply_list[i]==cpu_list[i]:
            counter_ok += 1
        elif ply_list[i] in cpu_list:
            counter_misplaced += 1
        else:
            counter_false += 1
    return (counter_ok, counter_misplaced, counter_false)

def mastermind(digits=4, turns=10):
    '''
    Game of mastermind with 'digits' numbers and 'turns' turns
    '''
    ### generate actual list to be found
    actual_list = random.sample(range(0, 9), 4)
    ### Game definition
    # Welcome message
    print('\n>>',
          digits,
          'chiffres distincts entre 0 et 9 à trouver:\n',
          digits*'_ ')
    
    # Header for the current turn
    for turn in range(turns):
        if turn != turns-1:
            print('\n>> Tour',turn+1,', Votre proposition ?')  
        else:
            print('\n>> Dernière chance ! Votre proposition ?')
        
        # Current turn - user input
        user_input = False
        player_prop = []
        while user_input == False:
            try:
                player_prop = [int(i) for i in list(input())]
                if len(player_prop) != digits:
                    raise(ValueError)
                user_input = True
            except ValueError:
                print('Entrer exactement',digits,'chiffres')
                
        # Analyse answer
        #print(actual_list)
        
        result = compar_list(actual_list,player_prop)
        print('- Nombre de chiffres bien placés :',result[0])
        print('- Nombre de chiffres mal placés :',result[1])
        print('- Nombre de chiffres faux :',result[2])
        
        # case of winning
        if result == (4,0,0):
            print('\n>> Bravo ! Vous avez trouvé',actual_list)
            return
    print('\n>> Vous avez perdu... La réponse était',actual_list)
    return

def game():
    '''
    Game turns management
    '''
    print('### Bienvenue au Mastermind ###')
    while True:
        mastermind()
        print('\n>> Voulez vous rejouer ? (y/n)')
        if input() != 'y':
            print('\n>> A bientôt !')
            break

if __name__ == "__main__":
    game()