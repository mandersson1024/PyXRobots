
from ui import *
from states.pyx_state_machine import PyxStateMachine


window_ui = WindowUI()
state_machine = PyxStateMachine(window_ui)
state_machine.enter_state_main_menu()
window_ui.mainloop()

