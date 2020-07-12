import csv
from tabulate import tabulate


class Student:

    def __init__(self, student_details=None):
        self.student_details = student_details if student_details is not None else []


    def enroll(self):
        name = input('Enter your fullname: ')
        address =input('Enter your address: ')
        installment = int(input('Please enter Rs. 10000 for the first installment: \n'))
        if installment < 10000:
            print('Please make sure that installment is at least Rs.10000!\n')
            print('Enroll cancelled try again!!!\n')
        else:
            unpaid = 20000 - installment
            status = 'enrolled'
            all = []
            student_detail = [name, address, installment, unpaid, status]
            with open('student_infos.csv', 'r') as Input, open('student_infos.csv', 'a',newline='') as Output:
                reader = csv.reader(Input, delimiter = ',')
                writer = csv.writer(Output, delimiter = ',')
                count = len(list(reader))
                if count == 0:
                    writer.writerow(['ID','Student Name', 'Address', 'Paid Amount', 'Unpaid Amount', 'Returned Amount', 'Course Status'])
                    student_detail.insert(0,count+1)
                    writer.writerow(student_detail)
                else:    
                    student_detail.insert(0,count)  #for adding student's id by incrementing total count of rows in csv file by 1 each time a new student is added.2
                    writer.writerow(student_detail)
            print('Congratulations!! you are successfully enrolled!\n')

    def displayStudents(self):
        with open('student_infos.csv', 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            
            for row in reader:
                self.student_details.append(row)
                print(row[0])
            print('Below are the details of enrolled students:\n')    
            print(f'{tabulate(self.student_details,headers="firstrow")}')
            print('\n')
            # else:
            #     print('No students enrolled currently!!\n')    

    def updateStudent(self, id):
        name = input('Enter the updated name: ')
        address = input('Enter the updated address: ')
        paid = input('Enter the updated paid amount: ')
        unpaid = str(20000 - int(paid))
        returned = 0
        status = input('Enter the updated Course status: ')

        lines = list() # list for maintaing entire rows after updation of single row.
        up_dict = {} # dictionary for maintaining the key value pairs of updated csv row.
       
        with open('student_infos.csv', 'r') as readFile:
            reader = csv.DictReader(readFile)
            for row in reader:
                if row['ID'] == id:  # checks if the id value in the row is equal to id passed by user.
                    up_dict['ID'] = row['ID']
                    up_dict['Student Name'] = name
                    up_dict['Address'] = address
                    up_dict['Paid Amount'] = paid
                    up_dict['Unpaid Amount'] = unpaid
                    up_dict['Returned Amount'] = returned
                    up_dict['Course Status'] = 'enrolled' #status is only changed to completed from option 6.
                    lines.append(up_dict) # appending the updated dictionary to the lines list.
                else:
                    lines.append({k : v for k , v in row.items()})
                                  
        with open('student_infos.csv', 'w', newline='') as writeFile:
            fields = lines[0].keys()
            writer = csv.DictWriter(writeFile, fieldnames=fields)
            writer.writeheader() 
            writer.writerows(lines)
            print('Student updated successfully!!\n')
                        


    def deleteStudent(self, id):
        lines = list()
        with open('student_infos.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == id:
                        lines.remove(row)
        with open('student_infos.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)  
            writer.writerows(lines)
            print('Student deleted successfully!!\n')     
            


    def graduateStudent(self, id):
        
        lines = list() 
        up_dict = {} 
       
        with open('student_infos.csv', 'r') as readFile:
            reader = csv.DictReader(readFile)
            for row in reader:
                if row['ID'] == id: 
                    up_dict['ID'] = row['ID']
                    up_dict['Student Name'] = row['Student Name']
                    up_dict['Address'] = row['Address']
                    up_dict['Paid Amount'] = row['Paid Amount']
                    up_dict['Unpaid Amount'] = row['Unpaid Amount']
                    up_dict['Returned Amount'] = '20000'
                    up_dict['Course Status'] = 'completed' #status is changed to completed after student's graduation.
                    lines.append(up_dict) 
                else:
                    lines.append({k : v for k , v in row.items()})
            print(lines)        
                                  
        with open('student_infos.csv', 'w', newline='') as writeFile:
            fields = lines[0].keys()
            writer = csv.DictWriter(writeFile, fieldnames=fields)
            writer.writeheader() 
            writer.writerows(lines)
            print('Student graduated successfully!!\n')
                        
        


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
    elif ch == '4':
        id = input('Enter a student\'s ID to update: ')
        st.updateStudent(id)    
    elif ch == '5':
        id = input('Enter a student\'s ID to delete: ')
        st.deleteStudent(id) 
    elif ch == '6':
        num = input("\tEnter The students id who have completed the course : ")
        st.graduateStudent(num)
    elif ch == '7':
        print("\tThanks for visiting Insight Workshop Acadamey Program!")
        break
    else :
        print("Invalid choice")          
