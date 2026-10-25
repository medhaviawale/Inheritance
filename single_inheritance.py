class Vehicle:
    Company_Name = "ABC Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        print(f"Init of Vehicle")
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This Vehicle has {self.n_wheels} wheels, {self.n_seats} seats and provide a mileage of {self.mileage}."

# v1 = Vehicle(4, 7, 30)
# print(v1.get_details())

class Car(Vehicle):
    model = "ABC123"

    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        print(f"Init of Car")
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(wheels, seats, mileage)


c1 = Car("SUV", "Manual", 4, 7, 15)
print(c1.model)
print(c1.Company_Name)
print(c1.mileage)
print(c1.get_details())
print(c1.__dict__)
