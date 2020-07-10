''' All the methods and properties of academy '''

import pyfiglet
from student import Student


class Academy:
    course = "Python Django Fullstack"
    deposit = 20000
    course_duration = 3
 

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        #prints welcome message in ascii
        msg = pyfiglet.figlet_format(self.name)
        print("Welcome to InsightWorkshop")
        print(msg)


    def inquiry(self):
        print("Welcome to InsightWorkshop")
        print("We have one fixed course.")
        print(f"Course name is {Academy.course}")
        print(f"For joining the course you have to deposit Rs.{Academy.deposit}")
        print("Deposit will be refunded after completion of the course")
        print(f'Duration of Course is {Academy.course_duration} month')
        print('\n\n')


    def registration(self):
        """register student for course """
        print('For Registration for course, Fill baisc data')
        student = Student()
        student.register()
        del student
        print("** Student registerd successfully! **")
        print('\n\n')


    def update_student_detail(self):
        student = Student()
        student.update()
        del student
        print("** Student Detail updated ! **")
        print('\n\n')


    def pay_second_installment(self):
        student = Student()
        student.pay_second()
        del student
        print('** installment depsoited sucessfully! **')


    def print_students_info(self):
        student = Student()
        student.show_students()
        del student


    def delete_student(self):
        student = Student()
        student.delete()
        del student
        print("** Student Deleted successfully! **")


    def return_deposit(self):
        student = Student()
        student.return_deposit()
        del student
     

