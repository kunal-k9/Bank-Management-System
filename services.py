from database import *
from datetime import datetime


class Passbook:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number
        self.createPassbook()
    
    def createPassbook(self):
        db_query(f'''CREATE TABLE IF NOT EXISTS pb{self.account_number}
                 (acc_no INTEGER,
                 timestamp VARCHAR(30),
                 amount VARCHAR(20),
                 transaction_type VARCHAR(20),
                 balance INTEGER)
                 ''')
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        db_query(f'''INSERT INTO pb{self.account_number} VALUES(
                 {self.account_number}, '{formatted_datetime}', 0 , 'ACCOUNT CREATED', 0);''')
        mydb.commit()

class Services:
    def BalanceEnquiry(self, acc_no):
        balance = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
        print("_"*50)
        print(f"Your account balance is: {balance[0][0]}")
        print("_"*50)

    def CashDeposit(self, acc_no, deposit):
        db_query(f"UPDATE customers SET balance = balance+{deposit} WHERE account_number = '{acc_no}' ")
        balance = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
        print("_"*50)
        print(f"Your updated balance is: {balance[0][0]}")
        print("_"*50)
        # UPDATING THE PASSBOOK
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        db_query(f"INSERT INTO pb{acc_no} VALUES('{acc_no}', '{formatted_datetime}', '+{deposit}', 'DEPOSIT', '{balance[0][0]}' ) ")
        mydb.commit()

    def CashWithdraw(self, acc_no, withdraw):
        db_query(f"UPDATE customers SET balance = balance-{withdraw} WHERE account_number = '{acc_no}' ")
        balance = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
        print("_"*50)
        print(f"Your updated balance is: {balance[0][0]}")
        print("_"*50)
        # UPDATING THE PASSBOOK
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        db_query(f"INSERT INTO pb{acc_no} VALUES('{acc_no}', '{formatted_datetime}', '-{withdraw}', 'WITHDRAW', '{balance[0][0]}' ) ")
        mydb.commit()

    def FundTransfer(self,acc_no, transfer_to, amount):
        receiver_bal = db_query(f"SELECT balance FROM customers WHERE account_number = '{transfer_to}' ")
        sender_bal = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
        if receiver_bal:
            if sender_bal[0][0] < amount:
                print("_"*50)
                print(f"Insufficient Balance in your Account. Available balance: {sender_bal[0][0]}")
                print("_"*50)
            else:
                # UPDATING THE RECIPIENT PASSBOOK
                db_query(f"UPDATE customers SET balance = balance+{amount} WHERE account_number = '{transfer_to}' ")
                mydb.commit() 
                updated_receiver_bal = db_query(f"SELECT balance FROM customers WHERE account_number = '{transfer_to}' ")
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                db_query(f"INSERT INTO pb{transfer_to} VALUES('{transfer_to}', '{formatted_datetime}', '+{amount}', 'RECEIVED', '{updated_receiver_bal[0][0]}' ) ")
                                
                # UPDATING THE SENDER PASSBOOK
                db_query(f"UPDATE customers SET balance = balance-{amount} WHERE account_number = '{acc_no}' ")
                updated_sender_bal = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                db_query(f"INSERT INTO pb{acc_no} VALUES('{acc_no}', '{formatted_datetime}', '-{amount}', 'SENT', '{updated_sender_bal[0][0]}' ) ")    
                print("_"*50)
                print(f"Transaction Successfull!\nRemaining balance is: {updated_sender_bal[0][0]}")
                print("_"*50)

                mydb.commit() 
            
        else:
            print("_"*50)
            print(f"No user with account number {transfer_to}. Transaction Failed!")
            print("_"*50)

    def ViewPassbook(self, acc_no):
        passbook = db_query(f"SELECT * FROM pb{acc_no} ")

        print("_" * 80)
        print(f"{'Account No.':<15} | {'TimeStamp':<20} | {'Amount':<10} | {'Transaction type':<17} | {'Balance':<10}")
        print("_" * 80)

        for row in passbook:
            print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10} | {row[3]:<17} | {row[4]:<10}")
            print("_" * 80)

    def CloseAccount(self, acc_no):
        balance = db_query(f"SELECT balance FROM customers WHERE account_number = '{acc_no}' ")
        print("_" * 80)
        print(f"You have Rs {balance[0][0]} in your account")
        choice = input(f"Are you sure to proceed with closing your account?: {acc_no}? (y/n): ")
        try:
            if choice == 'y' or 'Y':
                db_query(f"DROP TABLE pb{acc_no}")
                db_query(f"DELETE FROM customers WHERE account_number = {acc_no}")
                mydb.commit()
                print("_" * 40)
                print(f"Your Account {acc_no} has been closed.")
                print("_" * 40)
            elif choice == 'n' or 'N':
                exit
            else:
                print("Enter Y for Yes and N for No")
        except:
            print("Invalid Input")





    

