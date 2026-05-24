# 📌 Step 2: Program Introduction
print("\nWelcome to Student Score Tracker System\n")
name = []
score = []
student_counting = 1
# 📌 Step 3: Student Data Input

number_of_students = int(input("Please Enter The Number Of Students You Want To Enter :   "))
if number_of_students > 0 :
    
    while number_of_students > 0 :
        print(f"=======Student Number {student_counting} =======")
        student_name = input("Please Enter The Name Of Student : ")
        student_score = float(input("Please Enter The Score Of Student : "))
        name.append(student_name)
        score.append(student_score)
        student_counting += 1
        number_of_students -= 1 
    # 📌 Step 4: Display All Scores
    print("\n==============Display All Scores============\n")  
    for index in range(len(name)):
        print(f"Student Number {index + 1}. {name[index]} - {score[index]}")
    # 📌 Step 5: Highest and Lowest Score
    print("\n=================Highest and Lowest Score=============\n")
    
    highest_score = max(score)
    lowest_score = min(score)

    highest_scorer_student = score.index(highest_score)
    lowest_scorer_student = score.index(lowest_score)

    print(f"Highest Score Student : {name[highest_scorer_student]} - {highest_score}")
    print(f"Lowest Score Student : {name[lowest_scorer_student]} - {lowest_score}")
    # 📌 Step 6: Convert Scores to Tuple
    print("\n============Convert Scores to Tuple=============\n")
    score_tuple = tuple(score)
    print(f"Score as Tuple (Immutable) : {score_tuple}")
    # 📌 Step 7: Tuple Unpacking (Practice)
    print("\n==========Tuple Unpacking (Practice)=========\n")
    if len(score) >= 3 :
        score1, score2, score3, *rest_of_list = score
        print("First Three Scores : ")
        print(f"Score 1 : {score1}")
        print(f"Score 2 : {score2}")
        print(f"Score 3 : {score3}")
        print(f"Rest Of List : {rest_of_list}")
    else:
        print("\nNot enough scores to unpack (need at least 3).")
    # 📌 Step 8: Average Score Calculation
    print("\n============Average Score Calculation==============\n")
    total = sum(score)
    average_score = total / len(score)
    print(f"Average of all scores : {average_score:.2f}")
else:
    print("Invalid Input")
    