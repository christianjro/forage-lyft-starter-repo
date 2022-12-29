from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        for sensor in self.wear_sensors:
            if sensor >= 0.9:
                return True
        return False