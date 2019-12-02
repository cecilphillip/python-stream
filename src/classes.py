class Car:
    running = False
    cd_player = True
    can_break_window = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def is_started(self):
        if self.running:
            print(f'The car is running, make {self.make} model {self.model}')
        else:
            print('The car has not started')

    def __str__(self):
        return f"This car is a {self.make} of {self.model}"

    def __repr__(self):
        return f'Car("{self.make}", "{self.model}")'


    @classmethod
    def has_cd_player(cls):
        return cls.cd_player # is the same as Car.cd_player

    @classmethod
    def can_we_break_this_window(cls):
        return cls.can_break_window

# print(f'This is from Car.running {Car.running}')

my_car = Car('Tesla', 'CyberTruck')

print(repr(my_car))
print(str(my_car))

print(my_car)

# my_car.running = True # this references self.running
# my_car.tv = True # this references self.engine
# my_car.is_started()

# print(f'This is from Car.running {Car.running}')

# my_other_car = Car('Tesla', 'Model8')
# my_other_car.is_started()

