
#Count Area 
#output Area
class Area:
    def __init__(self,length,width):
        """
        Attributes from Area
        ------------------------------
        length = float
                    length of Area
        width = float
                    width of area
        """
        self.length = length
        self.width = width
    def area(self):
        """ 
        to determine the area value. 
        return input into the formula
        """
        return float(self.width * self.length)

#count Operation time
#Output operation time
class Operation_time :
    def __init__(self,start_hour,stop_hour):
        """
        Attributes from Operation Time
        ------------------------------
        start_hour = int
                    start_hour of Operation_time
        stop_hour = int
                    start_hour of Operation_time
        """
        self.start_hour = start_hour
        self.stop_hour = stop_hour
    def op_time(self):
        """
        to determine the op_time 
        return input into the formula
        """
        return int(self.stop_hour - self.start_hour)

#Spec of solar panel
class Type:
    def __init__(self,max_PO,oc_volt,mpp_volt,sc_current,mpp_current,efficiency):
        """
        Attributes from Type
        ------------------------------
        max_PO = int
                    max_PO of Type
        oc_volt = float
                    oc_volt of Type
        mpp_volt = float
                    mpp_volt of Type
        sc_current = float
                    sc_current of Type
        mpp_current = float
                    mpp_current of Type
        efficiency = float
                    efficiency of Type
        """
        self.__max_PO = max_PO
        self.__oc_volt = oc_volt
        self.__mpp_volt = mpp_volt
        self.__sc_current = sc_current
        self.__mpp_current = mpp_current
        self.__efficiency = efficiency

    
    def max_output (self):
        """ returns a printable representation of the object max_output """
        return self.__max_PO
    
    def efficiency (self):
        """ returns a printable representation of the object efficiency """
        return self.__efficiency
