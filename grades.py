grade=float(input("Enter your grade"))
if grade<=29 and grade>=0:
    print("D")
elif grade<=49 and grade>=30:
    print("C")
elif grade<=79 and grade>=50:
    print("B")
elif grade<=100 and grade>=80:
    print("A")
else:
    print("error")
