""" Ваша задача:
Если вы решали старую версию задачи, проверка будет производиться по ней.

Ссылка на старую версию тут.



Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.



Задача "Нужно больше этажей":

Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".



Необходимо дополнить класс House следующими специальными методами:

__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты
сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:



Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.

Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:

isinstance(other, int) - other указывает на объект типа int.

isinstance(other, House) - other указывает на объект типа House.



Пример результата выполнения программы:

Пример выполняемого кода:

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__



Вывод на консоль:

Название: ЖК Эльбрус, кол-во этажей: 10

Название: ЖК Акация, кол-во этажей: 20

False

Название: ЖК Эльбрус, кол-во этажей: 20

True

Название: ЖК Эльбрус, кол-во этажей: 30

Название: ЖК Акация, кол-во этажей: 30

False

True

False

True

False



Примечания:

Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__.
Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.




Успехов!

 """


# Solution

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

h1 = House('ЖК "Андромед"', 10)
h2 = House('ЖК "Солярис"', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__