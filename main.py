class Car:
    def __init__(self, model_name, colour, seats, max_speed):
        self.model_name = model_name
        self.colour = colour
        self.seats = seats
        self.max_speed = max_speed
        print('The %s %s model has %d seats and its max speed is %d.' % (self.colour, self.model_name, self.seats, self.max_speed))

    
    def set_brand_name(self, brand_name):
        print('The car is from %s.' % (brand_name))


    def increase_max_speed(self, max_speed_ratio):
        new_max_speed = self.max_speed * max_speed_ratio
        print('Tuning finished: The new max speed of %s %s is %d.' % (self.brand_name, self.model_name, new_max_speed))


class Model1(Car):
    """
    Example documentation for inheritage class Audi.
    """
    
    brand_name = 'Audi'
    max_speed_ratio = 1.5


class Model2(Car):
    """
    Example documentation for inheritage class BMW.
    """

    brand_name = 'Mercedes'
    max_speed_ratio = 1.4



if __name__ == '__main__':
    car1 = Model1('TC1', 'red', 4, 10)
    car1.set_brand_name(Model1.brand_name)
    car1.increase_max_speed(Model1.max_speed_ratio)
    print('\n')
    car2 = Model2('TC2', 'blue', 6, 10)
    car2.set_brand_name(Model2.brand_name)
    car2.increase_max_speed(Model2.max_speed_ratio)