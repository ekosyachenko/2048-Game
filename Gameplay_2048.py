from Functions_2048 import *


randomize_new_cell()
randomize_new_cell()


while (game_over() !=True)and(game_won() !=True):
    print_field()
    direction=input("Where to slide the field? 'U' - up, 'D' - down, 'L'- left, 'R'-right.\n " + 
        "Please enter the letter corresponding to your choise and press 'Enter' \n")
    
    state_of_game1=[]
    for x in range(1,5):
        for y in range(1,5):
            state_of_game1.append(get_cell(x,y))

    if direction=='U' or direction=='u':
        move(up)
    elif direction=='D' or direction=='d':
        move(down)
    elif direction=='L' or direction=='l':
        move(left)
    elif direction=='R' or direction=='r':
        move(right)

    state_of_game2=[]
    for x in range(1,5):
        for y in range(1,5):
            state_of_game2.append(get_cell(x,y))

    if num_empty()>0 and not(state_of_game1 == state_of_game2):
        randomize_new_cell()

if game_over()==True: #Doesn't work
    print_field()
    print('Game is over!You lost')
elif game_won()==True:
    print_field()
    print('Congratulations! You won the game!')


