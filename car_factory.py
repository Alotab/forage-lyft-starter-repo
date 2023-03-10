from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire


class CarFactory:

    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire1 = CarriganTire(array)
        tire2 = OctoprimeTire(array)
        car = Car(engine, battery, tire1, tire2)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire1 = CarriganTire(array)
        tire2 = OctoprimeTire(array)
        car = Car(engine, battery, tire1, tire2)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire1 = CarriganTire(array)
        tire2 = OctoprimeTire(array)
        car = Car(engine, battery, tire1, tire2)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire1 = CarriganTire(array)
        tire2 = OctoprimeTire(array)
        car = Car(engine, battery, tire1, tire2)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire1 = CarriganTire(array)
        tire2 = OctoprimeTire(array)
        car = Car(engine, battery, tire1, tire2)
        return car