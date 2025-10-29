from operations import *

while True:
    print("Pls select operation:\n " \
        "1. Add\n" \
        "2. sub\n" \
        "3. div\n" \
        "4. mul\n" \
        "5. avg\n" )
    select= int(input("Select a operation from 1,2,3,4,5: "))

    if select == 5:
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
    else:
        print("Invalid selection")