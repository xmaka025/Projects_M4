from typing import Union


class Publication:
    def __init__(self, title: str, author: str, year: Union[int, str]) -> None:
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        return (f"Инофрмация:\nНазвание: {self.title},"
                f"\nАвтор: {self.author}, \nГод издания: {self.year}")


class Book(Publication):
    def __init__(self, genre: str, title: str, author: str, year: Union[int, str]) -> None:
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info},\nЖанр: {self.genre}"


class Magazine(Publication):
    def __init__(self, issue_number: str, title: str, author: str, year: Union[int, str]) -> None:
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info},\nНомер выпуска: {self.issue_number}"


class Newspaper(Publication):
    def __init__(self, publisher: str, title: str, author: str, year: Union[int, str]) -> None:
        super().__init__(title, author, year)
        self.publisher = publisher

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info},\nИздатель газеты: {self.publisher}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

obj1 = Book("Fantasy", "Harry Potter", "Jowan Rowling", '2009', )
print(obj1.get_info())
print()
obj2 = Magazine('734', 'Forbs', 'Steve Forbs', '1917')
print(obj2.get_info())
print()
obj3 = Newspaper('Larry Kramer', 'USA Today', 'Alen Harold', '1980')
print(obj3.get_info())
