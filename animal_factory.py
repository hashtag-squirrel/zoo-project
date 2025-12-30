from animal import Lion, Antelope, Goose


class AnimalFactory:
    def create_animals(self):
        animals = []
        for _ in range(5):
            animals.append(Goose())
            animals.append(Lion())
            animals.append(Antelope())
        return animals
