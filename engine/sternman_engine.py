#from abc import ABC

from car import Car


class SternmanEngine(Car):
    def __init__(self, current_date, warning_light_is_on):
        super().__init__(current_date)
        self.warning_light_is_on = warning_light_is_on
        
    def needs_service(self):
        return self.warning_light_is_on
