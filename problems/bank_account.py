# fully corrected code from chat gpt
class BankAccount:
    def __init__(self, account_holder_name, initial_balance=0):
        self._account_holder_name = account_holder_name
        self._account_number = self.generate_account_number()
        self._balance = initial_balance

    def generate_account_number(self):
        # Generate a random account number (for demonstration purposes)
        import random
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount} into account {self._account_number}. New balance: {self._balance}")
        else:
            print(f"Invalid deposit amount. Amount must be greater than zero for account {self._account_number}.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount} from account {self._account_number}. New balance: {self._balance}")
            else:
                print(f"Insufficient funds for account {self._account_number}.")
        else:
            print(f"Invalid withdrawal amount. Amount must be greater than zero for account {self._account_number}.")

# Example usage:
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print("Account Holder:", account.account_holder_name)
    print("Account Number:", account.account_number)
    print("Initial Balance:", account.balance)
    account.deposit(500)
    account.withdraw(200)

# corrected code by chat gpt
# import random

# class BankAccount:
#     def __init__(self, account_holder_name=None, initial_balance=0):
#         self._account_holder_name = account_holder_name
#         self._account_no = ''.join(str(random.randint(0, 9)) for _ in range(10))
#         self._my_balance = initial_balance

#     def account_owner_name(self):
#         return self._account_holder_name

#     def initial_balance(self):
#         return self._my_balance

#     def account_no(self):
#         return self._account_no

#     def my_balance(self):
#         return self._my_balance

#     def deposit(self, amount):
#         if self._my_balance >= 10000:
#             print('Reached Maximum deposit is Ten Thousand')
#         else:
#             current_balance = self._my_balance + amount
#             if current_balance <= 10000:
#                 print(f'{amount} is being deposited to your account and your current balance is {current_balance}')
#                 self._my_balance = current_balance
#             else:
#                 print('Enter a smaller amount')

#     def withdraw(self, amount):
#         if amount > self._my_balance:
#             print('You do not have enough balance to withdraw')
#         else:
#             current_balance = self._my_balance - amount
#             if current_balance < 1000:
#                 print('Minimum balance should be maintained')
#             else:
#                 self._my_balance = current_balance
#                 print(f'Withdrawal is successful. {amount} has been deducted from your account and your current balance is {self._my_balance}')

# bankAccount = BankAccount('Amit', 1000)
# print('Account Owner Name:', bankAccount.account_owner_name())
# print('Account No:', bankAccount.account_no())
# print('Initial Balance:', bankAccount.my_balance())
# bankAccount.deposit(500)
# print('Current Balance:', bankAccount.my_balance())
# bankAccount.deposit(3000)
# print('Current Balance:', bankAccount.my_balance())
# bankAccount.deposit(5000)
# bankAccount.deposit(500)
# bankAccount.deposit(1500)
# bankAccount.withdraw(1000)
# bankAccount.withdraw(8000)
# print('Final Balance:', bankAccount.my_balance())









#  code i have written
# import random
# class BankAccount:
#     def __init__(self,account_holder_name=None,initial_balance=0):
#         self._account_holder_name=account_holder_name
#         account_no=[random.randint(0,9)for i in range(10)]
#         self.account_no=''.join(map(str,account_no))
#         self.my_balance=initial_balance
#     def account_owner_name(self):
#         return self._account_holder_name
#     def initial_balance(self):
#         return self._initial_balance
#     def account_no(self):
#         return self._account_no
#     def my_balance(self):
#         return self._my_balances
#     def deposit(self,amount):
#         if self.my_balance>=10000:
#             print('Reached Maximum deposite is Ten Thousand')
#         else:
#             current_balance= self.my_balance+amount
#             if(current_balance<=10000):
#                 print(f'{amount} is being deposited to your account and your current balance is {current_balance}')
#                 self.my_balance=current_balance
#             else:
#                 print('enter a smaller amount')
    
#     def withdraw(self,amount):
#         if amount >self.my_balance:
#             print('you dont have enough balance to withdraw')
#         else:
#             cureent_balance=self.my_balance-amount
#             if(cureent_balance==0 or cureent_balance<1000):
#                 print('Minimum balance should be maintained')
#             else:
#                 self.my_balance=cureent_balance
#                 print(f'Withdraw is successfull {amount} has been taken from your account and your current blance is {self.my_balance}')

# bankAccount=BankAccount('Amit',1000)
# print('Account Owner Name:',bankAccount.account_owner_name())
# print('Account No:',bankAccount.account_no)
# print('my initial Balance:',bankAccount.my_balance)
# bankAccount.deposit(500)
# print('my initial Balance:',bankAccount.my_balance)
# bankAccount.deposit(3000)
# print('my initial Balance:',bankAccount.my_balance)
# bankAccount.deposit(5000)
# bankAccount.deposit(500)
# bankAccount.deposit(1500)
# bankAccount.withdraw(1000)
# bankAccount.withdraw(8000)
# print('my initial Balance:',bankAccount.my_balance)



            


        
