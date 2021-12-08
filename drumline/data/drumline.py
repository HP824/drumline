"""
Drumline object used as base unit for application.
"""

from random import shuffle
from typing import List, Optional
from drumline.data.enums import Year
from drumline.data.member import Member


class Drumline:
    """
    Defines a single drumline unit with one or more initial members.
    Can have zero members but only after creation.
    """
    def __init__(self, *args: Member) -> None:
        """
        Creates a new drumline object with a list of members provided from args
        Raises ValueError if no arguments are provided.

        :param args: a list of members, provided one by one
        :return: None
        """
        if len(args) < 1:
            raise ValueError("No members in drumline!")
        self.__members = list(args)

    def get_members(self) -> List:
        """
        Returns a list of all the current members

        :return: list of members in drumline
        """
        return self.__members

    def add_member(self, member: Member) -> None:
        """
        Takes a Member object and adds it to the end of the
        list of members for the Drumline instance.

        :param member: Member object to be added
        :return: none
        """
        self.__members.append(member)

    def find_member(self, **kwargs) -> Member:
        """
        Finds a single member within a list using a set of
        search keywords arguments for each field in a Member.
        Can only search for exact matches (sorry, I'm not Google!)
        Raises a ValueError if multiple or zero search results are
        left, otherwise returns the single member found

        :param kwargs: (one required argument) name, year, and instrument of search
        :return: single Member object that matches all the keyword arguments
        """
        results = self.__members
        # filters a copy of the members list using the keyword arguments if they exist
        if kwargs.get("name", None) is not None:
            results = list(filter(lambda m: m.get_name() == kwargs["name"], results))
        if kwargs.get("year", None) is not None and len(results) > 0:
            results = list(filter(lambda m: m.get_year() == kwargs["year"], results))
        if kwargs.get("instrument", None) is not None and len(results) > 0:
            results = list(filter(lambda m: m.get_instrument() == kwargs["instrument"], results))
        # creates set from results to uniquely identify members and remove duplicates
        results = set(results)
        if len(results) < 1:
            raise ValueError("No results found")
        if len(results) > 1:
            raise ValueError("Multiple ambiguous results found, narrow your search")
        else:
            return tuple(results)[0]

    def remove_member(self, member: Member) -> None:
        """
        Removes a given Member object from the list.
        If member is not found, it will print why using the exception
        raised by self.find_member

        :param member: Member object to remove from member list
        :return: none
        """
        try:
            member = self.find_member(name=member.get_name(),
                                      year=member.get_year(),
                                      instrument=member.get_instrument())
        except ValueError as e:
            print(e)
            return
        self.__members.remove(member)

    def promote_members(self) -> 'Drumline':
        """
        Promotes all Member objects from the list.

        :return: new Drumline object with promoted members
        """
        return Drumline(*[m for m in map(self.__promote, self.__members) if m is not None])

    def scramble(self) -> 'Drumline':
        """

        :return:
        """
        instruments = [member.get_instrument() for member in self.__members]
        shuffle(instruments)
        scrambled = self.__members
        for member, instrument in zip(scrambled, instruments):
            member.set_instrument(instrument)
        return Drumline(*scrambled)

    @staticmethod
    def __promote(member: Member) -> Optional[Member]:
        """
        Safely increments year for provided Member object

        :return: a Member if successful, None otherwise
        """
        try:
            promoted_member = member.promote()
            if promoted_member.get_year() == Year.alumnus:
                return None
            return promoted_member
        except ValueError:
            return None
