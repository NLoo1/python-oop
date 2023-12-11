"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start-1

    def generate(self):
        """Increases start by 1 and returns new start number"""
        self.start+=1
        return self.start
    
    def __repr__(self):
        """ Returns repr of SerialGenerator"""
        return f"SerialGenerator {self.start}"

    def reset(self):
        """Sets serial number back to 99. Serial number is set to 99 to account for generate() adding +1"""
        self.start = 99

