class Visitor:
    def feed(self, animal, food):
        print(f'You feed the {animal.name}.')
        animal.eat(food)
