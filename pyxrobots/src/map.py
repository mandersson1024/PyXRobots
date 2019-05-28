class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.player_position = (0, 0)

    def move_player(self, dx, dy):
        self.player_position = (self.player_position[0] + dx, self.player_position[1] + dy)

    def execute_player_action(self, key: str) -> None:
        if key == 'q':
            self.move_player(-1, -1)
        elif key == 'w':
            self.move_player(0, -1)
        if key == 'e':
            self.move_player(1, -1)
        elif key == 'a':
            self.move_player(-1, 0)
        if key == 'd':
            self.move_player(1, 0)
        elif key == 'z':
            self.move_player(-1, 1)
        if key == 'x':
            self.move_player(0, 1)
        elif key == 'c':
            self.move_player(1, 1)

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
