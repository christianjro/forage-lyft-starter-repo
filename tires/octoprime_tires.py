from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        wear_sensors_score = sum(self.wear_sensors)
        if wear_sensors_score >= 3:
            return True
        else:
            return False