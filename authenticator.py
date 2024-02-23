#User Registration
from database import *
from services import *
import random

def Register():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}'")
    if temp:
        print("Username Already Exists! Please try other username")
        Register()
    else:
        print("Username Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        city = input("Enter your city: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers where account_number = '{account_number}'")
            if temp:
                continue
            else:
                db_query(f"INSERT INTO customers VALUES ('{username}', '{password}', '{name}', {age}, '{city}', 0, {account_number});")
                print("_"*70)
                print(f"Account Created Successfully! Your account number is: {account_number}"
                      "\nProceed to Login")
                print("_"*70)
                create_passbook = Passbook(username, account_number)
                break

def Login():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}'")
    if not temp:
        print("_"*70)
        print("Username Does not Exist! Please enter correct username")
        print("_"*70)
        Login()
    else:
        while True:
            password = input("Enter Your Password: ")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}' AND password = '{password}'")
            if temp:
                if temp[0][0] == password:
                    print("_"*50)
                    print("You are Logged In")
                    print("_"*50)
                    account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{username}' AND password = '{password}'")
                    return account_number
                    break
            else:
                print("_"*50)
                print("Wrong password! Try again!")
                print("_"*50)
        
