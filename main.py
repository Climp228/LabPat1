class Car:

    def __init__(self, registrationNum, year: int, licenseNumber: str):
        self.registrationNum = registrationNum
        self.year = year
        self.licenseNumber = licenseNumber

        self.GearBox = GearBox
        self.CarModel = CarModel
        self.Engine = Engine
        self.Body = Body
        self.Suspension = Suspension
        self.Brake = Brake

    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def turnRight(self):
        pass

    def turnLeft(self):
        pass


class CarModel:
    def __init__(self, title: str):
        self.title = title


class Engine:
    def __init__(self, capacity: float, numberOfCylinders: int):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors: int):
        self.numberOfDoors = numberOfDoors


class Brake:
    def __init__(self, type: str):
        self.type = type

        self.Wheel = Wheel

    def apply(self):
        pass


class Suspension:
    def __init__(self, springRate: float):
        self.springRate = springRate

        self.Wheel = Wheel


class Wheel:
    def __init__(self, diameter: float):
        self.diameter = diameter

        self.Tire = Tire


class Tire:
    def __init__(self, width: float, airPressure: float):
        self.width = width
        self.airPressure = airPressure


class GearBox:
    def __init__(self, gearRatio: float, currentGear: int):
        self.gearRatio = gearRatio
        self.currentGear = currentGear

        self.GearBoxType = GearBoxType

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class GearBoxType:
    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks
