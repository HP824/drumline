from drumline.data.enums import Instrument, Year


class Member:
    def __init__(self, name: str, year: Year, instrument: Instrument):
        self.__name = name
        self.__year = year
        self.__instrument = instrument

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_instrument(self):
        return self.__instrument

    def set_name(self, name: str):
        self.__name = name

    def set_year(self, year: Year):
        self.__year = year

    def set_instrument(self, instrument: Instrument):
        self.__instrument = instrument

    def promote(self) -> 'Member':
        if self.__year == Year.freshman:
            year = Year.sophomore
        elif self.__year == Year.sophomore:
            year = Year.junior
        elif self.__year == Year.junior:
            year = Year.senior
        elif self.__year == Year.senior:
            year = Year.alumnus
        else:
            raise ValueError("Attempted to promote alumnus")
        return Member(self.__name, year, self.__instrument)

    def __hash__(self):
        return hash((self.__name, self.__year, self.__instrument))

    def __eq__(self, other):
        return self.__name == other.get_name() \
               and self.__year == other.get_year() \
               and self.__instrument == other.get_instrument()

    def __str__(self) -> str:
        return f"Name: {self.__name}, Year: {self.__year.name}, Instrument: {self.__instrument.name}"



