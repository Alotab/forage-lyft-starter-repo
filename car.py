# from abc import ABC, abstractmethod
from car_factory import CarFactory


class Car(CarFactory):
    def __init__(self, current_date, last_service_date, last_service_mileage, array):
        super().__init__(current_date, last_service_date, last_service_mileage)
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.array = array
    

    def needs_service(self):
        pass

