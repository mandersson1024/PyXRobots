
from ui import *
from states.pyx_state_machine import PyxStateMachine
from keybinder import Keybinder


# def is_action_key(key: str) -> bool:
#     return key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']


window_ui = WindowUI()


def bind_key(key: str, func: callable) -> None:
    window_ui.bind(key, func)


def unbind_key(key: str) -> None:
    window_ui.unbind(key)


keybinder = Keybinder(bind_key, unbind_key)

state_machine = PyxStateMachine(keybinder)
state_machine.enter_main_menu_state()

window_ui.display(state_machine.current_state.render())
window_ui.mainloop()




