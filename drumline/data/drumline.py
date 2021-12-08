from random import shuffle
from typing import Optional
from drumline.data.enums import Year
from drumline.data.member import Member


class Drumline:
    def __init__(self, *args: Member):
        if len(args) < 1:
            raise ValueError("No members in drumline!")
        self.__members = list(args)

    def get_members(self):
        return self.__members

    def add_member(self, member: Member) -> None:
        self.__members.append(member)

    def find_member(self, **kwargs) -> Member:
        results = self.__members
        if kwargs.get("name", None) is not None:
            results = list(filter(lambda m: m.get_name() == kwargs["name"], results))
        if kwargs.get("year", None) is not None and len(results) > 0:
            results = list(filter(lambda m: m.get_year() == kwargs["year"], results))
        if kwargs.get("instrument", None) is not None and len(results) > 0:
            results = list(filter(lambda m: m.get_instrument() == kwargs["instrument"], results))
        results = set(results)
        if len(results) < 1:
            raise ValueError("No results found")
        if len(results) > 1:
            raise ValueError("Multiple ambiguous results found, narrow your search")
        else:
            return tuple(results)[0]

    def remove_member(self, member: Member) -> None:
        try:
            member = self.find_member(name=member.get_name(),
                                      year=member.get_year(),
                                      instrument=member.get_instrument())
        except ValueError as e:
            print(e)
            return
        self.__members.remove(member)
        print("oof")

    # promote members (return new drumline object)
    def promote_members(self) -> 'Drumline':
        return Drumline(*[m for m in map(self.__promote, self.__members) if m is not None])

    def scramble(self) -> 'Drumline':
        instruments = [member.get_instrument() for member in self.__members]
        shuffle(instruments)
        scrambled = self.__members
        for member, instrument in zip(scrambled, instruments):
            member.set_instrument(instrument)
        return Drumline(*scrambled)

    @staticmethod
    def __promote(member: Member) -> Optional[Member]:
        try:
            promoted_member = member.promote()
            if promoted_member.get_year() == Year.alumnus:
                return None
            return promoted_member
        except ValueError:
            return None