class TaskManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.tasks = {}
            self.initialized = True
        self.display_strategy = AllTasksDisplayStrategy()

    def _check_task_exists(self, task):
        if task not in self.tasks:
            raise ValueError(f"Задача '{task}' не найдена.")

    def add_task(self, task):
        if task in self.tasks:
            raise ValueError(f"Задача '{task}' уже существует.")
        self.tasks[task] = "не выполнено"

    def remove_task(self, task):
        self._check_task_exists(task)
        del self.tasks[task]

    def mark_completed(self, task):
        self._check_task_exists(task)
        self.tasks[task] = "выполнено"

    def display_tasks(self):
        return self.display_strategy.display(self.tasks)
