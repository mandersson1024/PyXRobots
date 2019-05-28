class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.player_position = (0, 0)

    def move_player(self, dx, dy):
        self.player_position = (self.player_position[0] + dx, self.player_position[1] + dy)

    def execute_player_action(self, key: str) -> None:
        if key == 'a':
            self.move_player(-1, 0)

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
