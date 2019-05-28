class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.player_position = (0, 0)

    def player_move(self, dx, dy):
        self.player_position = (self.player_position[0] + dx, self.player_position[1] + dy)

    def player_move_up_left(self):
        self.player_move(-1, -1)

    def player_move_up(self):
        self.player_move(0, -1)

    def player_move_up_right(self):
        self.player_move(1, -1)

    def player_move_left(self):
        self.player_move(-1, 0)

    def player_dont_move(self):
        self.player_move(0, 0)

    def player_move_right(self):
        self.player_move(1, 0)

    def player_move_down_left(self):
        self.player_move(-1, 1)

    def player_move_down(self):
        self.player_move(0, 1)

    def player_move_down_right(self):
        self.player_move(1, 1)

    def execute_player_action(self, key: str) -> None:
        if key == 'q':
            self.player_move_up_left()
        elif key == 'w':
            self.player_move_up()
        if key == 'e':
            self.player_move_up_right()
        elif key == 'a':
            self.player_move_left()
        elif key == 's':
            self.player_dont_move()
        if key == 'd':
            self.player_move_right()
        elif key == 'z':
            self.player_move_down_left()
        if key == 'x':
            self.player_move_down()
        elif key == 'c':
            self.player_move_down_right()

    @property
    def map_string(self) -> str:
        s = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                if (x, y) == self.player_position:
                    s += '@'
                else:
                    s += '·'
            s += '\n'

        s = s.strip("\n")
        return s
