from animal_factory import AnimalFactory
from simulation import Simulation
import os
import time


# Initialize the simulation
animal_factory = AnimalFactory()
sim = Simulation(animal_factory.create_animals())


# Ask for user input
os.system('cls')
print('''---------- Welcome to the Zoo Simulator! ----------

The simulator lets you experience the animals in the zoo for any number of
days and you can determine how many hours (aka animal actions) a day should
last.

After each day, you will receive a report over the current population of the
zoo.

At the end of the simulation, you will get statistics over how the zoo
population developed during the simulation.
''')

days = int(input(
    'Please input how many days at the zoo you wish to experience: '))
hours = int(input(
    'Please input how many hours a day should last: '))

print('You are entering the zoo')
for _ in range(3):
    print('...')
    time.sleep(1)
os.system('cls')
sim.run_simulation(days, hours)
