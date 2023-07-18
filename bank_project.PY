#Write a prototype bank CLI app that allows a person to open an account
#, deposit money, change PIN and withdraw money.
#You code should contain 3 classes: Class BankAccount,Class SavingsAccount
#Class CurrentAccount. Let SavingsAccount and CurrentAccount inherit BankAccount
import mysql.connector
from db_info import db_list

class Bank_account:
    def __init__ (this, name, Phone_no, Address, Occupation, gender,pin, dob, email):
        this.name = name
        this.Phone_no = Phone_no
        this.Address = Address
        this.Occupation = Occupation
        this.gender = gender
        this.pin = pin
        this.dob = dob
        this.email = email
        this.balance = 0
        
class Savings_account(Bank_account):
    def __init__(this, name, Phone_no, Address, Occupation, gender,pin, dob, email, City):
        super().__init__(name, Phone_no, Address, Occupation, gender,pin, dob, email)
        this.City = City

    def deposit(this, balance, amount):
        amount = float(amount)
        if(isinstance(amount, float) == True or isinstance(amount, int) == True):
            this.balance = balance
            this.balance += amount
            return this.balance
        else:
            return "Only numbers please"

    def change_pin(this, user_pin):
        if user_pin > 4:
            return "your pin should be four digits" 
        else:
            return "Pin changed successfully"

    def withdrawal(this, balance, amount):
        amount = float(amount)
        if(isinstance(amount, float) == True or isinstance(amount, int) == True):
            this.balance = balance
            this.balance -= amount
            return this.balance
        else:
            return "Only numbers please"

def check_db(model):
    email = str(input("Email: "))
    sql = "SELECT * FROM Bank_Account where email = %s"
    val = ([email])
    model.execute(sql, val)
    new_query = model.fetchone()

    return new_query

def my_main():
    db_params = db_list()
    mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user = db_params[0],
        password = db_params[1],
        database = db_params[2]
    )   
    new_db = mydb.cursor()
    '''
    new_db.execute("CREATE TABLE Bank_Account (id INT(11) NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Age VARCHAR(50) NOT NULL, Phone_No VARCHAR(50) NOT NULL, Gender VARCHAR(50) NOT NULL,PIN VARCHAR(4) NOT NULL, Address VARCHAR(50) NOT NULL, City VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, balance FLOAT(12, 3), PRIMARY KEY (id))")
    name = str(input("Please type in your name: "))
    phone_no = str(input("Mobile number please: "))
    address = str(input("House address?: "))
    occupation = str(input("What do you do?: "))
    gender = str(input("Male or Female?: "))
    pin = "0000"
    dob = str(input("Your date of birth: "))
    email = str(input("Email: "))
    city = str(input("City: "))
    new_client = Savings_account(name, phone_no, address, occupation, gender, pin, dob, email, city)
    sql = "INSERT INTO Bank_Account(Name, Age, Phone_No, Gender,pin, Address, City, email, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    Ray = (name, dob, phone_no, gender,pin, address, city, email, 0)
    new_db.execute(sql, Ray)
    
    mydb.commit()
    print(new_db.rowcount, "records inserted.")
    '''
    
    my_query = check_db(new_db)
    bal = my_query[9]
    email = my_query[8]
    print(f"This client's record is - {my_query}\nThe balance is {bal}")

    my_client = Savings_account(my_query[1], my_query[3], my_query[6], "Doctor", my_query[4], my_query[5], my_query[2], my_query[8], my_query[7])
    depositamount = input("Enter the deposit amount: ")
    my_deposit = my_client.deposit(bal, depositamount)
    print(my_deposit)
    sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
    val = (my_deposit, email)
    new_db.execute(sql, val)
    mydb.commit()
    print(new_db.rowcount, "records affected.")

    my_query = check_db(new_db)
    bal = my_query[9]
    email = my_query[8]
    print(f"This client's record is - {my_query}\nThe balance is {bal}")

    withdrawamount = input("Enter the withdrawal amount: ")
    my_withdrawal = my_client.withdrawal(bal, withdrawamount)
    print(my_withdrawal)
    sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
    val = (my_withdrawal, email)
    new_db.execute(sql, val)
    mydb.commit()
    print(new_db.rowcount, "records affected.")

    change_pin = input("Enter the user_pin:")
    
    

if __name__ == "__main__": #namespaces and scopes - global and local(function) scopes
    my_main()  