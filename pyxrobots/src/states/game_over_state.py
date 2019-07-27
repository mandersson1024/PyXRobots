
from states.pyx_state import *
from keybinder import *


class GameOverState(PyxState):

    def __init__(self):
        super().__init__()

    def enter(self):
        print('entering ' + self.__class__.__name__)

    def exit(self):
        print('exiting ' + self.__class__.__name__)

    def render(self) -> str:
        return "GameOverState"
