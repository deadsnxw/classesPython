class Book:
    def __init__(self, name, year, author, publisher, genre, price):
        self.name = name
        self.year = year
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.price = price

    def add_book(self):
        self.name = input("Enter book name: ")
        self.year = input("Enter book year: ")
        self.author = input("Enter book author: ")
        self.publisher = input("Enter book publisher: ")
        self.genre = input("Enter book genre: ")
        self.price = input("Enter book price: ")


    def display_book(self):
        print("--------------------------")
        print(f"Book Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Price: {self.price}")
        print("--------------------------")

book1 = Book("The Great Gatsby", 1925, "F. Scott Fitzgerald", "Scribner", "Fiction", 10.99)
book1.display_book()

book2 = Book("", "", "", "", "", "")
book2.add_book()
book2.display_book()