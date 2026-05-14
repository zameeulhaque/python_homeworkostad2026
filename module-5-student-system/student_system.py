print("Welcome to Smart Student Life Management System")
# 📌 Step 2: Program Introduction
student_name = str(input("Please Enter Student Name : "))
student_id = str(input("Please Enter Student ID : "))
daily_study_hours = float(input("Please Enter Daily Study Hours : "))
monthly_pocket_money = float(input("Please Enter Monthly Pocket Money TK : "))
attendance_percentage = None
grade = None
total_expense = None
remaining_pocket_money = monthly_pocket_money
while True:
    # 📌 Step 3: Main Menu System
    print("========== MAIN MENU ==========")
    print("Please Choose An Option From Below : ")
    print("1. Class Attendance Tracker")
    print("2. Study Session Manager")
    print("3. Exam Result Checker")
    print("4. Monthly Expense Tracker")
    print("5. Daily Problem Solver")
    print("6. Exit")
    option_main = str(input("Option : "))
    # 📌 Step 4: Class Attendance Tracker
    if option_main == "1":
        print("=========Welcome To Class Attendance Tracker==========")   
        total_classes = int(input("Please Enter Total Classes : "))
        if total_classes <= 0: 
            print("Invalid Classes Input")
            continue
        attended_classes = int(input("Please Enter Total Attended Classes : "))
        if attended_classes < 0:
            print("Invalid Attended Classes Input ")
            continue
        elif attended_classes > total_classes: 
            print("Invalid Attended Classes Input ")
            continue
        attendance_percentage = (attended_classes / total_classes) * 100
        if attendance_percentage >= 75:
            print("Your Are Eligible For Exam.")
        else:
            print("You Are Not ELigible For Exam.")
        
    # 📌 Step 5: Study Session Manager
    elif option_main == "2":
        print("=======Welcome To Study Session Manager=======")
        subject_name = str(input("Please Enter Subject Name : "))
        number_study_sessions = int(input("Please Enter Number Of Study Sessions : "))
        for i in range(1,number_study_sessions + 1):
            print(f"Subject :  {subject_name} Study Session {i} Completed")
        print("Did you complete all sessions? (yes/no)")
        session_ask = str(input("Your Answer : ")).strip().lower()
        if session_ask == "yes":
            print("Great Consistency!")
        else:
            print("Try To Improve Tomorrow.")
        
    # 📌 Step 6: Exam Result Checker
    elif option_main == "3":
        print("=======Welcome To Exam Result Checker=======")
        python_marks = float(input("Please Enter Marks In Python : "))
        if python_marks < 0 or python_marks > 100 : 
            print("Invalid Input ")
            continue
        mathematics_marks = float(input("Please Enter Marks In Mathematis : "))
        if mathematics_marks < 0 or mathematics_marks > 100 :
            print("Invalid Input")
            continue
        english_marks = float(input("Please Enter Marks In English : "))
        if english_marks < 0 or english_marks > 100 :
            print("Invalid Input")
            continue
        average_marks = (python_marks + mathematics_marks + english_marks)/3
        if average_marks >= 80:
            grade = "A"
        elif average_marks >= 70:
            grade = "B"
        elif average_marks >= 60:
            grade = "C"
        else:
            grade = "Fail"
            
        print(f"Your Grade : {grade}")
    # 📌 Step 7: Monthly Expense Tracker
    elif option_main == "4":
        print("=======Welcome To Monthly Expense Tracker=======")
        food_expense = float(input("Please Enter Your Food Expense TK : "))
        internet_expense = float(input("Please Enter Your Internet Expense TK : "))
        transport_expense = float(input("Please Enter Your Transport Expense TK : "))
        other_expense = float(input("Please Enter Your Others Expense TK : "))
        total_expense = food_expense + internet_expense + transport_expense + other_expense 
        remaining_pocket_money = monthly_pocket_money - total_expense
        if total_expense > monthly_pocket_money:
            print("Budget Limit Crossed")
        else:
            print("You managed your expenses well.")
            
    # 📌 Step 8: Daily Problem Solver
    elif option_main == "5":
        while True: 
            print("=======Welcome To Daily Problem Solver=======")   
            print("Please Choose An Option From Below : ")
            print("1. Even or Odd Checker.")
            print("2. Largest Number Finder.")
            print("3. Simple Sum Calculator.")
            print("4. Return To Main Menu")
            option = str(input("Option : "))
            # 🔹 Even or Odd Checker
            if option == "1":
                print("=======Welcome To Even Or Odd Checker=======")
                even_or_odd_number = int(input("Please Input Any Integer Number : "))
                if even_or_odd_number % 2 ==0:
                   print(f"You Have Entered Even Number : {even_or_odd_number}")
                else:
                   print(f"You Have Entered Odd Number : {even_or_odd_number}")

            # 🔹 Largest Number Finder
            elif option == "2":
                print("=======Welcome To Largest Number Finder=======")
                max_number1 = float(input("Please Enter Any Number1 : "))
                max_number2 = float(input("Please Enter Any Number2 : "))
                max_number3 = float(input("Please Enter Any Number3 : "))
                if max_number1 > max_number2 and max_number1 > max_number3:
                    max_result = f"The Largest Number Is : {max_number1}"
                elif max_number2 > max_number1 and max_number2 > max_number3:
                    max_result = f"The Largest Number Is : {max_number2}"
                elif max_number3 > max_number1 and max_number3 > max_number2:
                    max_result = f"The Largest Number Is : {max_number3}"
                else:
                    max_result = "Three Number Equal Or Invalid Input"
                print(f"Result : {max_result} ")

            # 🔹 Simple Sum Calculator
            elif option == "3":
                print("=======Welcome To Simple Sum Calculator=======") 
                sum_number1 = float(input("Please Input Any Number1 : "))
                sum_number2 = float(input("Please Input Any Number2 : "))
                total_sum = sum_number1 + sum_number2 
                print(f"Sum Of Two Number Is : {total_sum}")
            elif option == "4":
                break
            else:
                print("Invalid Option")
    elif option_main == "6":
        break
    else:
        print("Invalid Main Menu Option Input")
# 📌 Step 9: Countdown Timer (While Loop Practice)
countdown_number = int(input("Please Enter A Countdown Number : "))
n = 1
while countdown_number >= n:
    print(countdown_number)
    countdown_number -= 1
print("Session Finished Successfully.")

# 📌 Step 10: Final Summary Report
print("========== FINAL SUMMARY ==========")
print(f"Student Name : {student_name}")
print(f"Student ID : {student_id}")
if attendance_percentage == None:
    print(f"Attendance : Not Calculated ")
else:
    print(f"Attendance : {attendance_percentage} %")
if grade == None:
    print(f"Last Grade : Not Calculated ")
else:
    print(f"Last Grade : {grade}")
if total_expense == None:
    print(f"Monthly Expense : Not Calculated ")
else:
    print(f"Monthly Expense : {total_expense} TK ")
if remaining_pocket_money < 0:
    print(f"Remaining Balance : You Have Already Spent More Than Your Budget.")
else:
    print(f"Remaining Balance : {remaining_pocket_money} TK ")
print("==============Thank You For Using The System.===============")