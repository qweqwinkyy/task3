import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Создает объект TaskManager перед каждым тестом."""
        self.manager = TaskManager()

    def test_add_task(self):
        """Тестирует добавление задачи."""
        self.manager.add_task("Выучить TDD")
        self.assertIn("Выучить TDD", self.manager.tasks)

    def test_add_duplicate_task(self):
        """Тестирует добавление повторяющейся задачи."""
        self.manager.add_task("Выучить TDD")
        self.manager.add_task("Выучить TDD")  # Попытка добавить дубликат
        self.assertEqual(len(self.manager.tasks), 1)  # Задача не должна повторяться

    def test_remove_task(self):
        """Тестирует удаление задачи."""
        self.manager.add_task("Выучить TDD")
        self.manager.remove_task("Выучить TDD")
        self.assertNotIn("Выучить TDD", self.manager.tasks)

    def test_remove_non_existing_task(self):
        """Тестирует удаление несуществующей задачи."""
        self.manager.remove_task("Выучить TDD")  # Попытка удалить несуществующую задачу
        self.assertNotIn("Выучить TDD", self.manager.tasks)

    def test_task_status(self):
        """Тестирует изменение статуса задачи на выполнено."""
        self.manager.add_task("Выучить TDD")
        self.manager.mark_completed("Выучить TDD")
        self.assertEqual(self.manager.tasks["Выучить TDD"], "выполнено")

    def test_mark_completed_for_non_existing_task(self):
        """Тестирует попытку отметить как выполненную несуществующую задачу."""
        self.manager.mark_completed("Выучить TDD")
        self.assertNotIn("Выучить TDD", self.manager.tasks)

if __name__ == "__main__":
    unittest.main()
