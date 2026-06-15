marks= int(input("Enter your Marks(0-100): "))
if marks<0 or marks>100:
    print("Invalid marks! Please enter a value between 0 and 100.")
else:
    if marks>=90:
        print("Grade: A")
    elif marks>=75 and marks<=89:
        print("Grade: B")
    elif marks>=60 and marks<=74:
        print("Grade: C")
    elif marks>=40 and marks<=59:
        print("Grade: D")
    else:        
        print("Fail")