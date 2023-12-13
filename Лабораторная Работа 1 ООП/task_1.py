import doctest


class Car:
    def __init__(self, brand: str, model: str, color: str):
        """
        Конструктор класса Car.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param color: Цвет автомобиля.

        >>> car = Car("Lada", "Vesta", "Red")
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.brand = brand
        self.model = model
        self.color = color

    def move(self) -> None:
        """
        Заставляет автомобиль двигаться.

        >>> car = Car("Lada", "Vesta", "Red")
        >>> car.move()
        """
        ...

    def stop(self) -> None:
        """
        Останавливает автомобиль.

        >>> car = Car("Lada", "Vesta", "Red")
        >>> car.stop()
        """
        ...

    def park(self) -> None:
        """
        Паркует автомобиль.

        >>> car = Car("Lada", "Vesta", "Red")
        >>> car.park()
        """
        ...

    def repaint(self, new_color: str) -> None:
        """
        Перекрашивает автомобиль в новый цвет.
        :param new_color: Новый цвет автомобиля.
        >>> car = Car("Lada", "Vesta", "Red")
        >>> car.repaint("Blue")
        >>> print(car.color)
        Blue
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        self.color = new_color


class Engine:
    def __init__(self, type_engine: str, volume: float):
        """
        Конструктор класса Engine.
        :param type_engine: Тип двигателя.
        :param volume: Объем двигателя в литрах.

        >>> engine = Engine("бензиновый", 1.6)
        """
        if not isinstance(type_engine, str):
            raise TypeError("Тип должен быть строкой")
        assert isinstance(volume, float) and volume > 0, "Объем должен быть положительным числом"
        self.type_engine = type_engine
        self.volume = volume

    def start(self) -> bool:
        """
        Запускает двигатель.
        >>> engine = Engine("бензиновый", 1.6)
        >>> engine.start()
        """
        ...

    def stop(self) -> bool:
        """
        Останавливает двигатель.
        >>> engine = Engine("бензиновый", 1.6)
        >>> engine.stop()
        """
        ...


class Transmission:
    def __init__(self, transmission_type: str, number_of_gears: int):
        """
        Конструктор класса Transmission.
        :param transmission_type: Тип трансмиссии.
        :param number_of_gears: Количество передач.

        >>> transmission = Transmission("механическая", 5)
        """
        if not isinstance(transmission_type, str):
            raise TypeError("Тип должен быть строкой")
        assert isinstance(number_of_gears, int) and number_of_gears > 0, "Количество передач должно быть положительным числом"
        self.transmission_type = transmission_type
        self.number_of_gears = number_of_gears

    def switch_gear(self, gear: int) -> None:
        """
        Переключает передачу.
        :param gear: Номер передачи.
        >>> transmission = Transmission("механическая", 5)
        >>> transmission.switch_gear(3)
        """
        assert isinstance(gear, int) and 0 < gear <= self.number_of_gears, "Передача должна быть положительным числом и не превышать количество передач"
        ...

    def engage_reverse(self) -> bool:
        """
        Включает заднюю передачу.
        >>> transmission = Transmission("механическая", 5)
        >>> transmission.engage_reverse()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
