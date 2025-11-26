import csv
import os


class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float.amount


class Income(Transaction):
    def __init__(self, amount, category):
        super().__init__(category, amount)
        self.type = "Income"


class Expense(Transaction):
    def __init__(self, amount, category):
        super().__init__(category, amount)
        self.type = "Expense"


# create a list
budget = []
FILENAME = "budget_data.csv"
# Example to add items to the list
# budget = [ {"date":"2023-01-01", "type :"income", "amount":1000, "description":"Salary"}
#         , {"date":"2023-01-02", "type":"expense", "amount":200, "description":"Groceries"} ]


def save_data_csv():
    # This function is to save the data to csv file

    try:
        with open(FILENAME="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file)
            writer.writerow()
        print
    except Exception as e:
        print("Error: " + e)


def add_record(type, amount, category):
    # This function is to record the bill to the list

    new_transaction = {"type": type, "amount": amount, "category": category}
    budget.append(new_transaction)
    print("Record added:", new_transaction)


def get_balance():
    # This function is to calculate the balance of income and expense

    total_income = 0
    total_expense = 0
    # loop through the list to calculate income and expense
    for item in budget:
        if item["type"] == "Income":
            total_income += item["amount"]
        else:
            # if not income,then is expenses
            total_expense += item["amount"]

    balance = total_income + total_expense

    print("--------------------")
    print("Total Income= RM", total_income)
    print("Total Expense= RM", total_expense)
    print("Balance: RM", balance)
    print("--------------------")
