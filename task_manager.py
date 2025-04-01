class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        """Добавляет задачу в список с состоянием 'не выполнено'."""
        if task not in self.tasks:
            self.tasks[task] = "не выполнено"
        else:
            print(f"Задача '{task}' уже существует.")

    def remove_task(self, task):
        """Удаляет задачу, если она существует. Иначе выводит сообщение об ошибке."""
        if task in self.tasks:
            del self.tasks[task]
        else:
            print(f"Задача '{task}' не найдена.")

    def mark_completed(self, task):
        """Меняет статус задачи на 'выполнено', если задача существует."""
        if task in self.tasks:
            self.tasks[task] = "выполнено"
        else:
            print(f"Задача '{task}' не найдена.")
