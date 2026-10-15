class Plant:
    def __init__(self, name: str, days_old: int, height: float) -> None:
        self.name = name
        self.days_old = days_old
        self.height = height

    def grow(self) -> None:
        if (self.name == "Rose"):
            self.height += 0.8
        elif (self.name == "Sunflower"):
            self.height += 0.5
        elif (self.name == "Orchid"):
            self.height += 0.1
        else:
            self.height += 0.3

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm,"
              f"{round(self.days_old, 2)} days old")


if __name__ == "__main__":

    def week_simulation(plant: Plant) -> None:
        plant.show()
        initial_height = plant.height
        for i in range(1, 8):
            plant.grow()
            plant.age()
            print(f"=== Day {i} ===")
            print(f"{plant.name}: {round(plant.height, 2)} cm,"
                  f"{round(plant.days_old, 2)} days old")
            i += 1
        result_height = plant.height - initial_height
        print(f"Growth this week: {round(result_height, 2)}cm")

    rose = Plant("Rose", 30, 25.0)
    orchid = Plant("Orchid", 11, 3)
    sunflower = Plant("Sunflower", 20, 7)
    violet = Plant("Violet", 9, 2)
    print("=== Garden Plant Growth ===")
    week_simulation(rose)
