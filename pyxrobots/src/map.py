class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def map_string(self) -> str:
        s = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                s += '·'
            s += '\n'

        s = s.strip("\n")
        return s
