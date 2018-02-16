class FarmAnimals():
    def __init__(self, kind, color, size, age):
        self.kind = kind
        self.color = color
        self.size = size
        self.age = age

    def __str__(self):
        return str(dict(kind=self.kind, color=self.color, size=self.size, age=self.age))


class Animals(FarmAnimals):
    def __init__(self, kind, color, size, age, horns, milk, ):
        super().__init__(kind, color, size, age)
        self.horns = horns
        self.milk = milk

    def __str__(self):
        return str(
            dict(kind=self.kind, color=self.color, size=self.size, age=self.age, horns=self.horns, milk=self.milk))


class Birds(FarmAnimals):
    def __init__(self, kind, color, size, age, gender, eggs):
        super().__init__(kind, color, size, age)
        self.gender = gender
        self.eggs = eggs

    def __str__(self):
        return str(
            dict(kind=self.kind, color=self.color, size=self.size, age=self.age, gender=self.gender, eggs=self.eggs))

cow = Animals('Cow', 'white', 'big', 10, 'yes', 'yes')
print(cow)
goat = Animals('Goat', 'grey', 'medium', 5, 'no', 'yes')
print(goat)
sheep = Animals('Sheep', 'black', 'medium', 7, 'no', 'no')
print(sheep)
pig = Animals('Pig', 'rose', 'medium', 4, 'no', 'no')
print(pig)
duck = Birds('Duck', 'grey', 'little', 2, 'female', 'yes')
print(duck)
chicken = Birds('Chicken', 'white', 'little', 2, 'female', 'yes')
print(chicken)
goose = Birds('Goose', 'white', 'little', 4, 'male', 'no')
print(goose)
