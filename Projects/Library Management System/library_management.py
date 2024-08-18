class Library:
    def __init__(self, name):
        self.name = name
        self.books = [
            "It Ends with Us",
            "Harry Potter and the Goblet of Fire",
            "Cosmos",
            "The Hunger Games",
            "The Girl on the Train"
        ]
        self.number = len(self.books)

    def show_book_num(self):
        print(f"There are a total of {self.number} books in '{self.name}'.")

    def add_book(self, book):
        self.books.append(book)
        self.number = len(self.books)
        print(f"Book: '{book}' added.")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"- {book}")

    def menu(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Show number of books")
            print("2. Display names of books")
            print("3. Add a new book")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.show_book_num()
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                book = input("Enter the name of the book to add: ")
                self.add_book(book)
            elif choice == '4':
                print("Exiting the library system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

library = Library("My Library")
library.menu()
