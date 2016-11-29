import unittest
from kol2_gr2 import sum_of_marks, sum_, Student, not_bool, count_marks, ClassDiary

class MyTest(unittest.TestCase):

    def test_not_bool(self):
        s = Student('Imie', 'Nazwisko', 'Klasa')
        self.assertEqual(not_bool(s), True)

    def test_sum_of_marks(self):
        self.assertEqual(sum_of_marks(1,2), 3)

    def test_sum(self):
        self.assertEqual(sum_(4, 4), 5)

    def test_count_marks(self):
        list = {1, 2, 3, 4, 5} #5 ocen
        self.assertEqual(count_marks(list), 5)

    def test_is_present(self):
        s = Student('Imie', 'Nazwisko', 'Klasa')
        self.assertEqual(s.is_present(1, True), s.marks_in_day[1])

    def test_add_mark(self):
        s = Student('Imie', 'Nazwisko', 'Klasa')
        s.is_present(1, True)
        s.add_mark(1, 3)
        self.assertEqual(s.marks_in_day[1], 3)

    def test_average_mark(self):
        s = Student('Imie', 'Nazwisko', 'Klasa')
        s.is_present(1, True)
        s.is_present(2, True)
        s.add_mark(1, 5)
        s.add_mark(2, 4)
        self.assertEqual(s.average_mark(), 4.5)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)