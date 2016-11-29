from functools import reduce
#
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

def not_bool(a):
    return False if isinstance(a,type(False)) else True


def sum_of_marks(x,y):
    x+=y
    return x

def sum_(x,y):
    x+=1
    return x


def count_marks(list_of_marks):
    result = reduce(sum_,list_of_marks)
    return result


class Student(object):
    def __init__(self,student_name,student_surname,student_class):
        self.name = student_name
        self.surname = student_surname
        self.class_ = student_class
        self.marks_in_day = {}

    def is_present(self,day_id,is_present):
        self.marks_in_day[day_id] = None if is_present else False

    def add_mark(self,day_id,mark):
        if isinstance(self.marks_in_day[day_id],type(False)):
            print("nie ma ucznia ktoremu chcesz wpisac ocene: %s" % str(self))
        else:
            if self.marks_in_day[day_id] is None:
                self.marks_in_day[day_id] = mark
            else:
                self.marks_in_day[day_id].extend(mark)

    def average_mark(self):
        not_bool_list = filter(not_bool,self.marks_in_day.values())
        x = []
        [x.extend(y) for y in not_bool_list]
        print ("average for %s is %.2f" % (self,reduce(sum_of_marks,x)/reduce(sum_,x)))
        return reduce(sum_of_marks,x)/reduce(sum_,x)

    def __str__(self):
        return self.name+" "+self.surname


class ClassDiary(object):
    def __init__(self, dict_of_students):
        self.students = dict_of_students
        self.days = []

    def check_attendance(self,day_id,**attendance):
        self.days.append(day_id)
        for student,is_present in attendance.items():
            if student in self.students.keys():
                self.students[student].is_present(day_id,is_present)

    def add_mark(self,day_id,**marks):
        if day_id in self.days:
            for student,mark in marks.items():
                if student in self.students.keys() and self.students[student]!=False:
                    self.students[student].add_mark(day_id,mark)
