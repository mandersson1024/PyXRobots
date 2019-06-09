
class Command:
    def __init__(self, execute_function: callable, undo_function: callable):
        self.execute_function: callable = execute_function
        self.undo_function: callable = undo_function

    def execute(self):
        self.execute_function()

    def undo(self):
        self.undo_function()


class CommandStack:
    def __init__(self):
        self.stack: list = []

    def push(self, command: Command):
        self.stack.insert(0, command)

    def pop(self) -> Command:
        # todo: check for empty list
        return self.stack.pop(0)

    @property
    def size(self) -> int:
        return len(self.stack)


class UndoHistory:
    def __init__(self):
        self.undo_history: CommandStack = CommandStack()
        self.redo_history: CommandStack = CommandStack()

    def do(self, command: Command):
        self.undo_history.push(command)
        command.execute()

    def undo(self) -> None:
        command: Command = self.undo_history.pop()
        self.redo_history.push(command)
        command.undo()

    def redo(self) -> None:
        command: Command = self.redo_history.pop()
        self.undo_history.push(command)
        command.execute()

    @property
    def num_undo_steps(self) -> int:
        return self.undo_history.size

    @property
    def num_redo_steps(self) -> int:
        return self.redo_history.size
