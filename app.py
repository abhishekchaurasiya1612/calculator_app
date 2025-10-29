from operations import *

while True:
    print("Pls select operation:\n " \
        "1. Add\n" \
        "2. sub\n" \
        "3. div\n" \
        "4. mul\n" \
        "5. square\n" \
        "6. sqrt\n" \
        "7. Power\n" \
        "8. Fcatorial\n" \
        "9. Exit\n" )
    select= int(input("Select a operation from 1,2,3,4,5,6,7,8,9: "))

    if select == 9:
        break
    n1= int(input("Enter 1st number"))
    n2= int(input("Enter 2nd number"))


    if select == 1:
        print(n1, "+", n2, "=", \
                add_num(n1,n2))
        
    elif select == 2:
        print(n1, "-", n2, "=", \
                sub_num(n1,n2))
    elif select == 3:
        print(n1, "/", n2, "=", \
                div_num(n1,n2))
    elif select == 4:
        print(n1, "*", n2, "=", \
                mul_num(n1,n2))
    elif select == 5:
        print("Square of",n1,"=",square_num(n1))
    elif select == 6:
        print("Sqrt of",n1,"=",sqrt_num(n1))
    elif select == 7:
        print(n1,"^",n2,"=",power_num(n1,n2))
    elif select == 8:
        print("Factorial of",int(n1),"=",factorial_num(n1))
    else:
        print("Invalid selection")