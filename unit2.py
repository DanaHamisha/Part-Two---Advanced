from abc import ABC, abstractmethod


class Animal(ABC):
    zoo_name = "Hayaton"

    # create an animal instance
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    # return the name
    def get_name(self):
        return self._name

    # return if the animal is hungry
    def is_hungry(self):
        return self._hunger > 0

    # feed the animal
    def feed(self):
        self._hunger = self._hunger - 1

    # create an abstract method
    @abstractmethod
    def talk(self):
        pass


class Dog(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal, ABC):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    # talk method
    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')


class Unicorn(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('Good day, darling')

    def sing(self):
        print('I’m not your toy...')


class Dragon(Animal, ABC):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    # talk method
    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')


def main():
    # create the zoo list
    zoo_lst = [Dog('Brownie', 10), Cat('Zelda', 3), Skunk('Stinky', 0), Unicorn('Keith', 7), Dragon('Lizzy', 1450)]

    # add new animals to the list
    new_lst = [Dog("Doggo", 80), Cat('Kitty', 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80), Dragon("McFly", 80)]

    zoo_lst.extend(new_lst)

    # check if the animal is hungry and feeds it
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:
            animal.breath_fire()

    print("The zoo name: " + Animal.zoo_name)


if __name__ == '__main__':
    main()
