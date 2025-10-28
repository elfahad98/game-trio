import random


class Element:
    def __init__(self, char_repr):
        self.char_repr = char_repr

    def __repr__(self):
        return self.char_repr

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.char_repr == other.char_repr

class Resource(Element):
    def __init__(self, char_repr, value):
        super().__init__(char_repr)
        self.value = value

    def get_value(self):
        return self.value

class Water(Resource):
    def __init__(self):
        super().__init__('\U0001F4A7', 0.0)

class Herb(Resource):
    def __init__(self):
        super().__init__('\U0001F331', 0.0)

class Animal(Element):
    def __init__(self, char_repr, life_max):
        super().__init__(char_repr)
        self.age = 0
        self.gender = random.randint(0, 1)  # 0: Female, 1: Male
        self.bar_life = [life_max, life_max]  # [current_life, max_life]
        self._current_direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

    def get_age(self):
        return self.age

    def ageing(self):
        self.age += 1

    def get_gender(self):
        return self.gender

    def get_life_max(self):
        return self.bar_life[1]

    def get_life(self):
        return self.bar_life[0]

    def is_alive(self):
        return self.bar_life[0] > 0

    def is_dead(self):
        return not self.is_alive()

    def recovering_life(self, value):
        self.bar_life[0] = min(self.bar_life[0] + value, self.bar_life[1])

    def losing_life(self, value):
        self.bar_life[0] = max(self.bar_life[0] - value, 0)

    def get_current_direction(self):
        return self._current_direction

    def set_current_direction(self, line_direction, column_direction):
        self._current_direction = [line_direction, column_direction]

class Cow(Animal):
    def __init__(self):
        super().__init__('\U0001F42E', 100)

class Dragon(Animal):
    def __init__(self):
        super().__init__('\U0001F432', 300)

class Lion(Animal):
    def __init__(self):
        super().__init__('\U0001F981', 150)

class Mouse(Animal):
    def __init__(self):
        super().__init__('\U0001F42D', 50)

class Ground(Element):
    def __init__(self):
        super().__init__('\u2E1C')


class Human(Element):
    """Représente un être humain dans le jeu de Conway"""
    SYMBOL = "H"  # Utilisé pour représenter un Human sur la grille

    def __init__(self):
        super().__init__(Human.SYMBOL)



# TEST~##

print(Ground(), str(Ground()))
print(Ground() == str(Ground()))
print(Ground() == Ground())
print(Ground() is Ground())

TYPES_COUNT = {Herb: 2, Water: 3, Cow: 2, Dragon: 1, Lion: 5, Mouse: 10}
ELEMENTS_BY_TYPE = {element_type: [element_type() for _ in range(element_count)]
                    for element_type, element_count in TYPES_COUNT.items()}

for element_type, elements in ELEMENTS_BY_TYPE.items():
    print(element_type.__name__, elements)
