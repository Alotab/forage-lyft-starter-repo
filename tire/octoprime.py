from tire.tire import Tire



class OctoprimeTire(Tire):
    def __init__(self, array):
        self.array = array

    sum = 0
    def needs_service(self):
        for i in self.array:
            sum = sum + i
        if sum >= 3:
            return True
        return False