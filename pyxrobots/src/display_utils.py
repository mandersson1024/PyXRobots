
from ingame_data import *


def ingame_data_to_map_string(data: IngameData) -> str:
    s = ''

    for y in range(data.height):
        for x in range(data.width):
            if (x, y) == data.player:
                s += '@'
            elif (x, y) in data.enemies:
                s += '+'
            elif (x, y) in data.trash_piles:
                s += '#'
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
···                        ···
···       PyXRobots        ···
···                        ···
···    <Numpad> to move    ···
···       B to blink       ···
···                        ···
···    <Enter> to start    ···
···                        ···
···                        ···
······························
······························
······························
······························
······························
······························
'''.strip()


game_over_text: str = '''
······························
······························
······························
······························
······························
······························
···                        ···
···                        ···
···                        ···
···       Game Over        ···
···                        ···
···                        ···
···   <Enter> to continue  ···
···                        ···
···                        ···
···                        ···
······························
······························
······························
······························
······························
······························
'''.strip()

level_complete_text: str = '''
······························
······························
······························
······························
······························
······························
···                        ···
···                        ···
···                        ···
···     Level Complete!    ···
···                        ···
···                        ···
···   <Enter> to continue  ···
···                        ···
···                        ···
···                        ···
······························
······························
······························
······························
······························
······························
'''.strip()
