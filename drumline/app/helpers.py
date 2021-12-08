"""
Toplevel command implementations that are invoked by the user.
Do not use outside the context of main.py.
"""

from drumline.data.drumline import Drumline
from drumline.data.member import Member
from drumline.data.enums import Year, Instrument


def __create_drumline() -> Drumline:
    """
    Creates a new sample drumline object for initial use

    :return: a new Drumline with a fixed amount of sample members
    """
    varun = Member("Varun", Year.junior, Instrument.tenors)
    adrian = Member("Adrian", Year.junior, Instrument.tenors)
    isaac = Member("Isaac", Year.senior, Instrument.snare)
    harish = Member("Harish", Year.junior, Instrument.snare)
    sid = Member("Siddharth", Year.junior, Instrument.snare)
    zekah = Member("Rebekah", Year.sophomore, Instrument.bass)
    brandon = Member("Brandon", Year.sophomore, Instrument.bass)
    avinash = Member("Avinash", Year.junior, Instrument.bass)
    aadi = Member("Aaditya", Year.sophomore, Instrument.bass)
    john = Member("John", Year.sophomore, Instrument.cymbals)
    ash = Member("Ash", Year.sophomore, Instrument.cymbals)
    return Drumline(varun, adrian, isaac, harish, sid, zekah, brandon, avinash, aadi, john, ash)


drumline = __create_drumline()


def add_member() -> None:
    """
    Adds new member into Drumline object

    :return: none
    """
    while True:
        # Enter name of member
        name = input("Enter name of member: ")
        # Checks to see if valid name has been inputted
        if len(name) == 0:
            print("Enter a valid name")
            continue
        break
    while True:
        # Enter year of member
        year = input("Enter year member is in (freshman, sophomore, junior, senior, alumnus): ").lower()
        if year == "freshman":
            year = Year.freshman
        elif year == "sophomore":
            year = Year.sophomore
        elif year == "junior":
            year = Year.junior
        elif year == "senior":
            year = Year.senior
        elif year == "alumnus":
            year = Year.alumnus
        else:
            print(f"Invalid input {year}, must be freshman, sophomore, junior, senior, or alumnus")
            continue
        break
    while True:
        # Enter instrument of member
        instrument = input("Enter instrument for member (snare, tenors, bass, cymbals): ").lower()
        if instrument == "snare":
            instrument = Instrument.snare
        elif instrument == "tenors":
            instrument = Instrument.tenors
        elif instrument == "bass":
            instrument = Instrument.bass
        elif instrument == "cymbals":
            instrument = Instrument.cymbals
        else:
            print(f"Invalid input {instrument}, must be snare, tenors, bass, cymbals")
            continue
        break

    drumline.add_member(Member(name, year, instrument))
    print("Added member successfully! :)")


def list_members() -> None:
    """
    Lists members of Drumline object

    :return: None
    """
    members = drumline.get_members()
    if len(members) == 0:
        print("No members found! Add one using the \"add\" command.")
    else:
        print(*drumline.get_members(), sep="\n")


def find_member() -> None:
    """
    Finds member in Drumline object

    :return: None
    """
    # Enter name of member if known
    name = input("Enter name of member (skip if unknown): ")
    # Enter a valid year of member if known
    while True:
        year = input("Enter year they are in: (skip if unknown): ").lower()
        if len(year) > 0:
            if year == "freshman":
                year = Year.freshman
            elif year == "sophomore":
                year = Year.sophomore
            elif year == "junior":
                year = Year.junior
            elif year == "senior":
                year = Year.senior
            elif year == "alumnus":
                year = Year.alumnus
            else:
                print("Enter a valid year!")
                continue
            break
        break
    # Enter valid instrument if known
    while True:
        instrument = input("Enter instrument they play (skip if unknown): ").lower()
        if len(instrument) > 0:
            if instrument == "snare":
                instrument = Instrument.snare
            elif instrument == "tenors":
                instrument = Instrument.tenors
            elif instrument == "bass":
                instrument = Instrument.bass
            elif instrument == "cymbals":
                instrument = Instrument.cymbals
            else:
                print("Enter a valid instrument!")
                continue
            break
        break
    # conditionally passes the keyword arguments if they exist
    arguments = {}
    if len(name) > 0:
        arguments.update({"name": name})
    if type(year) == Year:
        arguments.update({"year": year})
    if type(instrument) == Instrument:
        arguments.update({"instrument": instrument})
    try:
        member = drumline.find_member(**arguments)
        print(member)
    except ValueError as e:
        print(e)


def remove_member() -> None:
    """
    removes member from Drumline object

    :return: None
    """
    # display current members listed
    print("These are the current members:")
    members = drumline.get_members()
    for i in range(1, len(members) + 1):
        print(f"{i}) {members[i - 1]}")
    index = 0
    # asks user for which member they want to remove with integer input
    while True:
        try:
            index = int(input("Which one do you want to remove? Enter the number: "))
        except ValueError:
            print("Invalid input. Enter a number!")
            continue
        if index not in range(1, len(members) + 1):
            print("No member exists at that number!")
            continue
        break
    drumline.remove_member(members[index - 1])
    print("Removed member successfully! :)")


def promote_members() -> None:
    """
    promotes members of Drumline object

    :return: None
    """
    global drumline
    print("Congratulations on moving on to the next year!")
    drumline = drumline.promote_members()
    print("This drumline has now been promoted! Check it out:")
    list_members()


def scramble_members() -> None:
    """
    scrambles member instruments in Drumline object

    :return: None
    """
    global drumline
    print("Now scrambling the drumline. Here are your new roles:")
    scrambled = drumline.scramble()
    print(*scrambled.get_members(), sep="\n")
    confirmation = input("Would you like to replace the current drumline with the scrambled one?: ").lower()
    if len(confirmation) != 0 and confirmation[0] == 'y':
        drumline = scrambled
    else:
        print("Not scrambling current drumline.")
