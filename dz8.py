'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
class Date:
    def __init__(self, date: str = 'dd-mm-yyyy'):
        self.date = date

    @classmethod
    def ch_date(cls, date: str = 'dd-mm-yyyy'):
        d = date.split('-')
        return int(d[0]), int(d[1]), int(d[2])

    @staticmethod
    def valid(day, month, year):
        month_list = ['январь','февраль','март','апрель','май','июнь',
                      'июль','август','сентябрь','октябрь','ноябрь','декабрь']

        if 0 <= year <= 2021:
            if year % 4 == 0 and month == 2:
                if 1 <= day <= 29:
                    return print('Данные верны')
                else:
                    return print(f'{year} - весокосный год. В феврале 29 дней')
            elif month in [1,3,5,7,8,10,12]:
                if 1 <= day <= 31:
                    return print('Данные верны')
                else:
                    return print(f'Неверно введен день. В месяце {month_list[month-1]} - 31 день.')
            elif month in [4,6,9,11]:
                if 1 <= day <= 30:
                    return print('Данные верны')
                else:
                    return print(f'Неверно введен день. В месяце {month_list[month-1]} - 30 дней.')
            elif month == 2:
                if 1 <= day <= 28:
                    return print('Данные верны')
                else:
                    return print(f'{year} - не весокосный год. В феврале 28 дней.')
            else:
                return print('Неверно введен месяц. От 1 до 12.')
        else:
            return print('Неверно введен год.')

D=Date()
print(Date.ch_date('11-11-2021'))
print(D.ch_date('11-12-2021'))
print()
Date.valid(2,11,2021)
D.valid(60,4,2021)

'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class ZeroDiv:
    @classmethod
    def TryZeroDiv(cls,x,y):
        try:
            print(f'Частное: {int(x)/int(y)}')
        except ValueError:
            print('Вы ввели не числа.')
        except ZeroDivisionError:
            print('Делить на ноль нельзя')

d_1 = input('Введите делимое: ')
d_2 = input('Введите делитель: ')
ZeroDiv.TryZeroDiv(d_1, d_2)

'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''
class ValErr:
    @staticmethod
    def TryValErr():
        my_list = []
        el_list = ''
        print('Введи элементы списка (для окончания ввода напиши stop):')
        while el_list != 'stop':
            el_list = input()
            try:
                el_list = int(el_list)
                my_list.append(el_list)
            except ValueError:
                if el_list != 'stop':
                    print('Вы ввели не число.')
                else:
                    print('Ввод окончен.')
        print(f'Полученный список: {my_list}')
ValErr.TryValErr()

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
import datetime

class Store: #класс склада
    def __init__(self, name, address, telephone):  #параметры склада: название, адрес, телефон
        self.name = name
        self.address = address
        self.telephone = telephone

    stock = []

    def add_equipment(self, equipment):
        try:
            self.stock.append({'Оборудование':equipment.name_eq, 'Фирма': equipment.firm, 'Модель': equipment.model, 'Количество':int(equipment.amount)})
            print(f'На склад {self.name} передано оборудование: \n{equipment}')
            print()
        except:
            print(f'При попытке передачи на склад оборудования: \n{equipment}')
            print('произошла ошибка: количество может быть только числом')
            print()
    @staticmethod
    def get_stock():
        print()
        print(f'Запас склада на {datetime.date.today()}:')
        for n, el in enumerate(Store.stock):
            print(el)

class Office_Equipment: #класс оргтехники
    def __init__(self, firm, model, amount, name_eq):  #параметры: фирма-производитель, модель, количество
        self.name_eq = name_eq
        self.firm = firm
        self.model = model
        self.amount = amount

class Printer(Office_Equipment):
    def __init__(self, firm, model, amount, print_resolution, name_eq = 'Принтер'): #уникальный параметр: разрешение печати
        self.print_resolution = print_resolution
        super().__init__(firm, model, amount, name_eq)

    def __str__(self):
        return f'{self.name_eq}: {self.firm}, {self.model}, разрешение печати: {self.print_resolution}, {self.amount} шт.'

class Scanner(Office_Equipment):
    def __init__(self, firm, model, amount, density, name_eq = 'Сканер'): #уникальный параметр: плотность оригинала
        self.density = density
        super().__init__(firm, model, amount, name_eq)

    def __str__(self):
        return f'{self.name_eq}: {self.firm}, {self.model}, плотность оригинала: {self.density}, {self.amount} шт.'

class Copier(Office_Equipment):
    def __init__(self, firm, model, amount, speed_copy, name_eq  = 'Ксерокс'): #уникальный параметр: скорость копирования
        self.speed_copy = speed_copy
        super().__init__(firm, model, amount, name_eq)

    def __str__(self):
        return f'{self.name_eq}: {self.firm}, {self.model}, скорость печати: {self.speed_copy}, {self.amount} шт.'


store1 = Store('Центральный','ул.Ленина, 48','8-900-000-00-00')
printer1 = Printer('HP','LaserJet Pro M404n', 10, '1200*1200')
scanner1 = Scanner('Canon', 'DR-F120', 'four','35 – 128')
copier1 = Copier('Kyocera', 'FS-1120MFP', 3, '20')

store1.add_equipment(printer1)
store1.add_equipment(scanner1)
store1.add_equipment(copier1)
store1.get_stock()
