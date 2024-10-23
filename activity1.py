class vehicle:
    def __init__(self, name, max_speed, mileage):
     self.name = name
     self.max_speed = max_speed
     self.mileage = mileage
class bus(vehicle):
   pass
school_bus = bus("bolan", 180, 9)
print("vehicle name: ", school_bus.name, "\nvehicle max speed: ", school_bus.max_speed, "\nvehicle mileage: ", school_bus.mileage)