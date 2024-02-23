from authenticator import *
from services import *
print("_"*50)
print("Welcome to K-Banking System")
print("_"*50)
while True:
    try:
        choice = int(input("1. Register\n"
                            "2. Login\n"
                            "Enter Your choice: "))
        if choice == 1:
            Register()
        elif choice == 2:
            acc_no = Login()

            set=True
            while set == True:
                try:
                    choice = int(input("\n1. Balance Enquiry\n"
                                        "2. Cash Deposit\n"
                                        "3. Cash Withdraw\n"
                                        "4. Fund Transfer\n"
                                        "5. View Passbook\n"
                                        "6. Close Account\n"
                                        "7. Logout\n"
                                        "Enter Your choice: "))
                    if choice == 1:
                        obj = Services()
                        obj.BalanceEnquiry(acc_no[0][0])
                    
                    elif choice == 2:
                        deposit = int(input("Enter amount to deposit: "))
                        obj = Services()
                        obj.CashDeposit(acc_no[0][0], deposit)
                    
                    elif choice == 3:
                        withdraw = int(input("Enter amount to withdraw: "))
                        obj = Services()
                        obj.CashWithdraw(acc_no[0][0], withdraw)
                    
                    elif choice == 4:
                        transfer_to = int(input("Enter account number of Recipient: "))
                        amount = int(input("Enter amount to send: "))
                        obj = Services()
                        obj.FundTransfer(acc_no[0][0], transfer_to, amount)
                    
                    elif choice == 5:
                        obj = Services()
                        obj.ViewPassbook(acc_no[0][0])
                    
                    elif choice == 6:
                        obj = Services()
                        obj.CloseAccount(acc_no[0][0])
                        set = False

                    elif choice == 7:
                        set = False
                    else:
                        print("Please Enter Valid Input From Options")
                
                except ValueError:
                    print("Invalid Input! Try again")

        else:
            print("Please Enter Valid Input From Options")
    
    except ValueError:
        print("Invalid Input! Try again")
