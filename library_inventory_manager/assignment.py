
#book.py

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

    def to_line(self):
        return f"{self.title},{self.author},{self.isbn},{self.status}\n"

#libraryinventory.py

class LibraryInventory:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)

    def save_books(self):
        try:
            with open(self.filename, "w") as f:
                for book in self.books:
                    f.write(book.to_line())
        except Exception as e:
            print("Error saving file:", e)

    def load_books(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as f:
                for line in f:
                    self.books.append(Book.from_line(line))
        except Exception:
            print("File corrupted. Starting fresh.")
            self.books = []

#main.py 

def main():
    

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.issue():
                    inventory.save_books()
                    print("Book issued.")
                else:
                    print("Book already issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.return_book():
                    inventory.save_books()
                    print("Book returned.")
                else:
                    print("Book is not issued.")
            else:
                print("Book not found.")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("No matching books found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


