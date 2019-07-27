
from ingame_data import *


def ingame_data_to_map_string(data: IngameData) -> str:
    s = ""

    for y in range(0, data.height - 1):
        for x in range(0, data.width - 1):
            if (x, y) == data.player:
                s += '@'
            elif (x, y) in data.enemies:
                s += '+'
            else:
                s += '·'
        s += '\n'

    s = s.strip("\n")
    return s


main_menu_text: str = '''
······························
······························
······························
······························
······························
······························
···                        ···
···       PyXRobots        ···
···                        ···
···     Numpad to move     ···
···     T - teleport       ···
···     B - blast          ···
···                        ···
···                        ···
···    Any key to start    ···
···                        ···
······························
······························
······························
······························
······························
······························
'''.strip()


