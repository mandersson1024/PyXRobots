
from keybinder import *
from patterns.state_machine import *
from ingame_data import *


class PyxState(State):
    state_machine: 'PyxStateMachine'

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__()
        self.state_machine = state_machine

    def render(self) -> str:
        return "PyxState"


class MainMenuState(PyxState):

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)

    def enter(self) -> None:
        print('entering ' + self.__class__.__name__)

        def on_return(_) -> None:
            self.state_machine.enter_ingame_state()

        self.state_machine.keybinder.bind('<Return>', on_return)

    def exit(self) -> None:
        print('exiting ' + self.__class__.__name__)
        self.state_machine.keybinder.unbind('<Return>')

    def render(self) -> str:
        return "MainMenuState"


class IngameState(PyxState):
    data: IngameData

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)
        self.data = IngameData()
        self.data.player = (2, 0)
        self.data.enemies = [(0, 0)]

    def enter(self):
        print('entering ' + self.__class__.__name__)

    def exit(self):
        print('exiting ' + self.__class__.__name__)

    def update(self):
        # ingame_data.move_player_according_to_keypress(key)
        # ingame_data.move_all_enemies()
        pass

    def render(self) -> str:
        return "IngameState"
        # window_ui.display(m.map_string)


class GameOverState(PyxState):

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)

    def enter(self):
        print('entering ' + self.__class__.__name__)

    def exit(self):
        print('exiting ' + self.__class__.__name__)

    def render(self) -> str:
        return "GameOverState"


class PyxStateMachine(StateMachine):
    current_state: PyxState
    keybinder: Keybinder
    main_menu_state: MainMenuState
    ingame_state: IngameState
    game_over_state: GameOverState

    def __init__(self, keybinder: Keybinder):
        super().__init__()
        self.keybinder = keybinder
        self.main_menu_state = MainMenuState(self)
        self.ingame_state = IngameState(self)
        self.game_over_state = GameOverState(self)

    def enter_main_menu_state(self) -> None:
        self.enter_state(self.main_menu_state)

    def enter_ingame_state(self) -> None:
        self.enter_state(self.ingame_state)

    def enter_game_over_state(self) -> None:
        self.enter_state(self.game_over_state)


