class Kelvin:
    celsiusOffset = 273.15
    
    def __init__(self, kelvin):
        self.kelvin = kelvin

    @property
    def celsius(self):
        return self.kelvin - Kelvin.celsiusOffset
    
    @classmethod
    def fromCelsius(cls, celsius):
        return Kelvin(celsius+Kelvin.celsiusOffset)
