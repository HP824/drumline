import unittest
from unittest.mock import patch
from random import Random

from drumline.data.drumline import Drumline
from drumline.data.member import Member
from drumline.data.enums import Year, Instrument


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        global random
        random = Random(69420)

        self.varun = Member("Varun", Year.junior, Instrument.tenors)
        self.adrian = Member("Adrian", Year.junior, Instrument.tenors)
        self.isaac = Member("Isaac", Year.senior, Instrument.snare)
        self.harish = Member("Harish", Year.junior, Instrument.snare)
        self.sid = Member("Siddharth", Year.junior, Instrument.snare)
        self.zekah = Member("Rebekah", Year.sophomore, Instrument.bass)
        self.brandon = Member("Brandon", Year.sophomore, Instrument.bass)
        self.avinash = Member("Avinash", Year.junior, Instrument.bass)
        self.aadi = Member("Aaditya", Year.sophomore, Instrument.bass)
        self.john = Member("John", Year.sophomore, Instrument.cymbals)
        self.ash = Member("Ash", Year.sophomore, Instrument.cymbals)
        self.drumline = Drumline(self.varun, self.adrian, self.isaac, self.harish, self.sid,
                                self.zekah, self.brandon, self.avinash, self.aadi, self.john, self.ash)

    def test_init_fails(self):
        self.assertRaises(ValueError, Drumline)

    def test_get_members(self):
        expected = [self.varun, self.adrian, self.isaac, self.harish, self.sid,
                    self.zekah, self.brandon, self.avinash, self.aadi, self.john, self.ash]
        self.assertEqual(self.drumline.get_members(), expected)

    def test_add_member(self):
        jonathan = Member("Jonathan", Year.alumnus, Instrument.cymbals)
        self.drumline.add_member(jonathan)
        expected = [self.varun, self.adrian, self.isaac, self.harish, self.sid,
                    self.zekah, self.brandon, self.avinash, self.aadi, self.john, self.ash, jonathan]
        self.assertEqual(self.drumline.get_members(), expected)

    def test_remove_member_success(self):
        self.drumline.remove_member(self.ash)
        expected = [self.varun, self.adrian, self.isaac, self.harish, self.sid,
                    self.zekah, self.brandon, self.avinash, self.aadi, self.john]
        self.assertEqual(self.drumline.get_members(), expected)

    def test_remove_member_fail(self):
        self.drumline.remove_member(Member("Nonexistent", Year.junior, Instrument.bass))
        expected = [self.varun, self.adrian, self.isaac, self.harish, self.sid,
                    self.zekah, self.brandon, self.avinash, self.aadi, self.john, self.ash]
        self.assertEqual(self.drumline.get_members(), expected)

    def test_find_member_success(self):
        expected = self.harish
        result = self.drumline.find_member(name="Harish", year=Year.junior, instrument=Instrument.snare)
        self.assertEqual(result, expected)

    def test_find_member_fail(self):
        self.assertRaises(ValueError,
                          self.drumline.find_member,
                          name="Nonexistent",
                          year=Year.alumnus,
                          instrument=Instrument.bass)

    def test_promote_members(self):
        expected = [
            Member("Varun", Year.senior, Instrument.tenors),
            Member("Adrian", Year.senior, Instrument.tenors),
            Member("Harish", Year.senior, Instrument.snare),
            Member("Siddharth", Year.senior, Instrument.snare),
            Member("Rebekah", Year.junior, Instrument.bass),
            Member("Brandon", Year.junior, Instrument.bass),
            Member("Avinash", Year.senior, Instrument.bass),
            Member("Aaditya", Year.junior, Instrument.bass),
            Member("John", Year.junior, Instrument.cymbals),
            Member("Ash", Year.junior, Instrument.cymbals),
        ]
        result = self.drumline.promote_members().get_members()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
