
class Keybinder:
    bind_func: callable
    unbind_func: callable

    def __init__(self, bind_func: callable, unbind_func: callable):
        self.bind_func = bind_func
        self.unbind_func = unbind_func

    def bind(self, key: str, func: callable) -> None:
        self.bind_func(key, func)

    def unbind(self, key: str) -> None:
        self.unbind_func(key)

