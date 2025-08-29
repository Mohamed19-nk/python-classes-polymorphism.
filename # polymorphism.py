# polymorphism.py

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Example usage
def show_movement(vehicle):
    print(vehicle.move())

if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        show_movement(v)

# Output:
# Driving 🚗
# Flying ✈️
# Sailing 🚢
