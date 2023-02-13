import random

from car import Car

CAR_QTY = 16

class Traffic:

    def __init__(self):
        self.cars = []
        self.create_traffic()

    def create_traffic(self):
        car_y_position = -240

        for _ in range(CAR_QTY):
            car = Car()
            car_x_position = random.randrange(-280, 300, 40)
            car.set_position(car_x_position, car_y_position)
            self.cars.append(car)
            car_y_position += 30

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -300:
                car.back_to_edge()

    def turtle_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

        return False

