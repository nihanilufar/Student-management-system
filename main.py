from datetime import datetime



student = {}

'''
student = {
    roll_no : {
        name,
        course,
        department,
        phone number,
        
        
    }    
}
'''

print("========STUDENT MANAGEMENT SYSTEM========")
print("[1] Add Student")
print("[2] View Student ")
print("[3] Update student")
print("[4] Delete student")
print("[7] Show all Students")
print("[8] Exit")
print("==============================================")

while(True):
    option = int(input("enter your option : "))
    if(option==1):
        roll_no = int(input("enter your roll number : "))
        if(roll_no in student):
            print("Roll number already given...")
        else:
            name = input("enter your name: ")
            course = input("enter your course: ")
            department = input("enter your department: ")
            phone_num = int(input("enter phone num: "))

            student[roll_no] = {
                "name" : name,
                "course" : course,
                "department" : department,
                "phone num" : phone_num,
                "mark" : {}
            }  
            print("Student registered successfully")



    elif(option==2):
         roll_no = int(input("enter roll num: "))
         if (roll_no in student):
            student_info = student[roll_no]

            print("\n---STUDENT PROFILE ---")
            print(f"roll number : {roll_no}")
            print(f"name: {student_info['name']}")
            print(f"department : {student_info['department']}")
            print(f"phone num : {student_info['phone num']}")
            
         else:
                print("Error: student roll number not found!")


    elif(option==3):
        roll_no = int(input("enter roll num: "))
        if roll_no in student:

            new_course = input("enter your course: ")
            new_department = input("enter your department: ")
            new_phone_num = int(input("enter phone num: "))

            student[roll_no]["course"] = new_course
            student[roll_no]["department"] = new_department
            student[roll_no]["phone num"]=new_phone_num
            print("student details updated successfully")
        else:
            print("error:student record not found")

    elif(option==4):
        roll_no = int(input("enter roll num: "))
        if roll_no in student:
            del student[roll_no]
            print("deleted")

        else:
            print("not found")
    elif(option==5):
        if not student:
            print("No student records available")
        else:


            for roll_no in student.keys():
                name = student[roll_no]['name']
                dept = student[roll_no]['department']
                course = student[roll_no]['course']
                print(f"{roll_no} | name : {name} | dept : {dept} | course : {course}")
            print("-----------------------------------------------")


    elif(option==6):
        print("Thanks")
        break

    