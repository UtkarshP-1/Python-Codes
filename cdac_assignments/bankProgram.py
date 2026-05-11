# Class Account with name ,accNumber,balance
# Class Bank with bankName, branch,accountList(5 accounts)
# Implement following functions::
# A.accept_account_info
# B.print_account_info
# C.accept_bank_info
# D.print_bank_info
# E.delete_account #Return 1 if deleted else 0
# F.float deposit #Return updated balance
# G.float withdraw #Return updated balance
# Write a menu driven program using above details and perform following operations:
# i. Create New Bank and 5 records of account in accountList.
# ii. Depost Amount from Given Account No.
# iii. Withdraw Amount from Given Account No.
# iv. Delete Account

class Account:
    def __init__(self, name='XYZ', acct_nbr=0, bal=0):
        self.name = name
        self.acct_nbr = acct_nbr
        self.bal = bal

    def accept_account_info(self):
        self.name = input("Enter Name: ")
        self.acct_nbr = int(input("Enter Account Number: "))
        self.bal = float(input("Enter Balance: "))

    def print_account_info(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acct_nbr}")
        print(f"Balance: {self.bal}")


class Bank:
    def __init__(self, bankName='ABC', branch='Main'):
        self.bankName = bankName
        self.branch = branch
        self.accountList = []

    def accept_bank_info(self):
        self.bankName = input("Enter Bank Name: ")
        self.branch = input("Enter Branch: ")

    def print_bank_info(self):
        print(f"Bank Name: {self.bankName}")
        print(f"Branch: {self.branch}")

        for acc in self.accountList:
            acc.print_account_info()

    def delete_account(self, acct_nbr):
        for acc in self.accountList:
            if acc.acct_nbr == acct_nbr:
                self.accountList.remove(acc)
                return 1
        return 0

    def deposit(self, acct_nbr, amount):
        for acc in self.accountList:
            if acc.acct_nbr == acct_nbr:
                acc.bal += amount
                return acc.bal
        return -1

    def withdraw(self, acct_nbr, amount):
        for acc in self.accountList:
            if acc.acct_nbr == acct_nbr:
                if acc.bal >= amount:
                    acc.bal -= amount
                    return acc.bal
                else:
                    print("Insufficient Balance")
                    return acc.bal
        return -1


b1 = Bank()

print('''
1. Create New Bank and 5 Accounts
2. Deposit Amount
3. Withdraw Amount
4. Delete Account
5. Print Bank Info
0. Exit
''')

while True:

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            b1.accept_bank_info()

            for i in range(5):
                print(f"\nEnter details for Account {i+1}")

                acc = Account()
                acc.accept_account_info()

                b1.accountList.append(acc)

        case 2:
            acct_nbr = int(input("Enter Account Number: "))
            amt = float(input("Enter Amount: "))

            bal = b1.deposit(acct_nbr, amt)

            if bal != -1:
                print("Updated Balance:", bal)
            else:
                print("Account not found")

        case 3:
            acct_nbr = int(input("Enter Account Number: "))
            amt = float(input("Enter Amount: "))

            bal = b1.withdraw(acct_nbr, amt)

            if bal != -1:
                print("Updated Balance:", bal)
            else:
                print("Account not found")

        case 4:
            acct_nbr = int(input("Enter Account Number: "))

            result = b1.delete_account(acct_nbr)

            if result == 1:
                print("Account Deleted")
            else:
                print("Account not found")

        case 5:
            b1.print_bank_info()

        case 0:
            print("Program Ended")
            break

        case _:
            print("Invalid Choice")
