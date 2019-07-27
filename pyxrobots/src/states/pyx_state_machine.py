
from ui import *
from patterns.state_machine import *
from display_utils import *


class PyxState(State):
    state_machine: 'PyxStateMachine'

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__()
        self.state_machine = state_machine

    def render(self) -> None:
        self.state_machine.ui.display("Not implemented")


class MainMenuState(PyxState):

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)

    def enter(self) -> None:
        print('entering ' + self.__class__.__name__)
        self.state_machine.ui.bind_key('<Return>', self.state_machine.enter_ingame_state)
        self.render()

    def exit(self) -> None:
        print('exiting ' + self.__class__.__name__)
        self.state_machine.ui.unbind_key('<Return>')

    def render(self) -> None:
        self.state_machine.ui.display(main_menu_text)


class IngameState(PyxState):
    data: IngameData

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)

    def get_move_command(self, move_func: callable) -> callable:
        def move_command() -> None:
            move_func()
            self.data.move_all_enemies()
            dead = self.data.check_for_death()
            if dead:
                self.state_machine.enter_game_over_state()
            else:
                self.render()
        return move_command

    def enter(self) -> None:
        print('entering ' + self.__class__.__name__)

        self.data = IngameData()
        self.data.player = (2, 0)
        self.data.enemies = [(0, 0)]

        self.state_machine.ui.bind_key('q', self.get_move_command(self.data.player_move_up_left))
        self.state_machine.ui.bind_key('7', self.get_move_command(self.data.player_move_up_left))
        self.state_machine.ui.bind_key('w', self.get_move_command(self.data.player_move_up))
        self.state_machine.ui.bind_key('8', self.get_move_command(self.data.player_move_up))
        self.state_machine.ui.bind_key('e', self.get_move_command(self.data.player_move_up_right))
        self.state_machine.ui.bind_key('9', self.get_move_command(self.data.player_move_up_right))
        self.state_machine.ui.bind_key('a', self.get_move_command(self.data.player_move_left))
        self.state_machine.ui.bind_key('4', self.get_move_command(self.data.player_move_left))
        self.state_machine.ui.bind_key('a', self.get_move_command(self.data.player_dont_move))
        self.state_machine.ui.bind_key('5', self.get_move_command(self.data.player_dont_move))
        self.state_machine.ui.bind_key('d', self.get_move_command(self.data.player_move_right))
        self.state_machine.ui.bind_key('6', self.get_move_command(self.data.player_move_right))
        self.state_machine.ui.bind_key('z', self.get_move_command(self.data.player_move_down_left))
        self.state_machine.ui.bind_key('1', self.get_move_command(self.data.player_move_down_left))
        self.state_machine.ui.bind_key('x', self.get_move_command(self.data.player_move_down))
        self.state_machine.ui.bind_key('2', self.get_move_command(self.data.player_move_down))
        self.state_machine.ui.bind_key('c', self.get_move_command(self.data.player_move_down_right))
        self.state_machine.ui.bind_key('3', self.get_move_command(self.data.player_move_down_right))
        self.render()

    def exit(self):
        print('exiting ' + self.__class__.__name__)
        self.state_machine.ui.unbind_key('q')
        self.state_machine.ui.unbind_key('7')
        self.state_machine.ui.unbind_key('w')
        self.state_machine.ui.unbind_key('8')
        self.state_machine.ui.unbind_key('e')
        self.state_machine.ui.unbind_key('9')
        self.state_machine.ui.unbind_key('a')
        self.state_machine.ui.unbind_key('4')
        self.state_machine.ui.unbind_key('a')
        self.state_machine.ui.unbind_key('5')
        self.state_machine.ui.unbind_key('d')
        self.state_machine.ui.unbind_key('6')
        self.state_machine.ui.unbind_key('z')
        self.state_machine.ui.unbind_key('1')
        self.state_machine.ui.unbind_key('x')
        self.state_machine.ui.unbind_key('2')
        self.state_machine.ui.unbind_key('c')
        self.state_machine.ui.unbind_key('3')

    def data_to_string(self) -> str:
        s = ''

        for y in range(0, self.data.height):
            for x in range(0, self.data.width):
                if (x, y) == self.data.player:
                    s += '@'
                elif (x, y) in self.data.enemies:
                    s += '+'
                else:
                    s += '·'
            s += '\n'

        s = s.strip("\n")
        return s

    def render(self) -> None:
        self.state_machine.ui.display(self.data_to_string())


class GameOverState(PyxState):

    def __init__(self, state_machine: 'PyxStateMachine'):
        super().__init__(state_machine)

    def enter(self):
        print('entering ' + self.__class__.__name__)
        self.state_machine.ui.bind_key('<Return>', self.state_machine.enter_main_menu_state)
        self.render()

    def exit(self):
        print('exiting ' + self.__class__.__name__)
        self.state_machine.ui.unbind_key('<Return>')

    def render(self) -> None:
        self.state_machine.ui.display(game_over_text)


class PyxStateMachine(StateMachine):
    ui: WindowUI
    current_state: PyxState
    main_menu_state: MainMenuState
    ingame_state: IngameState
    game_over_state: GameOverState

    def __init__(self, ui: WindowUI):
        super().__init__()
        self.ui = ui
        self.main_menu_state = MainMenuState(self)
        self.ingame_state = IngameState(self)
        self.game_over_state = GameOverState(self)

    def enter_main_menu_state(self) -> None:
        self.enter_state(self.main_menu_state)

    def enter_ingame_state(self) -> None:
        self.enter_state(self.ingame_state)

    def enter_game_over_state(self) -> None:
        self.enter_state(self.game_over_state)


