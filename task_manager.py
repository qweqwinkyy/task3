class TaskDisplayStrategy:
    """Базовый класс стратегии отображения задач."""
    def display(self, tasks):
        raise NotImplementedError("Метод display должен быть реализован в подклассе.")

class CompletedTasksDisplayStrategy(TaskDisplayStrategy):
    """Стратегия отображения выполненных задач."""
    def display(self, tasks):
        return {task: status for task, status in tasks.items() if status == "выполнено"}

class NotCompletedTasksDisplayStrategy(TaskDisplayStrategy):
    """Стратегия отображения невыполненных задач."""
    def display(self, tasks):
        return {task: status for task, status in tasks.items() if status == "не выполнено"}

class TaskManager:
    """Менеджер задач с возможностью добавления, удаления и отображения задач."""
    
    def __init__(self):
        self.tasks = {}
        self.display_strategy = None

    def add_task(self, task):
        """Добавление задачи в список, если её ещё нет."""
        if task in self.tasks:
            raise ValueError(f"Задача '{task}' уже существует.")
        self.tasks[task] = "не выполнено"

    def remove_task(self, task):
        """Удаление задачи из списка."""
        if task not in self.tasks:
            raise ValueError(f"Задача '{task}' не найдена.")
        del self.tasks[task]

    def mark_completed(self, task):
        """Отметить задачу как выполненную."""
        if task not in self.tasks:
            raise ValueError(f"Задача '{task}' не найдена.")
        self.tasks[task] = "выполнено"

    def set_display_strategy(self, strategy):
        """Устанавливаем стратегию отображения задач."""
        if not isinstance(strategy, TaskDisplayStrategy):
            raise ValueError("Неверная стратегия отображения задач.")
        self.display_strategy = strategy

    def display_tasks(self):
        """Отображаем задачи в соответствии с текущей стратегией."""
        if self.display_strategy is None:
            raise ValueError("Не установлена стратегия отображения.")
        return self.display_strategy.display(self.tasks)
