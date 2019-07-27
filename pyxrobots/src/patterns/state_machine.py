
class State:
    state_machine: 'StateMachine'

    def __init__(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass


class NullState(State):
    pass


class StateMachine:
    null_state: State
    current_state: State

    def __init__(self):
        self.null_state = NullState()
        self.current_state = self.null_state

    def enter_state(self, state: State):
        self.current_state.exit()
        self.current_state = state
        self.current_state.enter()

