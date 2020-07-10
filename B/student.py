'''Represnt the student contains CRUD for student'''
import csv
import re
import os


class Student:
    sid = 0
    re_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    def register(self, is_course_completed=False):
        self.name = input("Enter your Name::  ")
        self.input_email()
        self.phone = input("Enter your phone no:: ")
        self.address = input("Enter your Address:: ")
        print("you need to deposit RS 20000 you can also pay it in 2 installment.")
        self.input_deposit()
        self.is_course_completed=is_course_completed
        self.save()


    def update(self):
        self.delete()
        print('Now, Enter updated data::')
        print("Enter y | Y for if student completed course:")
        x = input("Else enter any key::")
        if x == 'y' or 'Y':
            self.register(True)
        else:
            self.register()
       

    def delete(self):
        self.input_email()
        with open('student.csv', 'r') as file, open('temp.csv', 'w',newline='') as temp:
            reader = csv.DictReader(file)
            writer = csv.writer(temp)
            writer.writerow(['name','email','phone','address','deposit','is_course_completed'])
            for row in reader:
                if row['email'] == self.email:
                   pass
                else:
                    writer.writerow([row['name'],row['email'],row['phone'], row['address'], row['deposit'], row['is_course_completed']])

        with open('student.csv','w',newline='') as file, open('temp.csv', 'r') as temp:
            reader = csv.reader(temp)
            writer = csv.writer(file)
            for row in reader:
                writer.writerow(row)

        if os.path.exists("temp.csv"):
            os.remove("temp.csv")
        else:
            print("Something went wrong restart program")


    def pay_second(self):
        self.input_email()
        with open('student.csv', 'r') as file, open('temp.csv', 'w',newline='') as temp:
            reader = csv.DictReader(file)
            writer = csv.writer(temp)
            writer.writerow(['name','email','phone','address','deposit','is_course_completed'])
            for row in reader:
                if row['email'] == self.email:
                   row['deposit'] == 20000
                writer.writerow([row['name'],row['email'],row['phone'], row['address'], row['deposit'], row['is_course_completed']])

        with open('student.csv','w',newline='') as file, open('temp.csv', 'r') as temp:
            reader = csv.reader(temp)
            writer = csv.writer(file)
            for row in reader:
                writer.writerow(row)

        if os.path.exists("temp.csv"):
            os.remove("temp.csv")
        else:
            print("Something went wrong restart program")


    def show_students(self):
        with open('student.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    def return_deposit(self):
        self.input_email()
        with open('student.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == self.email:
                    if row['is_course_completed'] == True:
                        print("print deposit have been returned!")
                    else:
                        print("Not eligible")


    def input_email(self):
        self.email = input("Enter your email:: ")
        self.validate_email()


    def validate_email(self):
        if(re.search(Student.re_email,self.email)):  
            pass
        else:  
           print("Invalid email format!")
           self.input_email()


    def input_deposit(self):
        self.deposit = int(input("Enter the deposit (Rs):: "))
        self.validate_deposit()
    

    def validate_deposit(self):
        if self.deposit == 10000 or self.deposit == 20000:
            pass
        else:
            self.input_deposit()


    def save(self):
        with open('student.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.email, self.phone, self.address, self.deposit, self.is_course_completed])
            

