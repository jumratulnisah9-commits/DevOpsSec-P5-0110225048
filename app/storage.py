from app.tasks import create_task, complete_task


class TaskStorage:
    """Penyimpanan tugas sederhana selama aplikasi berjalan."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title):
        task = create_task(title, self._next_id)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task.copy()

    def list_all(self):
        return [task.copy() for task in self._tasks.values()]

    def complete(self, task_id):
        if task_id not in self._tasks:
            raise KeyError("Tugas tidak ditemukan.")

        self._tasks[task_id] = complete_task(
            self._tasks[task_id]
        )
        return self._tasks[task_id].copy()

    def delete(self, task_id):
        if task_id not in self._tasks:
            raise KeyError("Tugas tidak ditemukan.")

        del self._tasks[task_id]