from Models import Task, ListTask, TaskDataclass

class ViewModel:
    def __init__(self, listTask: ListTask) -> None:
        self._listTask = listTask
        self._tasks: list[Task] = self._listTask.get_tasks()

    def add_task(self, task: TaskDataclass):
        newTask = Task(task.title, task.description)
        self._listTask.add_task(newTask)
        self._tasks = self._listTask.get_tasks()
    
    def remove_task(self, task: Task):
        self._listTask.remove_task(task)
        self._tasks = self._listTask.get_tasks()

    def toggle_task(self, task: Task):
        task.toggle()
        self._tasks = self._listTask.get_tasks()

    def get_tasks(self):
        return self._tasks
