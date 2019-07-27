
class State:
    def __init__(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass


class NullState(State):
    pass


class StateMachine:
    nullState: State
    currentState: State

    def __init__(self):
        self.nullState = NullState()
        self.currentState = self.nullState

    def enter_state(self, state: State):
        self.currentState.exit()
        self.currentState = state
        self.currentState.enter()

