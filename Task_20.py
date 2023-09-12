# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
import json


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):
    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):
    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):
    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

# Класс-фабрика
class AnimalFactory:
    def create_animal(self, animal_type, kind, name, age, specific_param):
        if animal_type == 'Fishes':
            return Fishes(kind, name, age, specific_param)
        elif animal_type == 'Birds':
            return Birds(kind, name, age, specific_param)
        elif animal_type == 'Mammals':
            return Mammals(kind, name, age, specific_param)
        else:
            raise ValueError(f"Unsupported animal type: {animal_type}")

    def serialize_animal(self, animal, file_name):
        data = {
            'kind': animal.get_kind(),
            'name': animal.get_name(),
            'age': animal.get_age(),
            'specific_param': animal.get_specific() if hasattr(animal, 'get_specific') else None
        }
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    def deserialize_animal(self, animal_type, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        kind = data['kind']
        name = data['name']
        age = data['age']
        specific_param = data.get('specific_param')
        return self.create_animal(animal_type, kind, name, age, specific_param)


# Создаем экземпляр класса фабрики
animal_factory = AnimalFactory()
# Создаем рыбу с использованием фабрики
fish = animal_factory.create_animal('Fishes', 'Карась', 'Федя', 1, 15)
# Сериализация
animal_factory.serialize_animal(fish, 'fish.json')
# Десериализация
deserialized_fish = animal_factory.deserialize_animal('Fishes', 'fish.json')

print(f'Вид: {deserialized_fish.get_kind()}')
print(f'Кличка: {deserialized_fish.get_name()}')
print(f'Возраст: {deserialized_fish.get_age()} лет')
print(f'Размер: {deserialized_fish.get_specific()} см.')