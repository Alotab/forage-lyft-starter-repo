# from abc import ABC

from car import Car


class CapuletEngine(Car):
    def __init__(self, current_date, last_service_date, last_service_mileage, current_mileage):
        super().__init__(current_date, last_service_date, last_service_mileage)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
