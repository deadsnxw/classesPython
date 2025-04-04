class Car:
    def __init__(self, name, year, make, engine, color):
        self.name = name
        self.year = year
        self.make = make
        self.engine = engine
        self.color = color

    def add_car(self):
        self.name = input("Enter car name: ")
        self.year = input("Enter car year: ")
        self.make = input("Enter car make: ")
        self.engine = input("Enter car engine: ")
        self.color = input("Enter car color: ")

    def display_car(self):
        print("--------------------------")
        print(f"Car Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Engine: {self.engine}")
        print(f"Color: {self.color}")
        print("--------------------------")

car1 = Car("Toyota", 2020, "Corolla", "1.8L", "Blue")
car1.display_car()

car2 = Car("", "", "", "", "")
car2.add_car()
car2.display_car()