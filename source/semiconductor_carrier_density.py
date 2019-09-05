import constants as const
from kelvin import Kelvin
from density import Density, CubicMeters
from carrier_mass import CarrierMass
from math import pi

class SemiconductorCarrierMasses:
    def __init__(self, stateDensity: CarrierMass, conductivity: CarrierMass):
        self.stateDensity = stateDensity
        self.conductivity = conductivity

    @classmethod
    def silicon(cls):
        return SemiconductorCarrierMasses(
            CarrierMass.fromRestingElectronMassRatio(1.08, 0.811),
            CarrierMass.fromRestingElectronMassRatio(0.26, 0.386))

    @classmethod
    def germanium(cls):
        return SemiconductorCarrierMasses(
            CarrierMass.fromRestingElectronMassRatio(0.55, 0.37),
            CarrierMass.fromRestingElectronMassRatio(0.12, 0.21))

        
class IntrinsicSemiconductorStateDensity:
    @classmethod
    def valenceBand(cls, carrierMass: CarrierMass, kelvin: Kelvin):
        return cls.fromCarrierMass(carrierMass.hole, kelvin)

    @classmethod
    def conductionBand(cls, carrierMass: CarrierMass, kelvin: Kelvin):
        return cls.fromCarrierMass(carrierMass.electron, kelvin)

    @classmethod
    def fromCarrierMass(cls, mass: float, kelvin: Kelvin):
        carriersPerCubicMeter = CubicMeters(2*(2*pi * mass * const.k * kelvin.kelvin / const.h**2)**(3/2))
        return Density(carriersPerCubicMeter)
