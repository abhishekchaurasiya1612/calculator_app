def add_num(num1,num2):
    return num1+num2
def sub_num(num1,num2):
    return num1-num2
def div_num(num1,num2):
    return num1/num2
def mul_num(num1,num2):
    return num1*num2
# def avg_num(num1,num2):
#     return (num1+num2)/2
while True:
    print("Pls select operation:\n " \
        "1. Add\n" \
        "2. sub\n" \
        "3. div\n" \
        "4. mul\n" \
        "5. avg\n" )

    select= int(input("Select a operation from 1,2,3,4: "))
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
        print(n1, "-", n2, "=", \
                mul_num(n1,n2))
    # elif select == 5:
    #        print(" (",n1, "+", n2,")", "/","2","=", \
    #             savg_num(n1,n2))
    else:
            print("Invalid operation!") 