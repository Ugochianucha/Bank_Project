#Write a prototype bank CLI app that allows a person to open an account
#, deposit money, change PIN and withdraw money.
#You code should contain 3 classes: Class BankAccount,Class SavingsAccount
#Class CurrentAccount. Let SavingsAccount and CurrentAccount inherit BankAccount
import mysql.connector
from db_info import db_list

class Bank_account:
    def __init__ (this, name, Phone_no, Address, Occupation, gender, dob, email):
        this.name = name
        this.Phone_no = Phone_no
        this.Address = Address
        this.Occupation = Occupation
        this.gender = gender
        this.dob = dob
        this.email = email
        this.balance = 0
        
class Savings_account(Bank_account):
    def __init__(this, name, Phone_no, Address, Occupation, gender, dob, email, City):
        super().__init__(name, Phone_no, Address, Occupation, gender, dob, email)
        this.City = City

    def deposit(this, amount):
        if(isinstance(amount, float) == True or isinstance(amount, int) == True):
            this.balance += amount
            return this.balance
        else:
            return "Only numbers please"

    def change_pin(this, user_pin):
        if user_pin > 4:
            return "your pin should be four digits" 
        else:
            pass

    def withdrawal(this):
        pass
'''
class Current_account:
    def __init__(this, name, Phone_no, Address, Occupation, City, Opening_balance):
        super().__init__(this, City, Opening_balance)
        this.city = City
        this.Opening_balance = Opening_balance

    def deposite(this):
        pass

    def change_pin(this, user_pin):
        if user_pin > 4:
            return "your pin should be four digits" 
        else:
            pass
    def withdrawal(this):
        pass
'''

def my_main():
    name = str(input("Please type in your name: "))
    phone_no = str(input("Mobile number please: "))
    address = str(input("House address?: "))
    occupation = str(input("What do you do?: "))
    gender = str(input("Male or Female?: "))
    dob = str(input("Your date of birth: "))
    email = str(input("Email: "))
    city = str(input("City: "))
    new_client = Savings_account(name, phone_no, address, occupation, gender, dob, email, city)

    db_params = db_list()
    mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user = db_params[0],
        password = db_params[1],
        database = db_params[2]
    )   
    new_db = mydb.cursor()
    new_db.execute("CREATE TABLE Bank_Account (id INT(11) NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL, Age VARCHAR(50) NOT NULL, Phone_No VARCHAR(50) NOT NULL, Gender VARCHAR(50) NOT NULL, Address VARCHAR(50) NOT NULL, City VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, balance FLOAT(12, 3), PRIMARY KEY (id))")
  
    sql = "INSERT INTO Bank_Account(Name, Age, Phone_No, Gender, Address, City, email, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s4)"
    Ray = (name, dob, phone_no, gender, address, city, email, 0)
    new_db.execute(sql, Ray)
    
    mydb.commit()
    print(new_db.rowcount, "records inserted.")

    sql = "SELECT id, email FROM Bank_Account"
    new_db.execute(sql)
    my_query = new_db.fetchone()
    print(my_query)
    depositamount = str(input("Enter the deposit amount: "))
    my_deposit = new_client.deposit(float(depositamount))
    print(my_deposit)
    sql = "UPDATE Bank_Account SET balance = %s WHERE email = %s"
    val = (my_deposit, email)
    new_db.execute(sql, val)
    mydb.commit()
    print(new_db.rowcount, "records affected.")

if __name__ == "__main__": #namespaces and scopes - global and local(function) scopes
    my_main()  