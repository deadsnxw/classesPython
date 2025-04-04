class Stadion:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def add_stadion(self):
        self.name = input("Enter stadium name: ")
        self.year = input("Enter stadium year: ")
        self.country = input("Enter stadium country: ")
        self.city = input("Enter stadium city: ")
        self.capacity = input("Enter stadium capacity: ")

    def display_stadion(self):
        print("--------------------------")
        print(f"Stadium Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")
        print("--------------------------")

stadion1 = Stadion("Camp Nou", 1957, "Spain", "Barcelona", 99354)
stadion1.display_stadion()

stadion2 = Stadion("", "", "", "", "")
stadion2.add_stadion()
stadion2.display_stadion()