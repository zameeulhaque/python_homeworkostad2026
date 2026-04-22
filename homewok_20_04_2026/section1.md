
Truthy and Falsy Values:
Question 1: The Identity Crisis In Python, many objects have an inherent "truthiness." Look at the following list of variables. Which of these will evaluate to True when passed into a boolean check like if variable:?

    a = 0.0 (false)
    b = " " (a string containing a single space) (true)
    c = [] (false)
    d = -1 (true)
    e = None (false)
Question 2: Short-Circuit Logic What will be the exact output of the following code snippet?

x = []
y = "Hello"

if x or y:
    print(f"Result: {y}")
else:
    print("Result: Nothing")

    Result: Hello
