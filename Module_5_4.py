class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name=str, number_of_floors=int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor=int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for number_floors in range(1, new_floor + 1):
                print(number_floors)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, колличесиво этажей {self.number_of_floors}.')
    def __eq__(self,other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self,other):
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
        if not isinstance(value,int):
            print("обьект 'value' должен быть целым числом")
        else:
            return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        return self.__add__(value)
    def __radd__(self, value):
        return self.__add__(value)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
# ____________________________________________________________________________
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
