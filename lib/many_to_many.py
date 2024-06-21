class Author:
    class Author:
     all_authors = []

    def _init_(self, name):
        self.name = name
        self.contracts_list = []
        self.books_list = []
        self.all_authors.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        new_contract = Contract(self, book, date, royalties)
        self.contracts_list.append(new_contract)
        return new_contract

    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts_list)
        return total


class Book:
    def _init_(self, title):
        self.title = title


class Contract:
    all_contracts = []

    def _init_(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]