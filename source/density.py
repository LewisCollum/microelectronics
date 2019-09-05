from __future__ import annotations

class CubicMeters:
    def __init__(self, cubicMeters):
        self.cubicMeters = cubicMeters

    def asCubicCentimeters(self) -> CubicCentimeters:
        return CubicCentimeters(self.cubicMeters / 10**6)
        
class CubicCentimeters:
    def __init__(self, cubicCentimeters):
        self.cubicCentimeters = cubicCentimeters

    def asCubicMeters(self) -> CubicMeters:
        return CubicMeters(self.cubicCentimeters * 10**6) 

class Density:
    def __init__(self, partsPerCubicMeter: CubicMeters):
        self.perCubicMeter = partsPerCubicMeter

    @property
    def perCubicCentimeter(self) -> CubicCentimeters:
        return self.perCubicMeter.asCubicCentimeters()

    @classmethod
    def fromPartsPerCubicMeter(partsPerCubicMeter: CubicMeters) -> Density:
        return Density(partsPerCubicMeter)

    @classmethod
    def fromPartsPerCubicCentimeter(partsPerCubicCentimeter: CubicCentimeters) -> Density:
        return Density(partsPerCubicCentimeter.asCubicMeters())
