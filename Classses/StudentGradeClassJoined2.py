
from tokenize import Double
from xml.etree.ElementTree import tostring

class Student():

   
    def __init__(self,n,e,p,a,m,g1,g2,g3,g4):
        self.name = n
        self.email = e
        self.phone = p
        self.address = a
        self.major = m
        self.grade1 = g1
        self.grade2 = g2
        self.grade3 = g3
        self.grade4 = g4
    def getName(self):
        return self.name
    def setName(self, new_name):
        self.name = new_name
    def getEmail(self):
        return self.email
    def setColor(self, new_email):
        self.email = new_email
    def getPhone(self):
        return self.phone
    def setColor(self, new_phone):
        self.phone = new_phone
    def getAddress(self):
        return self.address
    def setAddress(self, new_address):
        self.address = new_address
    def getMajor(self):
        return self.major
    def setMajor(self, new_major):
        self.major = new_major
    def getGrade1(self):
        return self.grade1
    def setGrade1(self, new_grade1):
        self.grade1 = new_grade1
    def getGrade2(self):
        return self.grade2
    def setGrade2(self, new_grade2):
        self.grade2 = new_grade2
    def getGrade3(self):
        return self.grade3
    def setGrade3(self, new_grade3):
        self.grade3 = new_grade3
    def getGrade4(self):
        return self.grade4
    def setGrade(self, new_grade4):
        self.grade4 = new_grade4 
           
    def getAverageGrade(self):
        sum = self.grade1 + self.grade2 + self.grade3 + self.grade4
        average = sum / 4
        return average
    def getAllAverageGrade(average_grade_array):
        total=0
        for i in range(0, len(average_grade_array)):
            total += average_grade_array[i]
            averageAll = total / len(average_grade_array)
        return averageAll
    def toString(self):
        return f"I'm a Student. My name is {self.getName}, and my email is {self.getEmail}," + \
            f"and my phone is {self.getPhone}, and my address is {self.getAddress}, and my major is {self.getMajor}," + \
            f"and my first grade is {self.getGrade1} ,and my second grade is {self.getGrade2},and my third grade is {self.getGrade3}," + \
            f"and my fourth grade is {self.getGrade4} and my average grade is {self.getAverageGrade}." 
    def toString2(self):
        return f"the average grade of all the student is {self.getAllAverageGrade} ."     






