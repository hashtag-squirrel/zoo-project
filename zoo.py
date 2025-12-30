from animal_factory import AnimalFactory
from simulation import Simulation


class Visitor:
    def feed(self, animal, food):
        print(f'The visitor feeds the {animal.name}')
        animal.eat(food)


animal_factory = AnimalFactory()

sim = Simulation(animal_factory.create_animals())


visitor = Visitor()

sim.run_simulation(5)
