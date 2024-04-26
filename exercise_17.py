# new student entry.
studentDetails =[]
def add(studentDetails_dict_) :
    studentDetails.append(studentDetails_dict_)
    print(studentDetails)
    main()
def newStudent() :
    name_ = input("Enter the name of the student : ")
    age_ = int(input("Enter age : "))
    rollNo_ = int(input("Enter Roll Number : "))
    courseName_ = input("Enter the course name : ")
    studentDetails_dict_ ={
        "name" : name_,
        "age"  : age_,
        "rollNo" : rollNo_,
        "courseName" : courseName_
    }
    add(studentDetails_dict_)
def main():
    choice = input("Want to add stdudent datils , Type 'Yes' or 'No' ")
    if choice == "Yes" :
        newStudent()
    else :
        print("Thank You!")
main()
