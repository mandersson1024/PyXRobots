import unittest
import state_machine as sm


class StateMachineTestCase(unittest.TestCase):

    def test_creation(self):
        machine = sm.StateMachine()
        self.assertEqual(machine.currentState, machine.nullState)

    def test_state_changes(self):
        class TestState(sm.State):
            enter_was_called: bool = False
            exit_was_called: bool = False

            def enter(self):
                self.enter_was_called = True

            def exit(self):
                self.exit_was_called = True

        machine = sm.StateMachine()
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
