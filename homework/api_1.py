from __future__ import annotations
import math
import pint

unit = pint.UnitRegistry()

def densityOfStates(materialConstant: float, kelvinOfSystem: float) -> float:
    return materialConstant/unit.kelvin**(3/2)/unit.centimeters**3 * kelvinOfSystem**(3/2)

class Boltzmann:        
    @classmethod
    def probability(cls, stateEnergy: float, kelvinOfSystem: float) -> float:
        return math.exp(-stateEnergy*unit.eV/(kelvinOfSystem * unit.boltzmann_constant))

class Silicon:
    densityOfStatesMaterialConstant = 7.3e15
    densityOfAtoms = 5e22
    holeMobility = 480 * unit.centimeters**2 / (unit.volts*unit.seconds)

    @classmethod
    def intrinsicConcentrationFromKelvin(cls, kelvin: float) -> float:
        siliconDensityOfStates = densityOfStates(
            materialConstant=Silicon.densityOfStatesMaterialConstant,
            kelvinOfSystem=kelvin)
        distribution = Boltzmann.probability(
            stateEnergy=1.12,
            kelvinOfSystem=kelvin)**(1/2)
        return siliconDensityOfStates * distribution
