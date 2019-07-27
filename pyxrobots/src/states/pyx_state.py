
from patterns.state_machine import State
from states.pyx_state_machine import PyxStateMachine


class PyxState(State):
    state_machine: PyxStateMachine

    def __init__(self):
        super().__init__()

    def render(self) -> str:
        return "PyxState"


