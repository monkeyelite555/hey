balance=float(10000)
active=1
while active==1:
    print("ATM\n(1)Check Balance\n(2)Deposit\n(3)Withdraw\n(4)Quit")
    option=input("Choose an option. ")
    if option=="1":
        print("Balance: $"+str(balance))
    elif option=="2":
        balance+=float(input("How much will you deposit? $"))
        print("Your balance is now $"+str(balance))
    elif option=="3":
        withdraw=float(input("How much will you withdraw? $"))
        if withdraw<=balance:
            balance = balance-withdraw
            print("$"+str(withdraw),"successfully withdrawn.")
            print("Your balance is now $"+str(balance))
        else:
            print("Withdrawal amount too large, please try again")
    elif option=="4":
        print("Thank you for using our service.")
        active=0
    else:
        print("Error: invalid command")
        print("Please enter the number of your desired command.")