from StudentGradeClassJoined2 import Student

class Program:

   
    def main(self):
        
        student1=Student("David","david@gmail.com","054-1289437","Tel aviv Karlibach 64","Electrical Engineering",90,94,91,96)
        student2=Student("Jonatan","janatan@gmail.com","054-1285433","Tel aviv Kaplan 20","Software Engineering",95,89,93,87)
        student3=Student("Sharon","sharon@gmail.com","054-7531267","Tel aviv Dizingof 64","Chemical Engineering",89,95,88,100)
        student4=Student("Shara","shara@gmail.com","054-8731442","Tel aviv Alenbi 64","Mechanical Engeneering",92,93,97,98)
        student5=Student("Benny","benny@gmail.com","054-1289437","tel aviv Rothschild 64","Genetic Engineering",94,90,86,87)
        
        student_array=[]
        student_array.extend([student1,student2,student3,student4,student5]) 
        average_grade_array=[]
        Program.printMethod(student_array,average_grade_array)

    def printMethod(student_array,average_grade_array):
        for item in student_array:
            print("I am Student,my name is: ",item.getName(),"and my email is: ",item.getEmail(),"and my phone is: ",item.getPhone(),
            " and my address is: ",item.getName(),"my major is: ",item.getMajor(),"my average grade is: ",item.getAverageGrade())
            average_grade_array.append(item.getAverageGrade())
        print("the all average is: ", Student.getAllAverageGrade(average_grade_array))


callprogram=Program()
callprogram.main()