class FarmAnimals():
    def __init__(self, name, color, size, age):
        self.name = name
        self.color = color
        self.size = size
        self.age = age

    def __str__(self):
        return str(dict(name=self.name, color=self.color, size=self.size, age=self.age))


class Cows(FarmAnimals):
    def __init__(self, name, color, size, age, milk):
        super().__init__(name, color, size, age)
        self.milk = milk

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, milk=self.milk))


class Goats(FarmAnimals):
    def __init__(self, name, color, size, age, horns):
        super().__init__(name, color, size, age)
        self.horns = horns

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, horns=self.horns))


class Sheep(FarmAnimals):
    def __init__(self, name, color, size, age, wool):
        super().__init__(name, color, size, age)
        self.wool = wool

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, wool=self.wool))


class Pigs(FarmAnimals):
    def __init__(self, name, color, size, age, meat):
        super().__init__(name, color, size, age)
        self.meat = meat

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, meat=self.meat))


class Ducks(FarmAnimals):
    def __init__(self, name, color, size, age, feather):
        super().__init__(name, color, size, age)
        self.feather = feather

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, feather=self.feather))


class Chicken(FarmAnimals):
    def __init__(self, name, color, size, age, eggs):
        super().__init__(name, color, size, age)
        self.eggs = eggs

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, eggs=self.eggs))


class Geese(FarmAnimals):
    def __init__(self, name, color, size, age, fluff):
        super().__init__(name, color, size, age)
        self.fluff = fluff

    def __str__(self):
        return str(
            dict(name=self.name, color=self.color, size=self.size, age=self.age, fluff=self.fluff))


cow = Cows('Zorka', 'white', 'big', 10, 'yes')
print(cow)
goat = Goats('Gena', 'grey', 'medium', 5, 'yes')
print(goat)
sheep = Sheep('Masha', 'black', 'medium', 7, 'yes')
print(sheep)
pig = Pigs('Nura', 'rose', 'medium', 4, 'yes')
print(pig)
duck = Ducks('Donald', 'grey', 'little', 2, 'yes')
print(duck)
chicken = Chicken('Natasha', 'white', 'little', 2, 'yes')
print(chicken)
goose = Geese('Vasya', 'white', 'little', 4, 'yes')
print(goose)
goose1 = Geese('Venya', 'white', 'little', 2, 'no')
print(goose1)
