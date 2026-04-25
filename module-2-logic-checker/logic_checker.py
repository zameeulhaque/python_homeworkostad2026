# Welcome Message section
print("Welcome to Smart Eligibility & Performance Checker")
# User Input Section
try:
   name = input("Please Enter Your Full Name : ").strip()
   if not name.replace(" ", "").isalpha():
       print("Error: Invalid Input")
       exit()
   age = float(input("Please Enter Your Age (Years) : "))
   if age <= 0 or age > 120:
       print("Invalid Age")
       exit()
   exam_score = float(input("Please Enter Your Exam Score : "))
   if exam_score < 0 or exam_score > 100:
       print("Invalid Exam Score")
       exit()
   monthly_income = float(input("Please Enter Your Monthly Income (TK) : "))
   if monthly_income < 0:
       print("Invalid Monthly Income")
       exit()
# Age Eligibility Check section
   if age < 18:
      age_eligibility = "You are not eligible due to age restrictions."
   else:
      age_eligibility = "Age requirement passed."
   print(f"{age_eligibility}")
# Score Evaluation (Using elif) section
   if exam_score >= 90:
       grade_display = "A"
   elif exam_score >= 75:
       grade_display = "B"
   elif exam_score >= 60:
       grade_display = "C"
   else:
       grade_display = "Fail"
   print(f"Grade : {grade_display}")   
# Financial Support Check  section
   if monthly_income < 20000 and exam_score > 75:
       scholarship_eligibility = "Eligible"
   else:
       scholarship_eligibility = "Not eligible"
   print(f"{scholarship_eligibility} for scholarship support.")
# Nested Condition (Advanced) section
   if age > 18:
       if exam_score >= 60:
           print("You passed the program.")
       else:
           print("You failed the program.")
   else:
       print("Program access denied.")
# Final Summary Output section
   print("Final Summary Report")
   print(f"Name: {name}")
   print(f"Age : {age} Years")
   print(f"Exam Score : {exam_score}")
   print(f"Grade : {grade_display}")
   print(f"Scholarship eligibility status : {scholarship_eligibility}.")
except ValueError:
    print("invalid Input")