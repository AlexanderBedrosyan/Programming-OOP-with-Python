from project.task import Task


class Section:

    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        task = ''
        if self.tasks:
            task = [obj for obj in self.tasks if obj.name == task_name][0]
        if task:
            task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for i in range(len(self.tasks) - 1, - 1, - 1):
            if self.tasks[i].completed:
                self.tasks.pop(i)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = [f'Section {self.name}:']
        for obj in self.tasks:
            result.append(obj.details())
        return '\n'.join(result)







