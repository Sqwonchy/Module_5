class House:
    def __init__(self,name = str,number_of_floors = int):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor = int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for number_floors in range(1,new_floor+1):
                print(number_floors)
    
    def __len__(self):
        return self.number_of_floors
        
    def __str__(self):
        return str(f'Название: {self.name}, колличесиво этажей {self.number_of_floors}.')


#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)
#h1.go_to(5)
#h2.go_to(10)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))