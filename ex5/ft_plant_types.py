class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height, is_init=True)
        self.set_age(age, is_init=True)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float, is_init: bool = False) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            if not is_init:
                print("Height update rejected")

    def set_age(self, age: int, is_init: bool = False) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative.")
            if not is_init:
                print("Age update rejected.")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
  def __init__(self, name: str, height: float, age: int, color: str):
    super().__init__(name, height, age)
    self._color = color

  def bloom(self) -> None:
      print(f"{self._name}: {self._height}cm, {self._age} days old")
      print(f"Color: {self._color}")
      print(f"{self._name} is blooming beautifully!")

  def show(self) -> None:
    super().show()
    print(f"Color: {self._color}")
    print(f"{self._name} has not yet bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
      super().__init__(name, height, age)
      self._diameter = diameter

if __name__ == "__main__":
  print("=== Garden Plant Types ===")
  print("=== Flower")
  rose = Flower("Rose", 9.0, 8, "red")
  rose.show()
  print("[asking the rose to bloom]")
  rose.bloom()
  print("\n===Tree")
