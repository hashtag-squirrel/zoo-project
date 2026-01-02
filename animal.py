from abc import ABC, abstractmethod
from random import choice, randint


class Animal(ABC):
    """
    Animal Base Class
    Properties: energy_level, name, age, sex
    Abstract methods: interact(), speak()
    Concrete methods: eat(), sleep(), procreate()
    """

    def __init__(self):
        self._age = 0
        if randint(1, 11) % 2 == 0:
            self._sex = 'female'
        else:
            self._sex = 'male'
        self._energy_level

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def sex(self):
        return self._sex

    @property
    def energy_level(self):
        return self._energy_level

    @energy_level.setter
    def energy_level(self, value):
        self._energy_level = value
        if self.energy_level > 10:
            self.energy_level = 10

    def eat(self, food):
        if food in self.food:
            self.energy_level += 3
            print(f'The {self.name} eats {food}.')

    def sleep(self):
        self.energy_level = 10
        print(f'The {self.name} sleeps.')

    def procreate(self):
        if randint(1, 11) % 2 == 0:
            print(f'A baby {self.name} is made.')
            return True
        else:
            print(f'The {self.name} procreates with its mate, but nothing happens.')  # noqa
            return False

    def act(self):
        print(choice(self.actions))
        self.energy_level -= 1

    @abstractmethod
    def interact(self, other):
        pass

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def snack(self):
        pass


class Herbivore(Animal):
    """
    Herbivore Sub-Class
    Properties: food; inherited from base class: energy_level, name, age, sex
    Methods: interact()
    """
    food = ['plants', 'grass', 'grains', 'leaves']

    def __init__(self):
        super().__init__()

    def run(self, animal):
        print(f'The {self.name} runs from the {animal.name}.')
        self.energy_level -= 2

    def interact(self, animal):
        if issubclass(animal.__class__, Carnivore):
            self.run(animal)
        elif isinstance(animal, self.__class__) and self.sex == animal.sex:
            return 'procreate'
        else:
            self.speak(animal)


class Carnivore(Animal):
    """
    Carnivore Sub-Class
    Properties: food; inherited from base class: energy_level, name, age, sex
    Methods: interact()
    """
    food = ['meat']

    def __init__(self):
        super().__init__()

    def hunt(self, animal):
        if self.energy_level >= 9:
            print(f'The {self.name} considers to hunt, but is feeling fully satisfied at the moment.')  # noqa
            return False
        print(f'The {self.name} hunts the {animal.name}.')
        self.energy_level -= 1
        if randint(1, 11) % 6 == 0:
            print(f'The {self.name} successfully kills the {animal.name}.')
            self.eat('meat')
            return True
        else:
            print(f'The {self.name} goes in for the kill, but misses. The {animal.name} gets away this time.')  # noqa
            return False

    def fight(self):
        print('Two lions circle, then collide in a flurry of claws and snapping jaws.')  # noqa
        if randint(1, 11) % 6 == 0:
            print('One lion is killed in the fight, leaving the victor to claim the territory.')  # noqa
            return True
        else:
            print('The victorious lion pins the other briefly before releasing and claiming the ground.')  # noqa
            return False

    def interact(self, animal):
        if issubclass(animal.__class__, Herbivore):
            return 'hunt'
        elif isinstance(animal, self.__class__) and self.sex == animal.sex:
            return 'procreate'
        elif isinstance(animal, self.__class__):
            return 'fight'
        else:
            self.speak(animal)


class Lion(Carnivore):
    """
    Lion Class
    Properties: food; inherited from base class: energy_level, name, age, sex
    """
    actions = [
        'The lion stretches lazily in the shade, keeping one eye on the rest of the pride.',  # noqa
        'The lion stalks forward slowly, muscles tense as it watches potential prey.',  # noqa
        'The lion nudges a cub gently, encouraging it to follow the group.'
    ]

    def __init__(self):
        super().__init__()

    def speak(self, animal):
        print(f"The lion roars at the {animal.name}.")

    def snack(self):
        print('The lion gnaws on a bone, cracking it slowly to reach the marrow inside.')  # noqa
        self.energy_level += 1


class Antelope(Herbivore):

    actions = [
        'The antelope freezes in place, scanning the horizon for danger.',
        'The antelope lowers its head to drink, remaining alert while doing so.',  # noqa
        'The antelope stays close to the herd, mirroring their movements.'
    ]

    def __init__(self):
        super().__init__()

    def speak(self, animal):
        print(f"The antelope snorts at the {animal.name}.")

    def snack(self):
        print('The antelope grazes calmly, ears twitching at distant sounds.')
        self.energy_level += 1


class Goose(Herbivore):

    actions = [
        'The goose waddles forward, pecking at the ground for food.',
        'The goose spreads its wings and flaps, displaying dominance.',
        'The goose keeps close to the group, adjusting its pace to stay in formation.'  # noqa
    ]

    def __init__(self):
        super().__init__()

    def speak(self, animal):
        print(f"HONK! The goose drives away the {animal.name}.")

    def snack(self):
        print(f'The goose paddles slowly, dipping its head underwater to feed on aquatic plants.')  # noqa
        self.energy_level += 1
