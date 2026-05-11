# 📌 Step 2: Program Introduction
print("Welcome to Daily Life Problem Solver Toolkit")
# 📌 Step 3: Menu System
sum_result = ""
even_odd_result = ""
max_number_result = ""
while True:
        print("Please Choose An Option :")
        print("1. Calculate sum of two numbers. ")
        print("2.Check even or odd ")
        print("3.Find maximum of three numbers ")
# 📌 Step 4: Sum Calculator
        choice = int(input("Option  : "))
        if choice ==1:
            print("Congratulation! You have selected option : 1. Calculate sum of two numbers.")
            sum_number1 = float(input("Please Input First Number : "))
            sum_number2 = float(input("Please Input Second Number :"))
            sum_result = sum_number1 + sum_number2
            print(f"Sum Of Two Number ( {sum_number1} + {sum_number2} ) : {sum_result}")
# 📌 Step 5: Even or Odd Checker
        elif choice ==2:
            print("Congratulation! You have selected option : 2.Check even or odd.")
            even_odd_number = int(input("Please Input Number To Check Even Or Odd : "))
            if even_odd_number % 2 ==0:
                even_odd_result = f"You Have Entered Even Number : {even_odd_number}"
                print(f"You Have Entered Even Number : {even_odd_number}")
            else:
                even_odd_result = f"You Have Entered Odd Number : {even_odd_number}"
                print(f"You Have Entered Odd Number : {even_odd_number}")
# 📌 Step 6: Maximum Finder
        elif choice ==3:
            print("Congratulation! You have selected option : 3.Find maximum of three numbers")
            max_number1 = float(input("Please Input Number First : "))
            max_number2 = float(input("Please Input Number Second : "))
            max_number3 = float(input("Please Input Number Third : "))
            if max_number1 > max_number2 and max_number1 > max_number3:
                max_number_result = max_number1
                print(f"The Largest Number Is : {max_number1}")
            elif max_number2 > max_number1 and max_number2 > max_number3:
                max_number_result = max_number2
                print(f"The Largest Number Is : {max_number2}")
            else:
                max_number_result = max_number3
                print(f"The Largest Number Is : {max_number3}")
        else:
            print("Invali Input try again")
# 📌 Step 7: Repeat Program Using Loop (Challenge Part)
        print("Do you want to solve another problem? (yes/no)")
        again_run_choice = input("Type : ").strip().lower()
        
        if again_run_choice == "no":
            print("Thank You For Using Daily Life Problem Solver Toolkit")
            break
        
# 📌 Step 8: Final Output Formatting
print("----Final Summary Report----")
print(f"Result : Sum Of Two Number : {sum_result}")
print(f"Result : {even_odd_result}")
print(f"The Largest Number Is : {max_number_result}")