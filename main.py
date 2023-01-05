from solar_cell import *
from material import *
from mode import *
from spec import *
from angle import *
import pandas as pd


class Main :
    ####################################################################
    ##                             Type                               ##
    ####################################################################
    sw280 = Type (280,39.5,31.2,9.71,9.07,0.167)
    sw285 = Type (285,39.7,31.3,9.84,9.20,0.17)
    sw290 = Type (290,39.9,31.4,9.97,9.33,0.173)
    sw295 = Type (295,40.0,31.5,10.10,9.45,0.1759)
    ####################################################################

    ####################################################################
    ##                            Material                            ##
    ####################################################################
    Cu = Material(0,4.7)
    Ag = Material(0,4.26)
    Zn = Material (0,4.3) 
    Si = Material (1.12,0)
    Am_Si = Material(1.75,0)
    CdTe = Material(1.5,0)
    ####################################################################
    def __init__(self) -> None:
        pass

    
    def calculate_latitude(self):
        print ("####################################################################")
        print ("##                          Latitude                              ##")
        print ("####################################################################")
        city_name = input("Input the city name: ")
        locat = pd.read_csv('C:\College Task\Smt 5\OOP\software design final\cities15000.csv')
        if city_name not in locat['name'].values:
            print ("Your city is not in our automated list")
            lat = float(input("Input the latitude: "))
        else :
            cit_name = locat[locat['name']==city_name].index.values[0]
            lat = (locat.loc[cit_name,'latitude'])

        abs_lat = abs(float(lat))
        return abs_lat

    def select_mode(self):
        print ("####################################################################")
        print ("##                          Mode                                  ##")
        print ("####################################################################")
        print ("MODE:\n 0.STC : When the temperature lower or equal to 25\n 1.NOTC : When the temperature higher than 25")
        a = int(input('Choose Mode (0/1): '))
        if a == 0:
            n = Mode('STC')
        elif a == 1:
            n = Mode('NOCT')

        return n


    def weather_selection(self,latitude):
        if latitude > 23.5 : 
            print("Weather:\n S : APPLIED FOR SUMMER OR SPRING\n W : APPLIED FOR FALL AND WINTER")
            x = input('Choose Weather (S/W): ')
            if x.upper() == 'S':
                weather = 'S'
            elif x.upper() == 'W':
                weather = 'W'
        elif latitude <= 23.5 :
            weather = "S"

        return weather


    def create_area(self):
        width = float(input("Input your solar cell width in meter: ")) #input the width of solar cell (in meter)
        length = float(input("Input your solar cell length in meter: ")) #input the length of solar cell (in meter)
        area = Area(length,width)

        return area


    def count_operation_time(self):
        start_hour = int(input("Input the start time (in 24 hours system) : ")) #input the start Hour (format 24 Hours)
        stop_hour = int(input("Input the stop time (in 24 hours system) : ")) #input stop hour (format 24 Hours)
        operation_time = Operation_time(start_hour,stop_hour)

        return operation_time

    def output(self):
        latitude = self.calculate_latitude()
        weather = self.weather_selection(latitude)
        mode = self.select_mode()
        area = self.create_area()
        operation_time= self.count_operation_time()
        angle = Angle(latitude,weather)
        Power_input = 1000 #input the power counted from the sun
        light_freq = 4.15*10**18 #input the light freq
        material = Main.Si
        type_cell = Main.sw280
        solar_cell_1 = Solar_cell(angle.ideal_angle(),operation_time.op_time(),area.area(),material,type_cell,mode,Power_input,light_freq)
        print("####################################################################")
        print("##                             OUTPUT                             ##")
        print("####################################################################")
        print(f"Angle : {round(solar_cell_1.angle,2)} degree")
        print(f"Operation Time : {solar_cell_1.operation_time} hours")
        print(f"Area of Solar cell : {round(solar_cell_1.area,2)} sqm")
        print(f"Solar Cell Operating Mode : {solar_cell_1.mode}")
        min_freq = "{:e}".format(solar_cell_1.material.Min_frequency())
        print(f"Minimum Frequency to activate the cell :{min_freq} Hz")
        print(f"Solar Cell Power Output: {round(solar_cell_1.count_output(),2)} Watt")
        print(f"Power Output in a Day : {round(solar_cell_1.Power_output_in_a_day(),2)} Wh")
        
    def Run(self):
        self.output()

main = Main()
main.Run()