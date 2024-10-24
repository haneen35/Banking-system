print ("enter your name")
name = input()
print ("hello, " + name + '\n' + "Choose your operation: " + '\n' + "a-Check Balance" + '\n' + "b-Deposit Money" + '\n' "c-Withdraw Money" + '\n' + "d-Exit" + '\n')
operation = input()
balance = int(1200)

def the_function():
    global balance
    print ("Thank you for using ACB bank " + name + '\n' + "Choose your operation: " + '\n' + "a-Check Balance" + '\n' + "b-Deposit Money" + '\n' "c-Withdraw Money" + '\n' + "d-Exit" + '\n')
    operation = input()
    
    if operation == "a":
         print("Your current balance: " + str(balance))
        the_function()
    elif operation == "b":
        deposite = int(input("enter:"))
        balance = balance + deposite
        print("Your current balance: " + balance)
        the_function()
    
    elif operation == "c":
        withdraw= int(input("enter:"))
        balance = balance + deposite - withdraw
        print("Your current balance: " + balance)
        the_function()
    
    elif operation == "d":
        print ("Thank you for using ACB bank")

