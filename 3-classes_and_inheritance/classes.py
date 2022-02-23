


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Student(Person):
    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        self.subject = subject

    def print_student(self):
        print(f'{self.full_name()}, subject: {self.subject}')


class Teacher(Person):
    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        self.subject = subject

    def print_teacher(self):
        print(f'{self.full_name}, subject: {self.subject}')

