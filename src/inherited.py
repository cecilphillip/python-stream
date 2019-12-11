from colorama import Fore, Style


class Vehicle():
    number_of_wheels = 4

    def __init__(self, make, model, fuel='gas'):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return Fore.GREEN + f'This is a {self.make} of model {self.model}'


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    number_of_wheels = 2
    pass


class Watercraft(Vehicle):
    number_of_wheels = 0
    number_of_sails = 2

    def __init__(self, make, model, color, fuel='gas'):
        super().__init__(make, model, fuel=fuel)
        self.color = color

    def __str__(self):
        return (
            Fore.GREEN +
            f'This is a Watercraft of make {self.make} and of model {self.model}.'
            f' It has a color of {self.color}'
            f' and has #{Watercraft.number_of_sails} sails'
        )


class Boat(Watercraft):
    pass


class Jetski(Watercraft):
    pass


# #my_car = Car('Acura', 'TSX')
# my_yachty = Boat('NorthStar', 'Expensive', 'Red', fuel='disel')


# my_yachty.number_of_sails = 1 # self.number_of_sails

# Watercraft.number_of_sails = 6

# print(Watercraft.number_of_sails)
# print(my_yachty.number_of_sails)

# print(Style.RESET_ALL)
# print(my_yachty)


class DontDoItException(Exception):
    def __init__(self, issue):
        self.issue = issue
        super().__init__("Why did you do that Brian???")


def dont_do_this():
    preordered_cybertruck = True

    if preordered_cybertruck:
        raise DontDoItException('The glass window sucks!')


try:
    dont_do_this()
except DontDoItException as error:
    print(f'{Fore.RED} Logging error of type DontDoItException. Issue => {error.issue} ')
