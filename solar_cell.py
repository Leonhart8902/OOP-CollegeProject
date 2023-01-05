class Solar_cell:
    def __init__(self,angle,operation_time,area,material,type,mode,power_input,light_freq,temp =0):
        """
        Attributes from Solar_cell
        ------------------------------
        angle = float
                    length of Solar_cell
        operation_time = float
                    operation_time of Solar_cell
        area = int
                    area of of Solar_cell
        material = str
                    material of of Solar_cell
        type = str
                    type of of Solar_cell
        mode = str
                    mode of of Solar_cell
        power_input = int
                    power_input of Solar_cell
        light_freq = int
                    light_freq of Solar_cell
        """
        self.angle = angle
        self.operation_time = operation_time
        self.area = area
        self.material = material
        self.type = type
        self.mode = mode
        self.power_input = power_input
        self.light_freq = light_freq
        self.temp = temp
    
    def count_output(self):
        """
        to count the output
        if material Min_frequency < light freq
            if  mode = STC
                temp <= 25
                Power_input_max = 1000
                    if power_input > Power_input_max:
                        power_input = Power_input_max
                        the efficiency *1 and max_output *0.75
            
            if  mode = NOCT
                temp > 25
                Power_input_max = 800
                    if power_input > Power_input_max:
                        power_input = Power_input_max
                        the efficiency and max_output will be * 1
            
        Ps = power_input * area
        Power_output = Ps * efficiency
            if Power_output > Max_Output
            the Power_output = Max_Output
            return Power_output
            elif  if Min_frequency > light_freq:
                it will be return none

        """
        if self.material.Min_frequency() < self.light_freq:
            if self.mode == "STC" :
                self.temp <= 25
                Power_input_max = 1000
                if self.power_input > Power_input_max:
                    self.power_input = Power_input_max
                self.type.efficiency * 1
                self.type.max_output *1
            elif self.mode == "NOCT" :
                self.temp > 25
                Power_input_max = 800
                if self.power_input > Power_input_max:
                    self.power_input = Power_input_max
                self.type.efficiency * 1
                self.type.max_output * 0.75

            Max_Output = self.type.max_output()
            Ps = self.power_input * self.area
            Power_output = Ps*self.type.efficiency()
            if Power_output > Max_Output:
                Power_output = Max_Output
            return Power_output
        elif self.material.Min_frequency() > self.light_freq:
            return None
    
    def Power_output_in_a_day (self):
        """
        Count the Daily_power_output 
        return a printable representation of the object Daily_power_output
        """
        Daily_power_output = self.count_output()*self.operation_time
        return Daily_power_output