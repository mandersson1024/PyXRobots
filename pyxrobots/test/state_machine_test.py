import unittest
from patterns import state_machine


class StateMachineTestCase(unittest.TestCase):

    def test_creation(self):
        machine = state_machine.StateMachine()
        self.assertEqual(machine.current_state, machine.null_state)

    def test_state_changes(self):
        class TestState(state_machine.State):
            enter_was_called: bool = False
            exit_was_called: bool = False

            def enter(self):
                self.enter_was_called = True

            def exit(self):
                self.exit_was_called = True

        machine = state_machine.StateMachine()
        state1 = TestState()
        state2 = TestState()
        self.assertFalse(state1.enter_was_called)
        self.assertFalse(state1.exit_was_called)
        machine.enter_state(state1)
        self.assertTrue(state1.enter_was_called)
        self.assertFalse(state1.exit_was_called)
        machine.enter_state(state2)
        self.assertTrue(state1.exit_was_called)
        self.assertTrue(state2.enter_was_called)


if __name__ == '__main__':
    unittest.main()
