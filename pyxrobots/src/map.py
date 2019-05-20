class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    @property
    def map_string(self):
        s = ""

        for y in range(0, self.height):
            for x in range(0, self.width):
                s += '·'
            s += '\n'

        s = s.strip("\n")
        return s
