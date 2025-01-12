class Car:
    amount_cars = 0
    
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1

    def print_car_amount(self):
        print("Amount: {}".format(Car.amount_cars))

    def __del__(self):
        print("Car object deleted")
        Car.amount_cars -= 1

if __name__ == "__main__":
    myCar1 = Car("Tesla", "Model X", 525)
    myCar2 = Car("BMW", "X3", 200)
    myCar3 = Car("VW", "Golf", 100)
    myCar4 = Car("Porsche", "911", 520)
    del myCar3
    myCar1.print_car_amount()
