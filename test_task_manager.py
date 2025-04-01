import unittest
from task_manager import TaskManager, CompletedTasksDisplayStrategy, NotCompletedTasksDisplayStrategy

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

    def test_completed_tasks_display(self):
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.mark_completed("Задача 1")
        self.manager.set_display_strategy(CompletedTasksDisplayStrategy())
        completed_tasks = self.manager.display_tasks()
        self.assertEqual(len(completed_tasks), 1)
        self.assertIn("Задача 1", completed_tasks)

    def test_not_completed_tasks_display(self):
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.mark_completed("Задача 1")
        self.manager.set_display_strategy(NotCompletedTasksDisplayStrategy())
        not_completed_tasks = self.manager.display_tasks()
        self.assertEqual(len(not_completed_tasks), 1)
        self.assertIn("Задача 2", not_completed_tasks)

if __name__ == "__main__":
    unittest.main()
