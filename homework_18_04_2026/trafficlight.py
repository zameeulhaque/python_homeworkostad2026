
color = input("Enter traffic light color: ").strip().lower()

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Wait!")
elif color == "green":
    print("Go!")
else:
    print("Invalid color!")
