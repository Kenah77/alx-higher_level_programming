#!/usr/bin/python3
Student = __import__('10-student').Student

student1 = Student("Joe", "Goldberg", 27)
student2 = Student("Peter", "Stewarts", 30)

Jstudent1 = student1.to_json()
Jstudent2 = student2.to_json(['first_name', 'age'])
Jstudent3 = student2.to_json(['middle_name', 'age'])

print(Jstudent1)
print(Jstudent2)
print(Jstudent3)
