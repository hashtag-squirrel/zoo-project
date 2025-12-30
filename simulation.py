from random import choice, randint
import time


class Simulation:
    population = {}
    population_over_time = []

    def __init__(self, animals):
        self.animals = animals
        self.day = 0

    def report(self):
        """
        Prints out a report of the current population on the current day
        """
        current_population = self.population.copy()
        self.population_over_time.append(current_population)
        print(f'''
---------------------------------------
Zoo Simulation Report
Day: {self.day}
Population (Total: {len(self.animals)}):''')
        for animal, number in self.population.items():
            print(f'  {animal.upper()}: {number}')
        print('---------------------------------------')

    def statistics(self):
        """
        Prints out the population over the whole run of the simulation
        """
        count = 0
        for item in self.population_over_time:
            print(f'\nDay {count}')
            for animal, number in item.items():
                print(f'{animal}: {number}', end=', ')
            count += 1

    def count_animals(self):
        """
        Counts the contents of the animal list and collates the numbers in a
        dict
        """
        for animal in self.animals:
            if animal.name in self.population.keys():
                self.population[animal.name] += 1
            else:
                self.population[animal.name] = 1

    def choose_random_animal(self):
        """
        Returns a randomly chosen animal from the animal list
        """
        return choice(self.animals)

    def choose_action(self, animal):
        """
        Chooses action or interaction for the specified animal
        """
        if randint(1, 11) % 3 == 0:
            self.action(animal)
        else:
            self.interaction(animal)

    def interaction(self, animal1):
        """
        Processes the interaction for the animal based on the return value
        from the interaction method from the animal class

        Adjusts the animal list, as well as the population dict if needed
        """
        animal2 = self.choose_random_animal()
        interaction = animal1.interact(animal2)
        if interaction == 'hunt':
            if animal1.hunt(animal2):
                self.animals.remove(animal2)
                self.population[animal2.name] -= 1
        elif interaction == 'procreate':
            if animal1.procreate():
                self.animals.append(animal1.__class__())
                self.population[animal1.name] += 1
        elif interaction == 'fight':
            if animal1.fight():
                self.animals.remove(animal2)
                self.population[animal2.name] -= 1

    def action(self, animal):
        """
        Chooses the action for the animal based on its energy level
        """
        if animal.energy_level >= 7:
            animal.act()
        elif animal.energy_level < 3:
            animal.sleep()
        else:
            animal.snack()

    def turn(self):
        """
        A turn consists of randomly choosing an animal and then performing an
        action for this animal
        """
        animal = self.choose_random_animal()
        self.choose_action(animal)

    def run_day(self):
        """
        Updates the day attribute
        Runs 24 turns with a 2 second break inbetween each turn
        At the end of the day, all animals go to sleep
        Prints the report after the animals sleep
        """
        self.day += 1
        for _ in range(24):
            self.turn()
            time.sleep(2)
        for animal in self.animals:
            animal.age += 1
            animal.sleep()
        self.report()

    def run_simulation(self, days):
        """
        Entrypoint into the simulation
        Runs the simulation for the specified number of days
        Prints out the statistics over population over time at the end
        """
        self.count_animals()
        current_population = self.population.copy()
        self.population_over_time.append(current_population)
        for i in range(days):
            self.run_day()
            if i < days-1:
                input("Press 'Enter' to continue to the next day.")
        self.statistics()
