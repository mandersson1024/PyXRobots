
class Command:
    def __init__(self, execute_function: callable, undo_function: callable):
        self.execute_function = execute_function
        self.undo_function = undo_function

    def execute(self):
        self.execute_function()

    def undo(self):
        self.undo_function()


class UndoHistory:
    def __init__(self):
        self.undo_history: list = []
        self.redo_history: list = []

    def add(self, command: Command):
        self.undo_history.insert(0, command)

    def get_undo(self) -> Command:
        # todo: check for empty list
        command = self.undo_history.pop(0)
        self.redo_history.insert(0, command)
        return command

    def get_redo(self) -> Command:
        # todo: check for empty list
        command = self.redo_history.pop(0)
        self.undo_history.insert(0, command)
        return command
