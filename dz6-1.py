'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

from time import sleep
class TrafficLight:
    __color = ['red','yellow','green']
    def running(self):
        for i,el in enumerate(TrafficLight.__color):
            print(f'Сигнал светофора: {el}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
TraffLight = TrafficLight()
TraffLight.running()


'''
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    mass_1_square = 25                      #кг - масса асфальта площадью 1кв.м., толщиной 1 см

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, thickness):
        return self._width * self._length * thickness * self.mass_1_square
try:
    m = Road(float(input('Введите длину дорожного полотна (м): ')), float(input('Введите ширину дорожного полотна (м): ')))
    print(f"{m.mass(float(input('Введите толщину дорожного покрытия в см: ')))} - масса асфальта")
except:
    print('Необходимо вводить числовые значения (дробные через точку)')

'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income= {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

try:
    w = Position(
        input('Имя сотрудника: '),
        input('Фамилия сотрудника: '),
        input('Должность сотрудника: '),
        int(input('Оклад сотрудника (руб): ')),
        int(input('Премия сотрудника (руб): ')),
    )
    print(f'Работник {w.get_full_name()} ежемесячно получает {w.get_total_income()} рублей')
except:
    print("Ошибка: поля Оклад и Премия должны содержать только числовые значения!")

'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, color, name, is_police:bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0

    def go(self, speed):                    #запускает машину с указанной скоростью
        self.speed = speed
        return print(f'Машина начинает движение')

    def stop(self):
        self.speed = 0
        return print('Машина остановилась')

    def turn(self, direction:str):          #определяет повотор машины
        if direction not in ('направо', 'налево'):
            return print('Поворот может быть только "направо" или "налево"')
        elif self.speed == 0:
            return print('Поворот на месте невозможен. Машина стоит, а не едет.')
        else:
            return print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/ч')
        if hasattr(self, 'max_speed') and self.speed > self.max_speed:
            return print(f'Скорость автомобиля превышена на {self.speed - self.max_speed} км/ч')

class TownCar(Car):
    max_speed = 60

class SportCar(Car):
    pass

class WorkCar(Car):
    max_speed = 40

class PoliceCar(Car):
    def __init__(self,*args):
        super().__init__(*args, is_police = True)
    def viuviu(self):
        print('Начинаем преследование.')

c = WorkCar('red','Honda')
print(f'Машина марки {c.name} цвет: {c.color}')
c.go(60)
c.show_speed()
c.turn('направо')
c.stop()
print()

p = PoliceCar('blue','lada')
print(f'Полицейская машина марки {p.name} цвет: {p.color}')
p.go(120)
p.turn('налево')
p.show_speed()
p.viuviu()
print()

w = WorkCar('VAZ', 'green')
w.go(30)
w.show_speed()

'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

o = Stationery('Что-то пишущее')
print(o.title)
o.draw()
print()
r = Pen('Ручка Berlingo')
print(r.title)
r.draw()
print()
k = Pencil('Карандаш Erich Krause')
print(k.title)
k.draw()
print()
m = Handle('Маркер черный')
print(m.title)
m.draw()