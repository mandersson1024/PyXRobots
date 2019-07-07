
from map import *
from ui import *
from main_menu import *
import undo


show_main_menu: bool = True

# if show_main_menu:
#     output.display(main_menu_text)
game_state = GameState(30, 22)
game_state.player = (2, 0)
game_state.enemies = [(0, 0)]

m = Map()
m.state = game_state

undo_history = undo.UndoHistory()


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
        old_state = m.state.clone()
        new_state = m.state.clone()

        new_state.move_player_according_to_keypress(key)
        new_state.move_all_enemies()

        def do_function() -> None:
            m.state = new_state

        def undo_function() -> None:
            m.state = old_state

        step = undo.Command(do_function, undo_function)
        undo_history.do(step)

    window_ui.display(m.map_string)


# TODO: Add ControlActions constants and return them from UI instead of keycodes.

window_ui = WindowUI(on_keypress)
window_ui.display(m.map_string)
window_ui.mainloop()

