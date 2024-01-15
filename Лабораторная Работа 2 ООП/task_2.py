BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# Определение класса Book
class Book:
    # Метод __str__ возвращает строку, представляющую объект книги
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    # Метод __str__
    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    # Метод __repr__
    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    # Конструктор класса, который инициализирует атрибут books
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    # Метод, возвращающий идентификатор для добавления новой книги в библиотеку
    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    # Метод, возвращающий индекс книги в списке
    def get_index_by_book_id(self, id_):
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
