#Write a prototype bank CLI app that allows a person to open an account
#, deposit money, change PIN and withdraw money.
#You code should contain 3 classes: Class BankAccount,Class SavingsAccount
#Class CurrentAccount. Let SavingsAccount and CurrentAccount inherit BankAccount
import mysql.connector

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
        if(isinstance(this.balance, float) == True or isinstance(this.balance, int) == True):
            this.balance += amount
            return f"{this.balance} deposited by {this.name}"
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
    my_deposit = new_client.deposit(5000)
    print(my_deposit)

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ugochi",
        password="November@10415",
        database= "new_work"
    )   
    new_db = mydb.cursor()

    '''sql = "INSERT INTO Bank_Account(name,age,gender,address,city, eMAIL) VALUES (%s,%s,%s,%s,%s,%s)"
    Ray = (name, dob, gender, address, city, email)
    new_db.execute(sql, Ray)
    
    mydb.commit()
    print(new_db.rowcount, "records inserted.")

if __name__ == "__main__": #namespaces and scopes - global and local(function) scopes
    my_main()'''




#new_db.execute("CREATE TABLE Bank_Account (id INT(11) NOT NULL AUTO_INCREMENT, Name VARCHAR(50) NOT NULL,Age VARCHAR(50) NOT NULL,PHONE_NO VARCHAR(50) NOT NULL,AMOUNT VARCHAR(50) NOT NULL,Gender VARCHAR(50) NOT NULL,Address VARCHAR(50) NOT NULL,City VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, PRIMARY KEY (id))")
    