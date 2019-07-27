
from keybinder import *
from patterns.state_machine import StateMachine
# from states.pyx_state import PyxState
from states.main_menu_state import MainMenuState
from states.ingame_state import IngameState
from states.game_over_state import GameOverState


class PyxStateMachine(StateMachine):
    current_state: 'PyxState'
    keybinder: Keybinder
    main_menu_state: 'MainMenuState'
    ingame_state: 'IngameState'
    game_over_state: 'GameOverState'

    def __init__(self, keybinder: Keybinder):
        super().__init__()
        self.keybinder = keybinder
        self.main_menu_state = MainMenuState()
        self.ingame_state = IngameState()
        self.game_over_state = GameOverState()

    def enter_main_menu_state(self) -> None:
        self.enter_state(self.main_menu_state)

    def enter_ingame_state(self) -> None:
        self.enter_state(self.ingame_state)

    def enter_game_over_state(self) -> None:
        self.enter_state(self.game_over_state)


