class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
book1 = Book("Start with WHY", "Simon Sinek")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Pride and Prejudice", "Jane Austen")
print(book1)
print(book2)
print(book3)

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.card_number = []

    def borrow_books(self, book):
        self.borrowed_books.append(book)

    def add_card_nuimber(self, number):
        self.card_number.append(number)


    def member_fine(self, name, over_days ):
        fine = Member.calculate_fine(over_days, 2) #Access the static method by using the Member class name.
        print(f"{name}, fine for {over_days}, {fine}")


    def __str__(self):
        return f"Member: {self.name} Number:{[str(num) for num in self.card_number]} Borrowed books: {[str(book) for book in self.borrowed_books]} "

@staticmethod
def calculate_fine(over_due_days, fine_per_day):
    return over_due_days * fine_per_day

member1 = Member("Simon")
member2 = Member("Paulo")
member1.borrow_books(book1)
member2.borrow_books(book2)
member2.borrow_books(book3)

# print(f"{member1} fine is {member1.calculate_fine(3, 5)}")
# member1.add_card_nuimber(6474838289)


print(member2)
print(member1)

class Library:
    library = "Default library"
    total_books = 0

    def __init__(self, name):
        self.name = name
        self.book_object = []
        self.members_object = []

    def add_book(self, book):
        self.book_object.append(book)
        Library.total_books += 1

    def add_member(self, mem):
        self.members_object.append(mem)

    def __str__(self):
        return f"Library: {self.name} Books: {[str(book) for book in self.book_object]} Members: {[str(member) for member in self.members_object]}"   

library1 = Library("Lib_1")
book3 = Book("Title 3", "Author 3")
library1.add_book(book1)
library1.add_book(book3)
library1.add_member(member1)

print(library1)

