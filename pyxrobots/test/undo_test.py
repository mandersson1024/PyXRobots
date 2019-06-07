import unittest
import undo


class UndoTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.uh = undo.UndoHistory()

    def test_empty(self):
        self.assertEqual(self.uh.num_undo_steps, 0)
        self.assertEqual(self.uh.num_redo_steps, 0)


if __name__ == '__main__':
    unittest.main()
