# implementation of card game - Memory

import simplegui
import random


state = 0

# helper function to initialize globals
def new_game():
    global state, arr1, arr2, exposed, ind_cards, turns
    turns = 0
    ind_cards = [None]*2
    exposed = [False]*16
    state = 0
    arr1 = [random.randrange(0,8) for _ in range(8)]
    arr2 = arr1 + arr1
    random.shuffle(arr2)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, index, exposed, ind_cards, turns
    index = pos[0]/50
    if not exposed[index]:
        turns += 1
    exposed[index] = True
    if state == 0:
        ind_cards[0] = index
        state = 1
    elif state == 1:
        for i in range(2):
            if ind_cards[i] == None:
                ind_cards[i] = index
                break
        state = 2
    else:
        if arr2[ind_cards[0]] == arr2[ind_cards[1]]:
            ind_cards[1] = None
            ind_cards[0] = None
        else:
            exposed[ind_cards[0]] = False
            exposed[ind_cards[1]] = False
            ind_cards[1] = None
            ind_cards[0] = None
        for i in range(2):
            if ind_cards[i] == None:
                ind_cards[i] = index
                break
        state = 1
    print ind_cards
    print state
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global start_loc, exposed, label
    start_loc = 0
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(arr2[i]),(start_loc+18, 60), 30, 'white')
        else:
            canvas.draw_polygon([[start_loc, 0], [start_loc+50, 0], [start_loc+50,100], [start_loc, 100]],
                               1, 'red', 'green')
        start_loc = start_loc + 50
    if turns%2 == 0:
        label.set_text('Turns = '+str(turns/2))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
