
from ui import *
from states.pyx_state_machine import PyxStateMachine


# def is_action_key(key: str) -> bool:
#     return key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']


window_ui = WindowUI()
state_machine = PyxStateMachine(window_ui)
state_machine.enter_state_main_menu()
window_ui.mainloop()

# window_ui.display(state_machine.current_state.render())
