class Book:
    def __init__(self, author: str, title: str, rating: int, read_date: str):
        self.author = author
        self.title = title
        
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Рейтинг должен быть числом от 1 до 5 (включительно).")
        self.rating = rating
        
        self.read_date = read_date

    def __repr__(self):
        return f"Книга(author='{self.author}', title='{self.title}', rating={self.rating}, read_date='{self.read_date}')"
