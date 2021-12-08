from enum import Enum


class Instrument(Enum):
    tenors = "tenors"
    snare = "snare"
    bass = "bass"
    cymbals = "cymbal"


class Year(Enum):
    freshman = "freshman"
    sophomore = "sophomore"
    junior = "junior"
    senior = "senior"
    alumnus = "alumnus"