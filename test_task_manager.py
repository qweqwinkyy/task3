import unittest
from task_manager import TaskManager, CompletedTasksDisplayStrategy, NotCompletedTasksDisplayStrategy

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        """Перед каждым тестом очищаем задачи."""
        self.manager = TaskManager()
        self.manager.tasks.clear()  # Очистить задачи перед каждым тестом

    def test_add_task(self):
        """Тестируем добавление задачи."""
        self.manager.add_task("Выучить TDD")
        self.assertIn("Выучить TDD", self.manager.tasks)

    def test_remove_task(self):
        """Тестируем удаление задачи."""
        self.manager.add_task("Выучить TDD")
        self.manager.remove_task("Выучить TDD")
        self.assertNotIn("Выучить TDD", self.manager.tasks)

    def test_task_status(self):
        """Тестируем изменение статуса задачи."""
        self.manager.add_task("Выучить TDD")
        self.manager.mark_completed("Выучить TDD")
        self.assertEqual(self.manager.tasks["Выучить TDD"], "выполнено")

    def test_completed_tasks_display(self):
        """Тестируем отображение выполненных задач."""
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.mark_completed("Задача 1")
        self.manager.set_display_strategy(CompletedTasksDisplayStrategy())
        completed_tasks = self.manager.display_tasks()
        self.assertEqual(len(completed_tasks), 1)
        self.assertIn("Задача 1", completed_tasks)

    def test_not_completed_tasks_display(self):
        """Тестируем отображение невыполненных задач."""
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.mark_completed("Задача 1")
        self.manager.set_display_strategy(NotCompletedTasksDisplayStrategy())
        not_completed_tasks = self.manager.display_tasks()
        self.assertEqual(len(not_completed_tasks), 1)
        self.assertIn("Задача 2", not_completed_tasks)

    def test_add_duplicate_task(self):
        """Тестируем добавление дублирующейся задачи."""
        self.manager.add_task("Задача 1")
        with self.assertRaises(ValueError):
            self.manager.add_task("Задача 1")  # Попытка добавить дубликат

    def test_remove_non_existing_task(self):
        """Тестируем удаление несуществующей задачи."""
        with self.assertRaises(ValueError):
            self.manager.remove_task("Не существующая задача")  # Задача не существует

    def test_mark_completed_non_existing_task(self):
        """Тестируем отметку выполненной несуществующей задачи."""
        with self.assertRaises(ValueError):
            self.manager.mark_completed("Не существующая задача")  # Задача не существует

if __name__ == "__main__":
    unittest.main()
