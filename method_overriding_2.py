# Create a class 'Student' with rollno, studentName, course ,dictionary of marks(subjectName ->
# marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data for given id.
# ( accept records of 5 students and store those in list )


class Student:
    def __init__(self, rollNo=None, studentName=None, course=None, markDict=None):
        self.rollNo = rollNo
        self.studentName = studentName
        self.course = course
        self.markDict = markDict
        
    def accept_data(self, rollNo, studentName, course, markDict):
        self.rollNo = input("Enter Roll No: ")
        self.studentName = input("Enter Student Name: ")
        self.course = input("Enter Course Name: ")
        self.markDict = input("Enter Marks for each Subject: ")
        
    def __str__(self):
        return f"rollNo: {self.rollNo}, studentName: {self.studentName}, course: {self.course}, marks: {self.markDict}\n"
    
    def print_data(self):
        print(f"rollNo: {self.rollNo}\nstudentName: {self.studentName}\ncourse: {self.course}\nmarks: {self.markDict}")
        

RollNo = [1,2,3,4,5]
Names = ["Aakash", "Sameer", "Ananya", "Nick", "Tarun"]
Course = ["IT", "ITI","IIT", "B.Tech", "B.A."]
marks = [
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 },
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 },
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 },
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 },
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 },
    {"sub1": 10,"sub2": 20, "sub3": 30,"sub4": 40,"sub5":50 }
    ]

student_list = []

for i in range(5):
    s = Student(rollNo=RollNo[i],studentName=Names[i],course=Course[i],markDict=marks[i])
    s.print_data()
    student_list.append(s)
    
print(f"Info: {student_list[int(input("Enter Roll No to get info : "))-1]}")
