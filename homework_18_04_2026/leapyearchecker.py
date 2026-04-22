
try:
    year = int(input("Please Enter Year : "))
    if year % 400 == 0:
        print(f"leap Year {year}")
    elif year % 100 == 0:
        print(f"Not Leap Year {year}")
    elif year % 4 == 0:
        print(f"Leap Year {year}")
    else:
        print("Not Leap Year")
except ValueError:
    print("Invalid Input")
             
