# First Parent Class
class Vehicle:
    def __init__(self, n_wheels, n_seats):
        print("Init of Vehicle")
        self.n_wheels = n_wheels
        self.n_seats = n_seats

    def drive(self):
        return "The vehicle is moving."


# Second Parent Class
class ElectricDevice:
    def __init__(self, battery_capacity):
        print("Init of ElectricDevice")
        self.battery_capacity = battery_capacity  # in kWh

    def charge(self):
        return "The battery is charging."


# Child Class inheriting from BOTH Vehicle and ElectricDevice
class ElectricCar(Vehicle, ElectricDevice):
    def __init__(self, n_wheels, n_seats, battery_capacity, model):
        print("Init of ElectricCar")
        # Explicitly calling the __init__ of both parent classes
        Vehicle.__init__(self, n_wheels, n_seats)
        ElectricDevice.__init__(self, battery_capacity)

        self.model = model

    def get_details(self):
        return f"{self.model} has {self.n_wheels} wheels, {self.n_seats} seats, and a {self.battery_capacity}kWh battery."


# Creating an instance of the child class
ec = ElectricCar(4, 5, 75, "Tesla Model 3")

print("\n--- Output ---")
print(ec.get_details())
print(ec.drive())  # Inherited from Vehicle
print(ec.charge())  # Inherited from ElectricDevice
print(ec.__dict__)
