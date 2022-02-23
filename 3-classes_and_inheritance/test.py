#!/usr/bin/env python
from classes import Person, Student

p = Person('Florian', 'van der Ent')
print(p.full_name())

p = Student('Florian', 'van der Ent', 'Advanced python')
p.print_student()
