S_number= 10
num= int(input("Guess the number: "))

while num!=S_number:
    num= int(input("Guess the number: "))
    if num==S_number:
        print("Correct Guess!")
    else:
        if num>S_number:
            print("Too High!")
        elif num<S_number:
            print("Too low!")