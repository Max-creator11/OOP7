import datetime


class Groups:
    numbers_of_students = 0
    stipend_percent = 1.07
    default_stipend = 1040

    def __init__(self, first, last, group, stipend):
        self.first = first
        self.last = last
        self.group = group
        self.stipend = stipend
        self.person = first + ' ' + last + ', Group:' + \
            group
        Groups.numbers_of_students += 1

    def student(self):
        print("Info: " + self.person)
        return self.person

    def apply_raise(self):
        self.stipend = int(self.stipend * self.stipend_percent)
        return self.stipend

    @classmethod
    def raise_stipend_by(cls, new_value):
        cls.default_stipend = cls.default_stipend + new_value

    @classmethod
    def from_string(cls, stud):
        first, last, group, stipend = stud.split(':')
        stipend = int(stipend)
        return cls(first, last, group, stipend)

    @staticmethod
    def is_study_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("Weekends!")
            return False
        else:
            print("Study day!")
            return True


student1 = Groups("Maksym", "Severyn", "It-12sp", 1040)
student2 = Groups("Bohdan", "Martyniv", "It-12sp", 1040)
student3 = Groups("Vasyl", "Horobec", "M-12", 1040)
student1.apply_raise()

Groups.raise_stipend_by(500)
print("New Stipend Amount:", Groups.default_stipend)


stud_1 = "Oleh:Syp:T-12sp:4000"
new_stud1 = Groups.from_string(stud_1)

temp = vars(new_stud1)
for item in temp:
    print(item, ':', temp[item])


date = datetime.date(2021, 4, 11)
Groups.is_study_day(date)

print(student1.stipend)
print(student2.stipend)
print(student3.stipend)
print(Groups.numbers_of_students)
student1.student()
student2.student()
student3.student()
