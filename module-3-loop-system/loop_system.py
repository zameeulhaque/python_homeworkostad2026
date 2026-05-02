# 📌 Step 2: Program Introduction
print("Welcome to Smart Task Repetition System")

# 📌 Step 3: Task Input
task_name = input("Please enter your task name: ")
repeat = int(input("How many times do you want to repeat this task today: "))

# 📌 Step 4: Using for Loop
for x in range(1, repeat + 1):
    print(f"Task ({x}) : {task_name} completed.")
    
#  📌 Step 5: Countdown Using while Loop
count = int(input("Please Enter Countdown Number : "))

while count > 0:
    print(count)
    count -=1
print("Countdown finished!")

# 📌 Step 6: Nested Loop (Advanced Practice)
sessions = ["Morning", "Evening"]

for session in sessions:
    for i in range(1, 4):
     print(f"{session} Task {i}")
     
# 📌 Step 7: Infinite Loop Test (Learning Purpose)
i = 1

while i < 5:
    print(f"Fixed Loop Running : {i}")
    i +=1 #proper counter. Comment this to test infinite loop.This is an infinite loop... Press Ctrl + C to stop 
    
# 📌 Step 8: Final Output Summary
print("\n--- Summary ---")
print(f"Task Name: {task_name}")
print(f"Total Repetitions Completed: {repeat}")
print("Countdown finished successfully!") 
     
     
        
    
   


   