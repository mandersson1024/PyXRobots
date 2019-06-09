import unittest
import undo


class CommandTestCase(unittest.TestCase):

    def test_execute_undo(self):
        self.counter: int = 0
        def add_one(): self.counter = self.counter + 1
        def subtract_one(): self.counter = self.counter - 1
        self.addOneCommand = undo.Command(add_one, subtract_one)
        self.assertEqual(self.counter, 0)
        self.addOneCommand.execute()
        self.assertEqual(self.counter, 1)
        self.addOneCommand.undo()
        self.assertEqual(self.counter, 0)


class UndoHistoryTestCase(unittest.TestCase):

    def test_empty(self):
        self.history = undo.UndoHistory()
        self.assertEqual(self.history.num_undo_steps, 0)
        self.assertEqual(self.history.num_redo_steps, 0)

    def test_undo_redo_queue_sizes(self):
        self.history = undo.UndoHistory()
        self.history.do(undo.Command(lambda: None, lambda: None))
        self.assertEqual(self.history.num_undo_steps, 1)
        self.assertEqual(self.history.num_redo_steps, 0)
        self.history.undo()
        self.assertEqual(self.history.num_undo_steps, 0)
        self.assertEqual(self.history.num_redo_steps, 1)
        self.history.redo()
        self.assertEqual(self.history.num_undo_steps, 1)
        self.assertEqual(self.history.num_redo_steps, 0)

    def test_execute_undo(self):
        self.history = undo.UndoHistory()
        self.counter: int = 0
        def add_one(): self.counter = self.counter + 1
        def subtract_one(): self.counter = self.counter - 1
        self.command = undo.Command(add_one, subtract_one)
        self.history.do(self.command)
        self.assertEqual(self.counter, 1)
        self.history.undo()
        self.assertEqual(self.counter, 0)
        self.history.redo()
        self.assertEqual(self.counter, 1)


if __name__ == '__main__':
    unittest.main()
