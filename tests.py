import unittest

from kol2_gr2 import Student

class test_student(unittest.TestCase):
    def setUp(self):
        self.stud = Student("name", "surname", "class")

     def test_stud_add(self):
        self.assertEqual(2, self.stud.add(1, 1))


    def test_add_mark(self):
        self.assertEqual(self.stud.marks_in_day, self.stud.add_mark(1, 1))

unittest.main()