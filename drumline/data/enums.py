"""
Union types used for Instrument and Year
so that they can have concrete types instead
of relying on raw numbers and strings.
"""

from enum import Enum


class Instrument(Enum):
    tenors = "tenors" """Tenor Drums (aka quads/quints)"""
    snare = "snare" """Snare Drum"""
    bass = "bass" """Bass Drum"""
    cymbals = "cymbal" """Cymbals"""


class Year(Enum):
    freshman = "freshman" """Freshman (9th grade)"""
    sophomore = "sophomore" """Sophomore (10th grade)"""
    junior = "junior" """Junior (11th Grade)"""
    senior = "senior" """Senior (12th Grade"""
    alumnus = "alumnus" """Alumnus (Graduated)"""
