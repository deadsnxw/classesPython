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

    def __str__(self):
        return f"'{self.name}' ({self.year}) in {self.city}, {self.country} with a capacity of {self.capacity}"

    def __eq__(self, other):
        if not isinstance(other, Stadion):
            return False
        return (self.name == other.name and
                self.year == other.year and
                self.country == other.country and
                self.city == other.city and
                self.capacity == other.capacity)

stadion1 = Stadion("Camp Nou", 1957, "Spain", "Barcelona", 99354)
print(stadion1)
stadion1.display_stadion()

stadion2 = Stadion("", "", "", "", "")
stadion2.add_stadion()
print(stadion2)
stadion2.display_stadion()

stadion3 = Stadion("Camp Nou", 1957, "Spain", "Barcelona", 99354)
print(stadion1 == stadion3)