class Plant:

    def __init__(self, name: str, age: int, height: float):
        self._name = name
        self._age = age
        self._height = height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def grow(self) -> None:
        if (self._name == "Rose"):
            self._height += 0.2
        elif (self._name == "Sunflower"):
            self._height += 0.5
        elif (self._name == "Orchid"):
            self._height += 0.1
        else:
            self._height += 0.3

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose = Plant("Rose", 10, 15.0)
    rose.show()
    print("\n")
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-1)
    rose.set_age(-1)
    print("\n")
    print("Current state: ", end="")
    rose.show()
