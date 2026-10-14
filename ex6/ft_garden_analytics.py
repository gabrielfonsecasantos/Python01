class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.stats = self.Statistics()
        self.set_height(height, is_init=True)
        self.set_age(age, is_init=True)

    def get_name(self) -> str:
        return self._name

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

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: float) -> None:
        self.stats.increment_grow()
        self.set_height(self.get_height() + amount)

    def age(self, days: int) -> None:
        self.stats.increment_age()
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        self.stats.increment_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._has_bloomed: bool = False

    def bloom(self) -> None:
        self._has_bloomed = True
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._has_bloomed:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.stats = self.TreeStatistics()
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        if isinstance(self.stats, self.TreeStatistics):
            self.stats.increment_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    display_statistics(sunflower)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)