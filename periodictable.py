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


type ATOMIC_NUMBER = PeriodicTable | int


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
    atomic_mass: float
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

    @staticmethod
    def create_element(atomic_number: PeriodicTable | int):
        match (atomic_number):
            case 1 | PeriodicTable.HYDROGEN:
                return Element("Hydrogen", PeriodicTable.HYDROGEN,
                               "H", 1, NaturalOccurence.PRIMODIAL)
            case 2 | PeriodicTable.HELIUM:
                return Element("Helium", PeriodicTable.HELIUM,
                               "HE", 1, NaturalOccurence.PRIMODIAL)
            case 3 | PeriodicTable.LITHIUM:
                return Element("Lithium", PeriodicTable.LITHIUM,
                               "LI", 1, NaturalOccurence.PRIMODIAL)
            case 4 | PeriodicTable.BERYLLIUM:
                return Element("Beryllium", PeriodicTable.BERYLLIUM,
                               "BE", 1, NaturalOccurence.PRIMODIAL)
            case 5 | PeriodicTable.BORON:
                return Element("Boron", PeriodicTable.BORON,
                               "B", 1, NaturalOccurence.PRIMODIAL)
            case 6 | PeriodicTable.CARBON:
                return Element("Carbon", PeriodicTable.CARBON,
                               "C", 1, NaturalOccurence.PRIMODIAL)
            case 7 | PeriodicTable.NITROGEN:
                return Element("Nitrogen", PeriodicTable.NITROGEN,
                               "N", 1, NaturalOccurence.PRIMODIAL)
            case 8 | PeriodicTable.OXYGEN:
                return Element("Oxygen", PeriodicTable.OXYGEN,
                               "O", 1, NaturalOccurence.PRIMODIAL)
            case 9 | PeriodicTable.FLUORINE:
                return Element("Fluorine", PeriodicTable.FLUORINE,
                               "F", 1, NaturalOccurence.PRIMODIAL)
            case 10 | PeriodicTable.NEON:
                return Element("Neon", PeriodicTable.NEON,
                               "NE", 1, NaturalOccurence.PRIMODIAL)
            case 11 | PeriodicTable.SODIUM:
                return Element("Sodium", PeriodicTable.SODIUM,
                               "NA", 1, NaturalOccurence.PRIMODIAL)
            case 12 | PeriodicTable.MAGNESIUM:
                return Element("Magnesium", PeriodicTable.MAGNESIUM,
                               "MG", 1, NaturalOccurence.PRIMODIAL)
            case 13 | PeriodicTable.ALUMNIUM:
                return Element("Alumnium", PeriodicTable.ALUMNIUM,
                               "AL", 1, NaturalOccurence.PRIMODIAL)
            case 14 | PeriodicTable.SILICON:
                return Element("Silicon", PeriodicTable.SILICON,
                               "SI", 1, NaturalOccurence.PRIMODIAL)
            case 15 | PeriodicTable.PHOSPHORUS:
                return Element("Phosphorus", PeriodicTable.PHOSPHORUS,
                               "P", 1, NaturalOccurence.PRIMODIAL)
            case 16 | PeriodicTable.SULFUR:
                return Element("Sulfur", PeriodicTable.SULFUR,
                               "S", 1, NaturalOccurence.PRIMODIAL)
            case 17 | PeriodicTable.CHLORINE:
                return Element("Chlorine", PeriodicTable.CHLORINE,
                               "Cl", 1, NaturalOccurence.PRIMODIAL)
            case 18 | PeriodicTable.ARGON:
                return Element("Argon", PeriodicTable.ARGON,
                               "Ar", 1, NaturalOccurence.PRIMODIAL)
            case 19 | PeriodicTable.POTASSIUM:
                return Element("Potassium", PeriodicTable.POTASSIUM,
                               "K", 1, NaturalOccurence.PRIMODIAL)
            case 20 | PeriodicTable.CALCIUM:
                return Element("Calcium", PeriodicTable.CALCIUM,
                               "CA", 1, NaturalOccurence.PRIMODIAL)
            case 21 | PeriodicTable.SCANDIUM:
                return Element("Scandium", PeriodicTable.SCANDIUM,
                               "SC", 1, NaturalOccurence.PRIMODIAL)
            case 22 | PeriodicTable.TITANIUM:
                return Element("Titanium", PeriodicTable.TITANIUM,
                               "TI", 1, NaturalOccurence.PRIMODIAL)
            case 23 | PeriodicTable.VANADIUM:
                return Element("Vanadium", PeriodicTable.VANADIUM,
                               "V", 1, NaturalOccurence.PRIMODIAL)
            case 24 | PeriodicTable.CHROMIUM:
                return Element("Chromium", PeriodicTable.CHROMIUM,
                               "CR", 51.996, NaturalOccurence.PRIMODIAL)
            case 25 | PeriodicTable.MANGANESE:
                return Element("Manganese", PeriodicTable.MANGANESE,
                               "MN", 54.938, NaturalOccurence.PRIMODIAL)
            case 26 | PeriodicTable.IRON:
                return Element("Iron", PeriodicTable.IRON,
                               "FE", 55.845, NaturalOccurence.PRIMODIAL)
            case 27 | PeriodicTable.COBALT:
                return Element("Cobalt", PeriodicTable.COBALT,
                               "CO", 58.933, NaturalOccurence.PRIMODIAL)
            case 28 | PeriodicTable.NICKEL:
                return Element("Nickel", PeriodicTable.NICKEL,
                               "NI", 58.693, NaturalOccurence.PRIMODIAL)
            case 29 | PeriodicTable.COPPER:
                return Element("Copper", PeriodicTable.COPPER,
                               "CU", 63.546, NaturalOccurence.PRIMODIAL)
            case 30 | PeriodicTable.ZINC:
                return Element("Zinc", PeriodicTable.ZINC,
                               "ZN", 65.38, NaturalOccurence.PRIMODIAL)
            case 31 | PeriodicTable.GALLIUM:
                return Element("Gallium", PeriodicTable.GALLIUM,
                               "GA", 69.723, NaturalOccurence.PRIMODIAL)
            case 32 | PeriodicTable.GERMANIUM:
                return Element("Germanium", PeriodicTable.GERMANIUM,
                               "GE", 72.630, NaturalOccurence.PRIMODIAL)
            case 33 | PeriodicTable.ARSENIC:
                return Element("Arsenic", PeriodicTable.ARSENIC,
                               "AS", 74.922, NaturalOccurence.PRIMODIAL)
            case 34 | PeriodicTable.SELENIUM:
                return Element("Selenium", PeriodicTable.SELENIUM,
                               "SE", 78.791, NaturalOccurence.PRIMODIAL)
            case 35 | PeriodicTable.BROMINE:
                return Element("Bromine", PeriodicTable.BROMINE,
                               "BR", 79.904, NaturalOccurence.PRIMODIAL)
            case 36 | PeriodicTable.KRYPTON:
                return Element("Krypton", PeriodicTable.KRYPTON,
                               "KR", 83.798, NaturalOccurence.PRIMODIAL)
            case 37 | PeriodicTable.RUBIDIUM:
                return Element("Rubidium", PeriodicTable.RUBIDIUM,
                               "RB", 85.468, NaturalOccurence.PRIMODIAL)
            case 38 | PeriodicTable.STRONTIUM:
                return Element("Strontium", PeriodicTable.STRONTIUM,
                               "SR", 87.62, NaturalOccurence.PRIMODIAL)
            case 39 | PeriodicTable.YTTRIUM:
                return Element("Yttrium", PeriodicTable.YTTRIUM,
                               "Y", 88.906, NaturalOccurence.PRIMODIAL)
            case 40 | PeriodicTable.ZIRCONIUM:
                return Element("Zirconium", PeriodicTable.ZIRCONIUM,
                               "ZR", 91.224, NaturalOccurence.PRIMODIAL)
            case 41 | PeriodicTable.NIOBIUM:
                return Element("Niobium", PeriodicTable.NIOBIUM,
                               "NB", 92.906, NaturalOccurence.PRIMODIAL)
            case 42 | PeriodicTable.MOLYBDENIUM:
                return Element("Molybdenium", PeriodicTable.MOLYBDENIUM,
                               "MO", 95.95, NaturalOccurence.PRIMODIAL)
            case 43 | PeriodicTable.TECHNETIUM:
                return Element("Technetium", PeriodicTable.TECHNETIUM,
                               "TC", 97, NaturalOccurence.PRIMODIAL)
            case 44 | PeriodicTable.RUTHENIUM:
                return Element("Ruthenium", PeriodicTable.RUTHENIUM,
                               "RU", 101.07, NaturalOccurence.PRIMODIAL)
            case 45 | PeriodicTable.RHODIUM:
                return Element("Rhodium", PeriodicTable.RHODIUM,
                               "RH", 102.91, NaturalOccurence.PRIMODIAL)
            case 46 | PeriodicTable.PALLADIUM:
                return Element("Palladium", PeriodicTable.PALLADIUM,
                               "PD", 106.42, NaturalOccurence.PRIMODIAL)
            case 47 | PeriodicTable.SILVER:
                return Element("Silver", PeriodicTable.SILVER,
                               "AG", 107.87, NaturalOccurence.PRIMODIAL)
            case 48 | PeriodicTable.CADMIUM:
                return Element("Cadmium", PeriodicTable.CADMIUM,
                               "CD", 112.41, NaturalOccurence.PRIMODIAL)
            case 49 | PeriodicTable.INDIUM:
                return Element("Indium", PeriodicTable.INDIUM,
                               "IN", 114.82, NaturalOccurence.PRIMODIAL)
            case 50 | PeriodicTable.TIN:
                return Element("Tin", PeriodicTable.TIN,
                               "SN", 118.71, NaturalOccurence.PRIMODIAL)
            case 51 | PeriodicTable.ANTIMONY:
                return Element("Antimony", PeriodicTable.ANTIMONY,
                               "SB", 121.76, NaturalOccurence.PRIMODIAL)
            case 52 | PeriodicTable.TELLURIUM:
                return Element("Tellurium", PeriodicTable.TELLURIUM,
                               "TE", 127.60, NaturalOccurence.PRIMODIAL)
            case 53 | PeriodicTable.IODINE:
                return Element("Iodine", PeriodicTable.IODINE,
                               "I", 126.90, NaturalOccurence.PRIMODIAL)
            case 54 | PeriodicTable.XENON:
                return Element("Xenon", PeriodicTable.XENON,
                               "XE", 131.29, NaturalOccurence.PRIMODIAL)
            case 55 | PeriodicTable.CAESIUM:
                return Element("Caesium", PeriodicTable.CAESIUM,
                               "CS", 132.91, NaturalOccurence.PRIMODIAL)
            case 56 | PeriodicTable.BARIUM:
                return Element("Barium", PeriodicTable.BARIUM,
                               "BA", 137.33, NaturalOccurence.PRIMODIAL)
            case 57 | PeriodicTable.LANTHANIUM:
                return Element("Lanthanium", PeriodicTable.LANTHANIUM,
                               "LA", 138.91, NaturalOccurence.PRIMODIAL)
            case 58 | PeriodicTable.CERIUM:
                return Element("Cerium", PeriodicTable.CERIUM,
                               "CE", 140.12, NaturalOccurence.PRIMODIAL)
            case 59 | PeriodicTable.PRASEODYMIUM:
                return Element("Praseodymium", PeriodicTable.PRASEODYMIUM,
                               "PR", 140.91, NaturalOccurence.PRIMODIAL)
            case 60 | PeriodicTable.NEODYMIUM:
                return Element("Neodymium", PeriodicTable.NEODYMIUM,
                               "ND", 144.24, NaturalOccurence.PRIMODIAL)
            case 61 | PeriodicTable.PROMETHIUM:
                return Element("Promethium", PeriodicTable.PROMETHIUM,
                               "PM", 145, NaturalOccurence.PRIMODIAL)
            case 62 | PeriodicTable.SAMARIUM:
                return Element("Samarium", PeriodicTable.SAMARIUM,
                               "SM", 150.36, NaturalOccurence.PRIMODIAL)
            case 63 | PeriodicTable.EUROPIUM:
                return Element("Europium", PeriodicTable.EUROPIUM,
                               "EU", 151.96, NaturalOccurence.PRIMODIAL)
            case 64 | PeriodicTable.GADOLINIUM:
                return Element("Gadolinium", PeriodicTable.GADOLINIUM,
                               "GD", 157.25, NaturalOccurence.PRIMODIAL)
            case 65 | PeriodicTable.TERBIUM:
                return Element("Terbium", PeriodicTable.TERBIUM,
                               "TB", 158.93, NaturalOccurence.PRIMODIAL)
            case 66 | PeriodicTable.DYSPROSIUM:
                return Element("Dysprosium", PeriodicTable.DYSPROSIUM,
                               "DY", 162.50, NaturalOccurence.PRIMODIAL)
            case 67 | PeriodicTable.HOLMIUM:
                return Element("Holmium", PeriodicTable.HOLMIUM,
                               "HO", 164.93, NaturalOccurence.PRIMODIAL)
            case 68 | PeriodicTable.ERBIUM:
                return Element("Erbium", PeriodicTable.ERBIUM,
                               "ER", 167.26, NaturalOccurence.PRIMODIAL)
            case 69 | PeriodicTable.THULIUM:
                return Element("Thulium", PeriodicTable.THULIUM,
                               "TM", 168.93, NaturalOccurence.PRIMODIAL)
            case 70 | PeriodicTable.YTTERBIUM:
                return Element("Ytterbium", PeriodicTable.YTTERBIUM,
                               "YB", 173.05, NaturalOccurence.PRIMODIAL)
            case 71 | PeriodicTable.LUTETIUM:
                return Element("Lutetium", PeriodicTable.LUTETIUM,
                               "LU", 174.97, NaturalOccurence.PRIMODIAL)
            case 72 | PeriodicTable.HAFNIUM:
                return Element("Hafnium", PeriodicTable.HAFNIUM,
                               "HF", 178.49, NaturalOccurence.PRIMODIAL)
            case 73 | PeriodicTable.TANTAIUM:
                return Element("Tantaium", PeriodicTable.TANTAIUM,
                               "TA", 180.95, NaturalOccurence.PRIMODIAL)
            case 74 | PeriodicTable.TUNGSTEN:
                return Element("Tungsten", PeriodicTable.TUNGSTEN,
                               "W", 183.84, NaturalOccurence.PRIMODIAL)
            case 75 | PeriodicTable.RHENIUM:
                return Element("Rhenium", PeriodicTable.RHENIUM,
                               "RE", 186.21, NaturalOccurence.PRIMODIAL)
            case 76 | PeriodicTable.OSMIUM:
                return Element("Osmium", PeriodicTable.OSMIUM,
                               "OS", 190.23, NaturalOccurence.PRIMODIAL)
            case 77 | PeriodicTable.IRIDIUM:
                return Element("Iridium", PeriodicTable.IRIDIUM,
                               "IR", 192.22, NaturalOccurence.PRIMODIAL)
            case 78 | PeriodicTable.PLATINIUM:
                return Element("Plainium", PeriodicTable.PLATINIUM,
                               "PT", 195.08, NaturalOccurence.PRIMODIAL)
            case 79 | PeriodicTable.GOLD:
                return Element("Gold", PeriodicTable.GOLD,
                               "AU", 196.97, NaturalOccurence.PRIMODIAL)
            case 80 | PeriodicTable.MERCURY:
                return Element("Mercury", PeriodicTable.MERCURY,
                               "HG", 200.59, NaturalOccurence.PRIMODIAL)
            case 81 | PeriodicTable.THALLIUM:
                return Element("Thallium", PeriodicTable.THALLIUM,
                               "TL", 204.38, NaturalOccurence.PRIMODIAL)
            case 82 | PeriodicTable.LEAD:
                return Element("Lead", PeriodicTable.LEAD,
                               "PB", 207.2, NaturalOccurence.PRIMODIAL)
            case 83 | PeriodicTable.BISMUTH:
                return Element("Bismuth", PeriodicTable.BISMUTH,
                               "BI", 208.98, NaturalOccurence.PRIMODIAL)
            case 84 | PeriodicTable.POLONIUM:
                return Element("Polonium", PeriodicTable.POLONIUM,
                               "PO", 209, NaturalOccurence.DECAY)
            case 85 | PeriodicTable.ASTATINE:
                return Element("Astatine", PeriodicTable.ASTATINE,
                               "PO", 210, NaturalOccurence.DECAY)
            case 86 | PeriodicTable.RADON:
                return Element("Radon", PeriodicTable.RADON,
                               "RN", 222, NaturalOccurence.DECAY)
            case 87 | PeriodicTable.FRANCIUM:
                return Element("Francium", PeriodicTable.FRANCIUM,
                               "FR", 223, NaturalOccurence.DECAY)
            case 88 | PeriodicTable.RADIUM:
                return Element("Radium", PeriodicTable.RADIUM,
                               "RA", 226, NaturalOccurence.DECAY)
            case 89 | PeriodicTable.ACTINIUM:
                return Element("Actinium", PeriodicTable.ACTINIUM,
                               "AC", 227, NaturalOccurence.DECAY)
            case 90 | PeriodicTable.THORIUM:
                return Element("Thorium", PeriodicTable.THORIUM,
                               "TH", 232.04, NaturalOccurence.PRIMODIAL)
            case 91 | PeriodicTable.PROTACTINIUM:
                return Element("Protactinium", PeriodicTable.PROTACTINIUM,
                               "PA", 231.04, NaturalOccurence.DECAY)
            case 92 | PeriodicTable.URANIUM:
                return Element("Uranium", PeriodicTable.URANIUM,
                               "U", 238.03, NaturalOccurence.PRIMODIAL)
            case 93 | PeriodicTable.NEPTUNIUM:
                return Element("Neptunium", PeriodicTable.NEPTUNIUM,
                               "NP", 237, NaturalOccurence.DECAY)
            case 94 | PeriodicTable.NEPTUNIUM:
                return Element("Neptunium", PeriodicTable.NEPTUNIUM,
                               "NP", 237, NaturalOccurence.DECAY)
            case 95 | PeriodicTable.AMERICIUM:
                return Element("Americium", PeriodicTable.AMERICIUM,
                               "AM", 243, NaturalOccurence.SYNTHETIC)
            case 96 | PeriodicTable.CURIUM:
                return Element("Curium", PeriodicTable.CURIUM,
                               "CM", 247, NaturalOccurence.SYNTHETIC)
            case 97 | PeriodicTable.BERKELIUM:
                return Element("Berkelium", PeriodicTable.BERKELIUM,
                               "BK", 247, NaturalOccurence.SYNTHETIC)
            case 98 | PeriodicTable.CALIFORNIUM:
                return Element("Californium", PeriodicTable.CALIFORNIUM,
                               "CF", 251, NaturalOccurence.SYNTHETIC)
            case 99 | PeriodicTable.EINSTEINIUM:
                return Element("Californium", PeriodicTable.CALIFORNIUM,
                               "ES", 252, NaturalOccurence.SYNTHETIC)
            case 100 | PeriodicTable.FERMIUM:
                return Element("Fermium", PeriodicTable.FERMIUM,
                               "FM", 257, NaturalOccurence.SYNTHETIC)
            case 101 | PeriodicTable.MENDELEVIUM:
                return Element("Mendelevium", PeriodicTable.MENDELEVIUM,
                               "MD", 258, NaturalOccurence.SYNTHETIC)
            case 102 | PeriodicTable.NOBELIUM:
                return Element("Nobelium", PeriodicTable.NOBELIUM,
                               "NO", 259, NaturalOccurence.SYNTHETIC)
            case 103 | PeriodicTable.LAWRENCIUM:
                return Element("Lawrencium", PeriodicTable.LAWRENCIUM,
                               "LR", 266, NaturalOccurence.SYNTHETIC)
            case 104 | PeriodicTable.RUTHERFORDIUM:
                return Element("Rutherfordium", PeriodicTable.RUTHERFORDIUM,
                               "RF", 267, NaturalOccurence.SYNTHETIC)
            case 105 | PeriodicTable.DUBNIUM:
                return Element("Dubnium", PeriodicTable.DUBNIUM,
                               "DB", 268, NaturalOccurence.SYNTHETIC)
            case 106 | PeriodicTable.SEABORGIUM:
                return Element("Seaborgium", PeriodicTable.SEABORGIUM,
                               "SG", 269, NaturalOccurence.SYNTHETIC)
            case 107 | PeriodicTable.BOHRIUM:
                return Element("Bohrium", PeriodicTable.BOHRIUM,
                               "BH", 270, NaturalOccurence.SYNTHETIC)
            case 108 | PeriodicTable.HASSIUM:
                return Element("Hassium", PeriodicTable.HASSIUM,
                               "HS", 269, NaturalOccurence.SYNTHETIC)
            case 109 | PeriodicTable.MEITNERIUM:
                return Element("Meitnerium", PeriodicTable.MEITNERIUM,
                               "MT", 278, NaturalOccurence.SYNTHETIC)
            case 110 | PeriodicTable.DARMSTADTIUM:
                return Element("Darmstadtium", PeriodicTable.DARMSTADTIUM,
                               "DS", 281, NaturalOccurence.SYNTHETIC)
            case 111 | PeriodicTable.ROENTGENIUM:
                return Element("Roentgenium", PeriodicTable.ROENTGENIUM,
                               "RG", 282, NaturalOccurence.SYNTHETIC)
            case 112 | PeriodicTable.COPERNICIUM:
                return Element("Copernicium", PeriodicTable.COPERNICIUM,
                               "CN", 285, NaturalOccurence.SYNTHETIC)
            case 113 | PeriodicTable.NIHONIUM:
                return Element("Nihonium", PeriodicTable.NIHONIUM,
                               "NH", 286, NaturalOccurence.SYNTHETIC)
            case 114 | PeriodicTable.FLEROVIUM:
                return Element("Flerovium", PeriodicTable.FLEROVIUM,
                               "FL", 289, NaturalOccurence.SYNTHETIC)
            case 115 | PeriodicTable.MOSCOVIUM:
                return Element("Moscovium", PeriodicTable.MOSCOVIUM,
                               "MC", 290, NaturalOccurence.SYNTHETIC)
            case 116 | PeriodicTable.LIVERMORIUM:
                return Element("Livermorium", PeriodicTable.LIVERMORIUM,
                               "LV", 293, NaturalOccurence.SYNTHETIC)
            case 117 | PeriodicTable.TENNESSINE:
                return Element("Tennessine", PeriodicTable.TENNESSINE,
                               "TS", 294, NaturalOccurence.SYNTHETIC)
            case 118 | PeriodicTable.OGANESSON:
                return Element("Oganesson", PeriodicTable.OGANESSON,
                               "OG", 294, NaturalOccurence.SYNTHETIC)
