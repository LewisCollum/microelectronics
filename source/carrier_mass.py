from __future__ import annotations
import constants as const

class CarrierMass:
    def __init__(self, electronMass, holeMass):
        self.electron = electronMass
        self.hole = holeMass

    @classmethod
    def fromRestingElectronMassRatio(cls, electronMassRatio, holeMassRatio) -> CarrierMass:
        return CarrierMass(
            electronMass = electronMassRatio*const.restingElectronMass,
            holeMass = holeMassRatio*const.restingElectronMass)
