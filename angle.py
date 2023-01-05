class Angle :
    def __init__(self,latitude,weather="S"):
        assert weather == "S" or "N", "Error"
        """Attributes from Angle
        ------------------------------
        latitude = float
                    latitude of Angle
        weather = str
                    Work_function of Angle"""

        self.latitude = latitude
        self.weather = weather

    def is_equator(self):
        """
        to determine is equator or not equator
           if latitude is <= 23.5 it will return true
           elif latitude is > 23.5 it will return false
           else it will print error
        """
        if self.latitude <= 23.5:
            return True 
        elif self.latitude > 23.5 :
            return False 
        else :
            print ("ERROR")

    def ideal_angle(self):
        """
        to determine is the ideal angle or not ideal angle
        if the equator == true angle = 45
        return angle == 45
        elif equator == false
            if wheather == "S" angle = input into the formula
            return angle
            elif weather = "W" angle = input into the another formula
            return angle
        """
        if self.is_equator() == True :
            self.angle = 45
            return float(self.angle)
        elif self.is_equator() == False:
            if self.weather == "S":
                self.angle = (self.latitude*0.9)+29
                return float(self.angle)
            elif self.weather == "W":
                self.angle = (self.latitude*0.9)+23.5
                return float(self.angle)