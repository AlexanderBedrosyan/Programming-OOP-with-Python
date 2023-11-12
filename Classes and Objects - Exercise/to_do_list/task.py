class Task:

    def __init__(self, name:str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def check_if_equal(self, parm1, parm2):
        return parm1 == parm2

    def change_name(self, new_name: str) -> str:
        if self.check_if_equal(new_name, self.name):
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str) -> str:
        if self.check_if_equal(self.due_date, new_date):
            return f"Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        try:
            self.comments[comment_number] = new_comment
            return ', '.join(str(ch) for ch in self.comments)
        except IndexError:
            return "Cannot find comment."

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"