# Определим базовый класс Automobile, который будет включать общие атрибуты и методы для автомобилей.
class Automobile:
    """
    Базовый класс для всех типов автомобилей, с добавлением непубличного атрибута и метода.

    Атрибуты:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        _year (int): Год выпуска, защищённый атрибут.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация нового экземпляра класса Automobile, включая непубличный атрибут _year.
        """
        self.make = make
        self.model = model
        self._year = year  # Защищённый атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.
        """
        return f"{self._year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление автомобиля.
        """
        return f"Automobile(make={self.make}, model={self.model}, year={self._year})"

    def _calculate_age(self) -> int:
        """
        Непубличный метод для вычисления возраста автомобиля.

        Возвращает:
            int: Возраст автомобиля.
        """
        return 2024 - self._year  # Примерное вычисление возраста, предполагая текущий год как 2024

    def basic_info(self) -> str:
        """
        Возвращает базовую информацию об автомобиле, включая его возраст.
        """
        age = self._calculate_age()
        return f"This is a {self.make} {self.model} from {self._year}. It is {age} years old."


# Определим дочерний класс PassengerCar, расширяющий базовый класс свойствами и методами легковых автомобилей.
class PassengerCar(Automobile):
    """
    Класс для легковых автомобилей, наследующий от Automobile.

    Атрибуты:
        seating_capacity (int): Вместимость посадочных мест.
    """

    def __init__(self, make: str, model: str, year: int, seating_capacity: int):
        """
        Инициализация нового экземпляра класса PassengerCar.
        """
        super().__init__(make, model, year)
        self.seating_capacity = seating_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля, расширяя базовую версию.
        """
        return super().__str__() + f" with seating capacity for {self.seating_capacity}."

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление легкового автомобиля.
        """
        return f"PassengerCar(make={self.make}, model={self.model}, year={self.year}, seating_capacity={self.seating_capacity})"

    def passenger_info(self) -> str:
        """
        Возвращает информацию о вместимости посадочных мест легкового автомобиля.

        Перегружает метод базового класса, добавляя специфичную для легковых автомобилей информацию.
        """
        return f"This passenger car can seat up to {self.seating_capacity} people."


# Определим дочерний класс CargoTruck, расширяющий базовый класс свойствами и методами грузовых автомобилей.
class CargoTruck(Automobile):
    """
    Класс для грузовых автомобилей, наследующий от Automobile.

    Атрибуты:
        cargo_capacity (int): Грузоподъёмность в килограммах.
    """

    def __init__(self, make: str, model: str, year: int, cargo_capacity: int):
        """
        Инициализация нового экземпляра класса CargoTruck.
        """
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля, расширяя базовую версию.
        """
        return super().__str__() + f" with cargo capacity of {self.cargo_capacity} kg."

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление грузового автомобиля.
        """
        return f"CargoTruck(make={self.make}, model={self.model}, year={self.year}, cargo_capacity={self.cargo_capacity})"

    def cargo_info(self) -> str:
        """
        Возвращает информацию о грузоподъёмности грузового автомобиля.

        Перегружает метод базового класса, добавляя специфичную для грузовых автомобилей информацию.
        """
        return f"This cargo truck can carry up to {self.cargo_capacity} kg of cargo."


# Основа программы, демонстрирующая использование классов.
if __name__ == "__main__":
    # Создание экземпляра легкового автомобиля
    passenger_car = PassengerCar("Toyota", "Camry", 2020, 5)
    print(passenger_car)
    print(passenger_car.passenger_info())

    # Создание экземпляра грузового автомобиля
    cargo_truck = CargoTruck("Volvo", "FH", 2018, 20000)
    print(cargo_truck)
    print(cargo_truck.cargo_info())

    # Создание другого экземпляра легкового автомобиля
    another_passenger_car = Automobile("Honda", "Civic", 2018)
    print(another_passenger_car.basic_info())

    pass
