class Car:
    amount_cars = 0
    
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1

    def print_car_amount(self):
        print("Amount: {}".format(Car.amount_cars))
