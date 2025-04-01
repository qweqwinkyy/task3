class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "не выполнено"
        
    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]

    def mark_completed(self, task):
        if task in self.tasks:
            self.tasks[task] = "выполнено"
