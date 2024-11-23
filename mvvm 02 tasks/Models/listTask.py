class ListTask:
    def __init__(self) -> None:
        self._tasks = []
    
    def add_task(self, task):
        self._tasks.append(task)

    def remove_task(self, task):
        self._tasks.remove(task)

    def get_tasks(self):
        return self._tasks