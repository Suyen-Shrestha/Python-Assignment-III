import csv
from tabulate import tabulate


class Student:

    def __init__(self, student_details=None):
        self.student_details = student_details if student_details is not None else []


    def enroll(self):
        name = input('Enter your fullname: ')
        address =input('Enter your address: ')
        installment = int(input('Please enter Rs. 10000 for the installment: '))
        if installment < 10000:
            print('Please make sure that installment is at least Rs.10000!\n')
        else:
            unpaid = 20000 - installment
            status = 'enrolled'
            student_detail = [name, address, installment, unpaid, status]
            with open('student_infos.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(student_detail)
            print('Congratulations!! you are successfully enrolled!\n')

    def displayStudents(self):
        with open('student_infos.csv', 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            headers = ['Student Name', 'Address', 'Paid Amount', 'Unpaid Amount', 'Course Status']
            for row in reader:
                self.student_details.append(row)
            print('Below are the details of enrolled students:\n')    
            print(f'{tabulate(self.student_details,headers)}')
            print('\n')

    # def updateStudent(self, name, address, paid):


        


class Academy:

    def __init__(self, coursecontents=None):
        self.coursecontents = coursecontents if coursecontents is not None else []

    
    def intro(self):
        print("\t\t\t\t*********************************************")
        print("\t\t\t\tWELCOME TO INSIGHT WORKSHOP ACADEMY PROGRAM!!")
        print("\t\t\t\t*********************************************\n")

    def displayCourseContents(self):
        with open('courseofstudy.csv', 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for row in reader:
                self.coursecontents.append(row)
            print('Below are the courses curriculum outline:\n')    
            print(f'{tabulate(self.coursecontents,headers="firstrow")}')
            print('\n')



    



ac = Academy()
st = Student()

# ac.displayCourseContents()    


# start of the program
ch=''
num=0
ac.intro()

while ch != 8:
    #system("cls");
    print("\tMAIN MENU")
    print("\t1. VIEW COURSE OF STUDY")
    print("\t2. ENROLL IN COURSE")
    print("\t3. VIEW STUDENTS INFORMATIONS")
    print("\t4. UPDATE STUDENT'S INFORMATION")
    print("\t5. DELETE A STUDENT FROM ACADEMY")
    print("\t6. COURSE COMPLETE AND RETURN THE DEPOSITED AMOUNT")
    print("\t7. EXIT")
    print("\tSelect Your Option (1-7) ")
     
    ch = input()
    print('\n')

    if ch == '1':
        ac.displayCourseContents() 
    elif ch == '2':
        st.enroll()
    elif ch == '3':
        st.displayStudents()     