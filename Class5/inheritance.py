class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class ElectricCar(Car):
    def __init__(self, model, color, battery_type):
        Car.__init__(self,model,color)
        self.battery_type = battery_type


def main():
    regular_volvo = Car("volvo", "white")
    electric_volvo = ElectricCar("electronic_volvo","red","lithium")

main()
