class Mode:
    def __init__(self,op_mode=str):
        """Attributes from Mode
        ------------------------------
        op_mode = str
                    op_mode of Mode """
        self.mode = op_mode
    def __repr__(self) -> str:
        """returns a printable representation of the object mode
        If the value is 0 then it applies to STC while 1 applies to NOCT
        """
        return self.mode

#0 for STC
#1 for NOCT