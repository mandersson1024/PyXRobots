
from map import *
from ui import *
from main_menu import *


show_main_menu: bool = True

# if show_main_menu:
#     output.display(main_menu_text)

m = Map(30, 22)
m.player_position = (2, 5)
m.enemy_positions = [(1, 1), (8, 8)]
m.trash_piles = [(1, 3)]

keys_up_left = ['q', '7']
keys_up = ['w', '8']
keys_up_right = ['e', '9']
keys_left = ['a', '4']
keys_pass = ['s', '5']
keys_right = ['d', '6']
keys_down_left = ['z', '1']
keys_down = ['x', '2']
keys_down_right = ['c', '3']


def move_player_according_to_keypress(key: str) -> None:
    if key in keys_up_left:
        m.player_move_up_left()
    elif key in keys_up:
        m.player_move_up()
    if key in keys_up_right:
        m.player_move_up_right()
    elif key in keys_left:
        m.player_move_left()
    elif key in keys_pass:
        m.player_dont_move()
    if key in keys_right:
        m.player_move_right()
    elif key in keys_down_left:
        m.player_move_down_left()
    if key in keys_down:
        m.player_move_down()
    elif key in keys_down_right:
        m.player_move_down_right()


def on_keypress(key):
    print('key: ' + key)
    move_player_according_to_keypress(key)
    m.move_all_enemies()
    window_ui.display(m.map_string)


def end_application(_):
    exit()


window_ui = WindowUI(on_keypress)
window_ui.bind('<Escape>', end_application)
window_ui.display(m.map_string)
window_ui.mainloop()

