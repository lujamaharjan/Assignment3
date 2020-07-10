
from academy import Academy

def main():
    acd = Academy("InsightWorkshop", 'iw@edu.io', '015591323')
    acd.inquiry()
    while(True):
        print("*****___MENU___*****")
        print('a: inquiry the course::')
        print('b: student registration::')
        print('c: update student info::')
        print('d: show all student details::')
        print('e: paysecond installment::')
        print('f: delete student::')
        print('g: return deposit::')
        print('h: enter h to exit program::')

        choice = input('Enter your choice::')
        if choice == 'a':
            acd.inquiry()
            print("/n")
        elif choice == 'b':
            acd.registration()
            print("/n")
        elif choice == 'c':
            acd.update_student_detail()
            print("/n")
        elif choice == 'd':
            acd.print_students_info()
            print("/n")
        elif choice == 'e':
            acd.pay_second_installment()
            print("/n")
        elif choice == 'f':
            acd.delete_student()
            print("/n")
        elif choice == 'g':
            acd.return_deposit()
            print("/n")
        elif choice =="h":
            break
        else:
            print("Invalid choice!")
            print("/n")






if __name__ == '__main__':
    main()





