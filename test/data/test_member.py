import unittest

from drumline.data.member import Member
from drumline.data.enums import Year, Instrument


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.member = Member("Harish", Year.junior, Instrument.snare)

    def test_get_name(self):
        self.assertEqual(self.member.get_name(), "Harish")

    def test_get_year(self):
        self.assertEqual(self.member.get_year(), Year.junior)

    def test_get_instrument(self):
        self.assertEqual(self.member.get_instrument(), Instrument.snare)

    def test_set_name(self):
        self.member.set_name("Harish Prabhakaran")
        self.assertNotEqual(self.member.get_name(), "Harish")
        self.assertEqual(self.member.get_name(), "Harish Prabhakaran")

    def test_set_year(self):
        self.member.set_year(Year.senior)
        self.assertNotEqual(self.member.get_year(), Year.junior)
        self.assertEqual(self.member.get_year(), Year.senior)

    def test_set_instrument(self):
        self.member.set_instrument(Instrument.tenors)
        self.assertNotEqual(self.member.get_instrument(), Instrument.snare)
        self.assertEqual(self.member.get_instrument(), Instrument.tenors)

    def test_promote_success(self):
        expected = Member("Harish", Year.senior, Instrument.snare)
        result = self.member.promote()
        self.assertEqual(result, expected)

    def test_promote_fail(self):
        self.assertRaises(ValueError, Member("Alumnus", Year.alumnus, Instrument.snare).promote)


if __name__ == '__main__':
    unittest.main()
