class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self) -> str:
        sorted_books = sorted(self.books)
        result = []
        for book in sorted_books:
            result.append(book)
        return ', '.join(result)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"