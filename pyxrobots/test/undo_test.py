import unittest
import undo


class CommandTestCase(unittest.TestCase):

    def test_execute_undo(self):
        self.counter: int = 0
        def add_one(): self.counter = self.counter + 1
        def subtract_one(): self.counter = self.counter - 1
        add_one_command = undo.Command(add_one, subtract_one)
        self.assertEqual(self.counter, 0)
        add_one_command.execute()
        self.assertEqual(self.counter, 1)
        add_one_command.undo()
        self.assertEqual(self.counter, 0)


class UndoHistoryTestCase(unittest.TestCase):

    def test_empty(self):
        history = undo.UndoHistory()
        self.assertEqual(history.num_undo_steps, 0)
        self.assertEqual(history.num_redo_steps, 0)

    def test_undo_redo_queue_sizes(self):
        history = undo.UndoHistory()
        history.do(undo.Command(lambda: None, lambda: None))
        self.assertEqual(history.num_undo_steps, 1)
        self.assertEqual(history.num_redo_steps, 0)
        history.undo()
        self.assertEqual(history.num_undo_steps, 0)
        self.assertEqual(history.num_redo_steps, 1)
        history.redo()
        self.assertEqual(history.num_undo_steps, 1)
        self.assertEqual(history.num_redo_steps, 0)

    def test_clear_redo_stack_after_undo_do(self):
        history = undo.UndoHistory()
        history.do(undo.Command(lambda: None, lambda: None))
        history.do(undo.Command(lambda: None, lambda: None))
        history.undo()
        history.undo()
        self.assertEqual(history.num_undo_steps, 0)
        self.assertEqual(history.num_redo_steps, 2)
        history.do(undo.Command(lambda: None, lambda: None))
        self.assertEqual(history.num_undo_steps, 1)
        self.assertEqual(history.num_redo_steps, 0)

    def test_do_undo(self):
        history = undo.UndoHistory()
        self.counter: int = 0
        def add_one(): self.counter = self.counter + 1
        def subtract_one(): self.counter = self.counter - 1
        command = undo.Command(add_one, subtract_one)
        history.do(command)
        self.assertEqual(self.counter, 1)
        history.do(command)
        self.assertEqual(self.counter, 2)
        history.undo()
        self.assertEqual(self.counter, 1)
        history.undo()
        self.assertEqual(self.counter, 0)
        history.redo()
        self.assertEqual(self.counter, 1)
        history.redo()
        self.assertEqual(self.counter, 2)


if __name__ == '__main__':
    unittest.main()
