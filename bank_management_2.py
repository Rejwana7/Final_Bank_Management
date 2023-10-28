import random
from datetime import datetime
class User:
    def __init__(self,name,email)->None:
        self.name=name
        self.email=email
        
class Bank:
    def __init__(self,name)->None:
        self.name= name
        self.total_balance=pow(10,6)
        self.total_loan=0
        self.bankrupt=False
        self.loan_system = True
        self.users=[]

class Account_holder(User):
    def __init__(self,name,email,ac_type,password)->None:
        super().__init__(name,email)
        self.ac_type=ac_type
        self.initial_balance = 0
        self.password= password
        self.loan_taken=0
        self.loan_limit=0
        self.ac_no = random.randint(2000,10000)
        self.transaction_history=[]
    #def create_account(self,bank,name,email,ac_type,password):
        #new_user = Account_holder(name,email,ac_type,password)
       # bank.users.append(new_user)
    def deposit(self,bank,amount):
        if amount>0:
            self.initial_balance +=amount
            bank.total_balance +=amount
            transaction_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
            self.transaction_history.append(f"{transaction_time} - Deposit: {self.initial_balance}")
            print(f'you  deposit {amount} Tk')
        else:
            print(f'Enter a valid amount of money for deposit')
    def withdraw(self,bank,amount):
        if bank.bankrupt == False:
            if amount>0 and amount<=self.initial_balance:
                self.initial_balance -=amount
                bank.total_balance -=amount
                transaction_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
                self.transaction_history.append(f"{transaction_time} - Withdrawal: {amount} tk")

                print(f"your amount now {self.initial_balance} tk,you withdraw {amount} tk")
            elif amount>self.initial_balance:
                print(f'You have no enough money')
        else:
            print(f'The bank is bankrupt')
    def check_balance(self):
        print(f'Your current balance: {self.initial_balance} tk')
        
    def view_transaction_history(self):
        print(f'\n --->Transaction History')
        if len(self.transaction_history) >0:
            for tran in self.transaction_history:
                transaction_time,transaction_info = tran.split(" - ")
                print(f"{transaction_time}-{transaction_info}")
        else:
            print("There is no transaction")

    
    def take_loan(self,bank,amount):
        if bank.bankrupt == False:
            if bank.loan_system == True:
                if self.loan_taken <2:
                    self.initial_balance +=amount
                    bank.total_balance-=amount
                    bank.total_loan +=amount
                    self.loan_limit+=1
                    self.loan_taken +=1
                else:
                    print(f" You can't take loan,Sorry sir/mam")
            else:
                print(f'The bank loan system stop,beacause loan limit exceed')
        else:
            print(f'The bank is bankrupt')
    def transfer_money(self,bank,amount,receiver_ac_no):
        receiver = None
        receiver_found = False
       
        for user in bank.users:
            if user.ac_no == receiver_ac_no:
                receiver= user
                receiver_found = True
                break
        if receiver_found:
            if not bank.bankrupt:
                if self.initial_balance >=amount:
                    #transfer money
                    self.initial_balance -=amount
                    receiver.initial_balance +=amount
                    print(f"sender's final balance : {self.initial_balance}")
                    print(f'Transfered {amount} tk to {receiver.name}')
                  
                else:
                    print(f'Insufficient balance')
            else:
                print(f'The bank bankrupt')
        else:
            print(f"Receiver not found")
    
# admin
class Admin:
    def __init__(self,bank,admin_name,password):
        self.bank=bank
        self.admin_name = admin_name
        self.password = password
    def create_user_account(self,bank,name,email,ac_type,password):
        new_user = Account_holder(name,email,ac_type,password)
        bank.users.append(new_user)
        
        print(f"Account for {name} created successfully")
        return new_user
    def delete_user_account(self, ac_no):
        user = None
        for u in self.bank.users:
            if u.ac_no == ac_no:
                user = u
                break
        if user:
            self.bank.users.remove(user)
            print(f'Account successfully deleted')
        else:
            print(f'No account found ,Account No: {ac_no}')
    
    def list_account(self):
        if len(self.bank.users)>0:
            
            print("All Account List")
            for user in self.bank.users:
                print(f'Name: {user.name} , Account Number: {user.ac_no}')
        else:
            print("NO Available account")
    def Check_bank_balance(self):
        print(f'Total Balance in {self.bank.name} : {self.bank.total_balance} ')
    def Check_loan_balance(self):
        print(f'Total loan amount in {self.bank.name} : {self.bank.total_loan}')
    def loan_status(self,status):
        if status == "on":
            self.bank.loan_system = True
            print(f"Loan System Enabled")
        elif status == "off":
            self.bank.loan_system = False
            print(f"Loan System disabled")
        else:
            print(f"Invalid Status")
    
brac = Bank("Brac")
admin = Admin(brac,"Admin1","1226")
while True:
    print(f"\n--->Welcome to the {brac.name} bank\n")
    print("1.Admin")
    print("2.User")
   
    print("3.Exit")
    option = input("Enter any option:")

    if option == "1":
        print("Admin Login")
        ad_name= input("Enter admin name : ")
        password = input("Enter admin password: ")
        if ad_name == admin.admin_name and password == admin.password:
            print("Admin Successfully Log IN")
            while True:
                print("1. Create User Account")
                print("2.Delete User Account")
                print("3.List All User Account")
                print("4.Check Bank Balance")
                print("5.Check Total Loan")
                print("6.Turn Loan System ON/OFF")
                print("7.Logged Out")
                choice = input("Enter option :")
                if choice == "1":
                    #create user account
                    name = input("Enter User Name : ")
                    Email = input("Enter User Email : ")
                    Account_Type = input("Enter Account Type : ")
                    Password = input("Enter User Password : ")
                    admin.create_user_account(brac,name,Email,Account_Type,Password)
                elif choice == "2":
                    ac_no = int(input('Enter Account Number:'))
                    admin.delete_user_account(ac_no)
                elif choice == "3":
                    admin.list_account()
                elif choice == "4":
                    admin.Check_bank_balance()
                elif choice =="5":
                    admin.Check_loan_balance()
                elif choice == "6":
                    status = input("Enter 'on' to enable the loan system  'off' to disable:" )
                    admin.loan_status(status)
                elif choice == "7":
                    print("Logged Out Admin")
                    break
                else:
                    print("Invalid Choice. Enter Valid Choice")
#user
    elif option == "2":
        print("1.Log IN")
        print("2.Register")
        user_option= input("Enter an option:")
        #account holder login
        if user_option == "1":
            ac_no = int(input("Enter Account Number: "))
            password =  int(input("Enter Account holder password: "))
            #print(ac_no,password)
            user_account = None
            for user in brac.users:
                #print("Hello",user.ac_no)
                user_account = user
                if user.ac_no== ac_no:
                    print("User Successfully Log In")
                    while True:
                        print("1.Deposit Money:")
                        print("2.Withdraw Money:")
                        print("3.Check Balance:")
                        print("4.View Transaction History:")
                        print("5.Take Loan:")
                        print("6.Transfer Money:")
                        print("7.Logged Out")
                        choice = input('Enter Choice:')
                        if choice == "1":
                            amount = float(input("Enter the amount to deposit:"))
                            user_account.deposit(brac,amount)
                        elif choice == "2":
                            amount = float(input("Enter the amount to Withdraw:"))
                            user_account.withdraw(brac,amount)
                        elif choice == "3":
                            user_account.check_balance()
                        elif choice== "4":
                            Account_holder.view_transaction_history()
                        elif choice == "5":
                            amount = float(input("Enter the loan amount :"))
                            user_account.take_loan(brac,amount)
                        elif choice == "6":
                            receiver_ac_no = int(input("Enter receiver account no:" ))
                            amount = float(input("Enter the amount to transfer:"))
                            user_account.transfer_money(brac,amount,receiver_ac_no)
                        elif choice == "7":
                            print("logged out")
                            break
                else:
                    print("Invalid account number or password")
        elif user_option == "2":
            name = input("Enter user name: ")
            email = input("Enter user Email: ")
            ac_type= input("Enter Your Account Type(Saving/current:) ")
            password =  int(input("Enter Account holder password: "))
            n_user= Account_holder(name, email, ac_type, password)
            print("Account Number : ", n_user.ac_no)
            brac.users.append(n_user)
            print(f"User Registration Successful")

        else:
            print("Invalid option")
        
            
    elif option == "3":
        break
    else:
        print("Enter valid option")
                    



        











            







        

            
        

        


