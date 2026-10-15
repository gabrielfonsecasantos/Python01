class Plant:
    def __init__(self, name: str, days_old: int, height: float) -> None:
        self.name = name
        self.days_old = days_old
        self.height = height

    def grow(self) -> None:
        if (self.name == "Rose"):
            self.height += 0.2
        elif (self.name == "Sunflower"):
            self.height += 0.5
        elif (self.name == "Orchid"):
            self.height += 0.1
        else:
            self.height += 0.3

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant_list = [
        Plant("Rose", 30, 25.0),
        Plant("Oak", 365, 200.0),
        Plant("Cactus", 90, 5.0),
        Plant("Sunflower", 45, 80.0),
        Plant("Fern", 120, 15.0)
    ]

    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print("Created: ", end="")
        plant.show()
