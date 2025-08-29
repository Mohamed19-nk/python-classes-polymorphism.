# superhero.py

class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def show_identity(self):
        return f"{self.name} from {self.universe} uses {self.power}!"

# Inheritance example
class Villain(Superhero):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)
        self.evil_plan = evil_plan

    def show_identity(self):
        return f"{self.name} is a villain from {self.universe} planning to {self.evil_plan}!"

# Example usage
if __name__ == "__main__":
    hero = Superhero("Spider-Man", "Web-slinging", "Marvel")
    villain = Villain("Joker", "Chaos", "DC", "destroy Gotham")

    print(hero.show_identity())     # Output: Spider-Man from Marvel uses Web-slinging!
    print(villain.show_identity())  # Output: Joker is a villain from DC planning to destroy Gotham!
