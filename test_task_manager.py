import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Выучить TDD")
        self.assertIn("Выучить TDD", self.manager.tasks)

    def test_remove_task(self):
        self.manager.add_task("Выучить TDD")
        self.manager.remove_task("Выучить TDD")
        self.assertNotIn("Выучить TDD", self.manager.tasks)

    def test_task_status(self):
        self.manager.add_task("Выучить TDD")
        self.manager.mark_completed("Выучить TDD")
        self.assertEqual(self.manager.tasks["Выучить TDD"], "выполнено")

if __name__ == "__main__":
    unittest.main()
