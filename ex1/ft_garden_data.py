class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant_list = [
        Plant("Rose", 30, 10),
        Plant("Sunflower", 30, 10),
        Plant("Orchid", 30, 10)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plant_list:
        plant.show()
