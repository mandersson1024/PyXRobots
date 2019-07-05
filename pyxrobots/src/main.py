
from map import *
from ui import *
from main_menu import *
import undo


show_main_menu: bool = True

# if show_main_menu:
#     output.display(main_menu_text)

m = Map(30, 22)
# m.player_position = (2, 5)
# m.enemy_positions = [(1, 1), (8, 8)]
m.trash_piles = [(1, 3)]

m.player_position = (2, 0)
m.enemy_positions = [(0, 0)]

undo_history = undo.UndoHistory()

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


def is_quit_key(key: str) -> bool:
    return key == 'Escape'


def is_undo_key(key: str) -> bool:
    return key == 'Left'


def is_redo_key(key: str) -> bool:
    return key == 'Right'


def is_action_key(key: str) -> bool:
    return key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']


def on_keypress(key: str) -> None:
    print('key: ' + key)

    if is_quit_key(key):
        exit()

    elif is_undo_key(key):
        undo_history.undo()

    elif is_redo_key(key):
        undo_history.redo()

    elif is_action_key(key):
        old_player_position = m.player_position
        old_enemy_positions = m.enemy_positions.copy()
        old_trash_piles = m.trash_piles.copy()
        print('old_enemy_positions' + str(old_enemy_positions))

        move_player_according_to_keypress(key)
        m.move_all_enemies()

        new_player_position = m.player_position
        new_enemy_positions = m.enemy_positions.copy()
        new_trash_piles = m.trash_piles.copy()
        print('new_enemy_positions' + str(new_enemy_positions))

        def do_function() -> None:
            m.player_position = new_player_position
            m.enemy_positions = new_enemy_positions
            m.trash_piles = new_trash_piles

        def undo_function() -> None:
            m.player_position = old_player_position
            m.enemy_positions = old_enemy_positions
            m.trash_piles = old_trash_piles

        step = undo.Command(do_function, undo_function)
        undo_history.do(step)

    window_ui.display(m.map_string)


# TODO: Do 2 steps, undo 2 steps, redo 1 step.
# TODO: Enemies move 2 steps.

# TODO: Add class GameState with clone-function.

# TODO: Add ControlActions constants and return them from UI instead of keycodes.

window_ui = WindowUI(on_keypress)
window_ui.display(m.map_string)
window_ui.mainloop()

