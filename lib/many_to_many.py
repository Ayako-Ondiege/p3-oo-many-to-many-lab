class Author:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name must be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
        
    def __str__(self):
        return f"Author(name='{self.name}')"
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author == self)
    


class Book:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("title must be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

    def __str__(self):
        return f"Book(title='{self.title}')"

from datetime import datetime

class Contract:

    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value 

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date =value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number (int or float)")
        self._royalties = value

    def __str__(self):
            return f"Contract(author={self.author.name}, book={self.book.title}, royalties={self.royalties})"

    @classmethod
    def contracts_by_date(cls, target_date):
        return [contract for contract in cls.all if contract.date == target_date]
    
    


