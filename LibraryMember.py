class LibraryMember:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def borrow_book(self, other, number):
            self.books -= number
            other.books += number 
            print(self.name, "gave", number, "books to", other.name)
        

member1 = LibraryMember("Alice", 8)
member2 = LibraryMember("Bob", 3)

member1.borrow_book(member2, 2)

print(member1.name, "has", member1.books, "books")
print(member2.name, "has", member2.books, "books")