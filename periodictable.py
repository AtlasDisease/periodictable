# Created By: Brendan (@atlasdisease)
# Copyright: 2023
# Description: Periodic Table

# --- Imports --- #

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum, auto


# --- PeriodicTable Enum --- #

class PeriodicTable(IntEnum):
    HYDROGEN = auto()
    HELIUM = auto()
    LITHIUM = auto()
    BERYLLIUM = auto()
    BORON = auto()
    CARBON = auto()
    NITROGEN = auto()
    OXYGEN = auto()
    FLUORINE = auto()
    NEON = auto()
    SODIUM = auto()
    MAGNESIUM = auto()
    ALUMNIUM = auto()
    SILICON = auto()
    PHOSPHORUS = auto()
    SULFUR = auto()
    CHLORINE = auto()
    ARGON = auto()
    POTASSIUM = auto()
    CALCIUM = auto()
    SCANDIUM = auto()
    TITANIUM = auto()
    VANADIUM = auto()
    CHROMIUM = auto()
    MANGANESE = auto()
    IRON = auto()
    COBALT = auto()
    NICKEL = auto()
    COPPER = auto()
    ZINC = auto()
    GALLIUM = auto()
    GERMANIUM = auto()
    ARSENIC = auto()
    SELENIUM = auto()
    BROMINE = auto()
    KRYPTON = auto()
    RUBIDIUM = auto()
    STRONTIUM = auto()
    YTTBIUM = auto()
    ZIRCONIUM = auto()
    NIOBIUM = auto()
    MOLYBDENUM = auto()
    TECHNETIUM = auto()
    RUTHENIUM = auto()
    RHODIUM = auto()
    PALLADIUM = auto()
    SILVER = auto()
    CADMIUM = auto()
    INDIUM = auto()
    TIN = auto()
    ANTIMONY = auto()
    TELLURIUM = auto()
    IODINE = auto()
    XENON = auto()
    CAESIUM = auto()
    BARIUM = auto()
    LANTHANUM = auto()
    CERIUM = auto()
    PRASEODYMIUM = auto()
    NEODYMIUM = auto()
    PROMETHIUM = auto()
    SAMARIUM = auto()
    EUROPIUM = auto()
    GADOLINIUM =  auto()
    TERBIUM = auto()
    DYSPROSIUM = auto()
    HOLMIUM = auto()
    ERBIUM = auto()
    THULIUM = auto()
    YTTERBIUM = auto() 
    LUTETIUM = auto()
    HAFNIUM = auto()
    TANTALUM = auto()
    TUNGSTEN = auto()
    RHENIUM = auto()
    OSMIUM = auto()
    IRIDIUM = auto()
    PLATINUM = auto()
    GOLD = auto()
    MERCURY = auto()
    THALLIUM = auto()
    LEAD = auto()
    BISMUTH = auto()
    POLONIUM = auto()
    ASTATINE = auto()
    RADON = auto()   
    FRANCIUM = auto()
    RADIUM = auto()
    ACTINIUM = auto()
    THORIUM = auto()
    PROTACTINIUM = auto()
    URANIUM = auto()
    NEPTUNIUM = auto()
    PLUTONIUM = auto()
    AMERICIUM = auto()
    CURIUM = auto()
    BERKELIUM = auto()
    CALIFORNIUM = auto()
    EINSTEINIUM = auto()
    FERMIUM = auto()
    MENDELEVIUM = auto()
    NOBELIUM = auto()
    LAWRENCIUM = auto()
    RUTHERFORDIUM = auto()
    DUBNIUM = auto()
    SEABORGIUM = auto()
    BOHRIUM = auto()
    HASIUM = auto()
    MEITNERIUM = auto()
    DARMSTADIUM = auto()
    ROENTGENIUM = auto()
    COPERNICIUM = auto()
    NIHONIUM = auto()
    FLEROVIUM = auto()
    MOSCOVIUM = auto()
    LIVERMORIUM = auto()
    TENNESSINE = auto()
    OGANESSON = auto()

    def __str__(self):
        return self.name.title()


# --- AtomicTypes Class --- #

class AtomicTypes(IntEnum):
    ELECTRON = -1
    NEUTRON = 0
    PROTON = 1

    def __str__(self):
        return self.name.title()


# --- NaturalOccurence Enum --- #

class NaturalOccurence(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.title()
    
    PRIMODIAL = auto()
    DECAY = auto()
    SYNTHETIC = auto()


# --- Element Class --- #

@dataclass
class Element:
    name: str
    number: PeriodicTable
    abbreviation: str
    atomic_mass: int
    occurence: NaturalOccurence

    def __post_init__(self):
        self.abbreviation = self.abbreviation.title()

    def __str__(self) -> str:
        return self.name

    def __format__(self, format_spec = "") -> str:
        if "a" in format_spec or "A" in format_spec:
            return self.abbreviation    
        return str(self)

    def __int__(self) -> int:
        return self.number

    @property
    def abbrev(self) -> str:
        return self.abbreviation
    

# --- Testing --- #

if __name__ == "__main__":
    element = Element("Oganesson",
                      PeriodicTable.OGANESSON,
                      "OG",
                      294,
                      NaturalOccurence.SYNTHETIC)
    print(element, f"({element: a})")
    
