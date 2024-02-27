class Animal:
    def __init__(self, name):
        self.name = name


class Panda(Animal):
    def __init__(self, name, loc):
        self.loc = loc
        Animal.__init__(self, name)


first = Panda("Atharva", "Labs")
print(first.name)
