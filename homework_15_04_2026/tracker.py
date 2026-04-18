print("Welcome to Daily Life Tracker Program")
username = input("Please Enter Your Name : ")
total_available_hours = float(input("Please Input Your Total Available Hours For Today : "))
daily_budget = float(input("Please Input Your Total Daily Budget TK : "))
print("How many hours you will spend on :")
Studying_Python = float(input("Studying Python ? Hours: "))
Practicing_coding = float(input("Practicing coding ? Hours: "))
Other_activities = float(input("Other activities ? Hours: "))
total_activities = (Studying_Python + Practicing_coding + Other_activities)
print(f"Total activity hours planned for the day : {total_activities} Hours")
print("Please Input Your Daily Expenses :")
food_expenses = float(input("Food Expenses TK : "))
transportation_expenses = float(input("Transportation Expenses TK : "))
Other_expenses = float(input("Other Expenses TK : "))
Total_daily_expenses = (food_expenses + transportation_expenses + Other_expenses )
print(f"Total daily expenses : {Total_daily_expenses} TK ")
if total_activities > total_available_hours:
    print("You have planned more hours than available.")
else:
    print("Your daily plan is realistic.")
    
if Total_daily_expenses > daily_budget:
    print("You have exceeded your daily budget.")
else:
    print("You are within your daily budget.")
    
print("Final Summary Report")
print(f"Hello {username}")
print(f"Total planned hours : {total_activities} Hours")
print(f"Total Expense : {Total_daily_expenses} TK")
Remaining_Budget = (daily_budget - Total_daily_expenses)
if Remaining_Budget > 0:
     print(f"Remaining Budget : {Remaining_Budget} TK")
elif Remaining_Budget == 0:
    print(f"You have no budget")
else:
     print(f"You have exceeded your budget limit")