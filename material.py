import scipy.constants as sp
class Material:
    def __init__(self, Bandgap_energy, work_function):
        """Attributes from Material
        ------------------------------
        Bandgap_Energy = float
                    Bandgap_Energy of Material
        Work_function = float
                    Work_function of Material"""
        self.Bandgap_energy = Bandgap_energy *sp.eV
        self.work_function = work_function * sp.eV
    def __repr__(self) -> float:
        """returns a printable representation of the object Min_Frequency"""
        return self.Min_frequency()

    def Is_semiconductor(self):
        """to determine is semiconductor or not semiconductor
           if bandgap_energy is 0 it will return true
           elif bandgap_energy is not 0 it will return false
           else it will print error"""
        if self.Bandgap_energy == 0:
            return True
        elif self.Bandgap_energy != 0:
            return False
        else:
            print("ERROR")

    def Min_frequency(self):
        """to determine minimum frequency
           if bandgap_energy is not 0:
                it will return F from bandgap_energy/p_constant
           and if work_function is not 0: 
                it will return F from work_function/p_constant
           else it will print error"""
        p_constant = sp.Planck
        if self.Bandgap_energy != 0:
            F = self.Bandgap_energy/p_constant
        elif self.work_function != 0:
            F = self.work_function/p_constant
        else:
            print('ERROR')
        return F

