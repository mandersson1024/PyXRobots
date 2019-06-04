import math


def sign(x: int) -> int:
    if x == 0:
        return 0
    else:
        return int(math.copysign(1, x))

