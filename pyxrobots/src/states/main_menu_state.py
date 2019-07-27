
from states.pyx_state import PyxState


class MainMenuState(PyxState):

    def __init__(self):
        super().__init__()

    def enter(self):
        print('entering ' + self.__class__.__name__)
        self.state_machine.keybinder.bind('<Enter>', self.state_machine.enter_ingame_state)

    def exit(self):
        print('exiting ' + self.__class__.__name__)

    def render(self) -> str:
        return "MainMenuState"
