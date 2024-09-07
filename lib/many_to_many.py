class Author:
    all=[]
    def __init__(self, name):
        self.name=name
        Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    def books(self):
        return [book.book for book in Contract.all if book.author==self]
    def sign_contract(self, book, date, royalties):
        for contract in Contract.all:
            if contract.author==self and contract.book==book:
                raise Exception("Contract already exists for this book and author.")
        new_contract=Contract(self, book, date, royalties)
        return new_contract
    def total_royalties(self):
        sum_of_royalties=0
        for contract in Contract.all:
            if contract.author==self:
                sum_of_royalties+=contract.royalties
        return sum_of_royalties

class Book:
    all=[]
    def __init__(self, title):
        self.title=title
        Book.all.append(self)
    def contracts(self):
        return [book_contract for book_contract in Contract.all if book_contract.book==self]
    def authors(self):
        return [book.author for book in Contract.all if book.book==self]
    
class Contract:
    all=[]
    def __init__(self, author, book, date, royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author=author
        else:
            raise Exception("Author should be an instance of the Author class.")
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book=book
        else:
            raise Exception("Book must be an instance of the Book class.")
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date=date
        else:
            raise Exception("Date must be a string!")
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties=royalties
        else:
            raise Exception("Royalties should be of int!")
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date==date]

