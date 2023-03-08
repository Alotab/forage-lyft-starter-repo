import unittest
from datetime import date


from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery




class TestCapuletEngine(unittest.TestCase):
    def test_needs_services(self):
        current_mileage = 5000
        last_service_mileage = 1200
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_need_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 7000
        last_service_mileage = 3400
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())




class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = 2018-12-10
        current_date = date.today()
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())



class TestSpindlerBattery(unittest.TestCase):
    def test_needs_servicer(self):
        last_service_date = 2020-12-10
        current_date = date.today()
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        


if __name__ == '__main__':
    unittest.main()
