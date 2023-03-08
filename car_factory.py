
class CarFactory:
    def __init__(self, current_date, last_service_date,last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = f'Thie is calliope: {current_date}, {last_service_date}, {current_mileage}, {last_service_mileage}'
        return calliope
       
    def create_palindrome(self,current_date, last_service_date, warning_light_is_on):
        palindrome = f'Thie is palindrome: {current_date}, {last_service_date}, {warning_light_is_on}'
        return palindrome
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = f'Thie is glissade: {current_date}, {last_service_date}, {current_mileage}, {last_service_mileage}'
        return glissade
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = f'Thie is thovex: {current_date}, {last_service_date}, {current_mileage}, {last_service_mileage}'
        return thovex