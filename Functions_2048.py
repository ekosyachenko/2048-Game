field_values={(1,1):0,(1,2):0,(1,3):0,(1,4):0,(2,1):0,(2,2):0,(2,3):0,(2,4):0,
              (3,1):0,(3,2):0,(3,3):0,(3,4):0,(4,1):0,(4,2):0,(4,3):0,(4,4):0}

def get_cell(x,y):
    '''
(int,int)->int

Returns value in cell at location (x,y)

Precondition: 1<=x<=4, 1<=y<=4
'''
    return field_values[(x,y)]

def set_cell(x,y,value):
    '''
(int,int,int)-> NoneType

Value is a number. Set value to cell at location (x,y)
Precondition: 1<=x<=4, 1<=y<=4
'''
    field_values[(x,y)]=value


def num_empty():
    ''' NoneType -> int

Returns the number of empty cells in the current state of the game
'''
    num_empty=0
    for x in range(1,5):
        for y in range (1,5):
            if get_cell(x,y)==0:
                num_empty=num_empty+1

    return num_empty

def randomize_new_cell():
    ''' NoneType->NoneType

Based on the current state of game randomly chooses an empty cell and assigns
it with value '2'.
'''
    from random import randint
    i = randint(1,num_empty()) #Inclusive
    n=0

    for x in range(1,5):
        for y in range (1,5):
            if get_cell(x,y)==0:
                n=n+1
                if n==i:
                    set_cell(x,y,2)

def print_field():
    ''' Prints the current state of the game on the screen'''
    for y in range(1,5):
        for x in range (1,5):
            print(str(get_cell(x,y)).rjust(6), end='')
        print('\n')

def num_matches_vertical():
    ''' NoneType->int
Returns the number of pairs of cells with the same value adjacent to each other
vertically
'''
    num_matches=0
    
    for x in range(1,5):
        for y in range(1,4):
            if get_cell(x,y)==get_cell(x,y+1):
                num_matches=num_matches+1
    return num_matches

def num_matches_horizontal():
    ''' NoneType->int
Returns the number of pairs of cells with the same value adjacent to each other
horizontally
'''
    num_matches=0
    
    for x in range(1,4):
        for y in range(1,5):
            if get_cell(x,y)==get_cell(x+1,y):
                num_matches=num_matches+1
    return num_matches

def num_empty():
    '''NoneType->int
Returns the number of empty cells in the current state of game
'''
    num_empty=0
    for x in range(1,5):
        for y in range(1,5):
            if get_cell(x,y)==0:
                num_empty=num_empty+1
    return num_empty

def game_over():
    return (num_matches_vertical()==0)and(num_matches_horizontal()==0)and(num_empty()==0)

def game_won():
    '''
Returns True if and only if there is a '2048' cell on the field
'''
    game_won=False
    for x in range(1,5):
        for y in range(1,5):
            if get_cell(x,y)==2048:
                game_won=True
    return game_won

def up(x,y):
    return (x,y)

def down(x,y):
    return (x,5-y)

def right(x,y):
    return (5-y,x)

def left(x,y):
    return (y,x)


def move(fxfy):
    ''' NoneType->NoneType
Takes the current condition of game and makes the following changes:
- If there are cells with the same value (x) adjacent to each other vertically
merges them into one cell with value (2x)
- Moves all the cells with values up to the empty fields;

'''
    def set_cell_fxfy(x,y,value):
        (x,y)=fxfy(x,y)
        set_cell(x,y,value)
    def get_cell_fxfy(x,y):
        (x,y)=fxfy(x,y)
        return get_cell(x,y)
    def shift_all_up():
        for x in range(1,5):
            place=None
            for y in range(1,5):
                if (get_cell_fxfy(x,y)==0) and (place == None):
                    place=y
                elif (get_cell_fxfy(x,y) != 0) and (place !=None):
                    set_cell_fxfy(x,place,get_cell_fxfy(x,y))
                    set_cell_fxfy(x,y,0)
                    place=place+1
    def merge_up():
        for y in range(1,4):
                for x in range(1,5):
                    if get_cell_fxfy(x,y)==get_cell_fxfy(x,y+1):
                        set_cell_fxfy(x,y,get_cell_fxfy(x,y)*2)
                        set_cell_fxfy(x,y+1,0)
    shift_all_up()
    merge_up()
    shift_all_up()
