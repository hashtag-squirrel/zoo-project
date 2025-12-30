import animal
import inspect


class AnimalFactory:
    def get_classes(self):
        herbivores = []
        carnivores = []
        for name, obj in inspect.getmembers(animal):
            if inspect.isclass(obj) and issubclass(obj, animal.Herbivore):
                if obj.__name__ != 'Herbivore':
                    herbivores.append(obj)
            if inspect.isclass(obj) and issubclass(obj, animal.Carnivore):
                if obj.__name__ != 'Carnivore':
                    carnivores.append(obj)
        return herbivores, carnivores

    def create_animals(self, herbivore=8, carnivore=3):
        animals = []
        herbivores, carnivores = self.get_classes()
        for obj in herbivores:
            for _ in range(herbivore):
                animals.append(obj())
        for obj in carnivores:
            for _ in range(carnivore):
                animals.append(obj())
        return animals
