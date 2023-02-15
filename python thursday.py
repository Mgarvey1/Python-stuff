x=1
marks=12
grade=89

#if statement
if (x>=0):
    print("The number is positive")
    print(4+10)

#if....else statement
if marks>=60:
    print("You have passed")
else:
    print("Umechimba bro")
#if....elif...else
if grade<=29 and grade>=0:
    print("You have failed")
elif grade<=49 and grade>=30:
    print("You fave failed")
elif grade<=79 and grade>=50:
    print("you have credit")
elif grade<=100 and grade>=80:
    print("you have distinction")
else:
    print("Wrong input")

if grade<=29 and grade>=0:
    print("D")
elif grade<=49 and grade>=30:
    print("C")
elif grade<=79 and grade>=50:
    print("B")
elif grade<=100 and grade>=80:
    print("A")
else:
    print("Wrong input")





