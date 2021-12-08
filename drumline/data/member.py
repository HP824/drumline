"""
Single Member of a drumline implementation
"""

from drumline.data.enums import Instrument, Year


class Member:
    """
    Defines a member of a Drumline
    """
    def __init__(self, name: str, year: Year, instrument: Instrument) -> None:
        """
        Creates a new member of a drumline

        :param name: name of member
        :param year: year in high school
        :param instrument: instrument played in drumline
        :return: None
        """
        self.__name = name
        self.__year = year
        self.__instrument = instrument

    def get_name(self) -> str:
        """
        Returns name of member

        :return: name of member
        """
        return self.__name

    def get_year(self) -> Year:
        """
        Returns year of member

        :return: year of member
        """
        return self.__year

    def get_instrument(self) -> Instrument:
        """
        Returns instrument that member plays in drumline

        :return: member's instrument in drumline
        """
        return self.__instrument

    def set_name(self, name: str) -> None:
        """
        Sets the name of member

        :param name: name of member
        :return: none
        """
        self.__name = name

    def set_year(self, year: Year) -> None:
        """
        Sets the year of the member

        :param year: year of member
        :return: none
        """
        self.__year = year

    def set_instrument(self, instrument: Instrument) -> None:
        """
        Sets the instrument of member

        :param instrument: instrument of member
        :return: none
        """
        self.__instrument = instrument

    def promote(self) -> 'Member':
        """
        Creates a new member with its year attribute incremented by one.
        Raises ValueError if it tries to promote an alumni

        :return: new instance of Member with year promoted
        """
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

    def __hash__(self) -> hash:
        return hash((self.__name, self.__year, self.__instrument))

    def __eq__(self, other) -> bool:
        return self.__name == other.get_name() \
               and self.__year == other.get_year() \
               and self.__instrument == other.get_instrument()

    def __str__(self) -> str:
        return f"Name: {self.__name}, Year: {self.__year.name}, Instrument: {self.__instrument.name}"



