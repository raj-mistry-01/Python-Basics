# an execellent example.
class university :
    def __init__(self,name = "Nirma University") -> None:
        self.name = name
    def showdetails(self) :
        print(self.name)

class course (university) :
    def __init__(self,courseName = "Engineering")->None :
        university.__init__(self) # use this rather than writing def __init(self,name = "Nirma University")
        self.courseName = courseName
    def showdetails(self):
        print(f"The name of the university is {self.name} and course name is {self.courseName}")

class branch(university) :
    def __init__(self,branchName = "CSE") -> None:
        course.__init__(self)
        self.branchName = branchName

    def showdetails(self):
        print(f"The name of the university is {self.name} ,course name is {self.courseName} and  the name of the {self.branchName}")

class student1 (branch) : 
    def __init__(self,student1Name = "Raj") :
        branch.__init__(self)
        self.student1Name = student1Name
    def showdetails(self):
        print(f"The name of the university is {self.name} ,branch name is {self.branchName} and student name is {self.student1Name}") # you can not access course here.

class student2 (course,branch) :
    def __init__(self,student2Name = "Rajvi" ) :
        branch.__init__(self) # will init course , init university
        self.student2Name = student2Name
    def showdetails(self):
        print(f"The name of the university is {self.name} ,branch name is {self.branchName} ,course name is {self.courseName} student name is {self.student2Name}")
obj1 = student1()
print(student1.mro())
obj1.showdetails()

obj2 = student2()
print(student1.mro())
obj2.showdetails()