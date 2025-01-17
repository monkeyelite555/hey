import math
active=1
while active==1:
    choice=int(input("     CALCULATOR     \n1.   Addition\n2.   Subtraction\n3.   Multiplication\n4.   Division\n5.   Remainder\n6.   Exponentation\n7.   Square Root\n8.   Factorial\n9.   Sum of a set\n10.   Exit\nChoice: "))
    if choice!=10:
        num1=float(input("Choose your first number: "))
        if choice!=7 and choice!=8:
            num2=float(input("Choose your second number: "))
    if choice==1:
        print(num1,"+",num2,"=",num1+num2)
    elif choice==2:
        print(num1,"-",num2,"=",num1-num2)
    elif choice==3:
        print(num1,"∙",num2,"=",num1*num2)
    elif choice==4:
        print(num1,"÷",num2,"=",num1/num2)
    elif choice==5:
        print("The remainder of",num1,"/",num2,"is",num1%num2)
    elif choice==6:
        print(num1,"to the power of",num2,"=",num1**num2)
    elif choice==7:
        print("The square root of",num1,"is",math.sqrt(num1))
    elif choice==8:
        print(str(int(num1))+"! =",math.factorial(int(num1)))
    elif choice==9:
        if num1>0:
            print("The sum of numbers",num1,"to",num2,"is",(num2*(num2+1))/2-(num1-1))
        elif num1==0:
            print("The sum of numbers",num1,"to",num2,"is",(num2*(num2+1))/2-num1)
        elif num1<0:
            print("The sum of numbers",num1,"to",num2,"is",(num2*(num2+1))/2-(abs(num1)*((abs(num1))+1)/2))
    elif choice==10:
        print("Goodbye!")
        active=0