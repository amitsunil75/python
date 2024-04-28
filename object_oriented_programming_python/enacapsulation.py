#student example

import re


class Student:
    def __init__(self,name,rollNo):
        self._name=name
        self._rollNo=rollNo
        self._grade=[]
    def add_grade(self,grade):
        self._grade.append(grade)
    def average_grade(self):
        if len(self._grade)==0:
            return 0
        else:
           return sum(self._grade)/len(self._grade)
    def displayStudentInfo(self):
        print('Student Name:',self._name)
        print('Roll Number',self._rollNo)
        print('Average grade:',self.average_grade())
    

student=Student('amit',200)
student.add_grade(90)
student.add_grade(95)
student.add_grade(85)
student.displayStudentInfo()

class Person:
    def __init__(self,name,age,email):
        self._name=name
        self.__age=None
        self.__email=None
        self.set_age(age)
        self.set_email(email)

    def set_age(self,age):
        if age>0:
            self.__age=age
        else :return None
    
    def set_email(self,email):
         email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
         if re.match(email_regex,email):
             self.__email=email
         else:return None
    
    def get_info(self):
        return{
            "Name":self._name,
            "Age":self.__age,
            "Email":self.__email
        }
person = Person('amit',26,'amitsunil912@gmail.com')
print(person.get_info)

