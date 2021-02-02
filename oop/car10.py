# Создать класс Car. Атрибуты: марка, модель, год выпуска,
# скорость(по умолчанию 0). Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def print_speed(self):
        print(f'Speed: {self.__speed}')

    def turning(self):
        self.__speed = -self.__speed


def main():
    car = Car('Audi', '80', '1971')

    car.increase_speed()
    car.print_speed()

    car.decrease_speed()
    car.decrease_speed()
    car.print_speed()

    car.stop()

    car.increase_speed()
    car.print_speed()
    car.turning()
    car.print_speed()


if __name__ == '__main__':
    main()
