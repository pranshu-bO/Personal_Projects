import csv
from datetime import date
import os
import sys

def main():
    print("Choose what action you wish to perform:")
    print("1. New Entry\n"
            "2. Veiw Report\n"
            "3. Exit")
    while True:
        try:
            choice = int(input("Type the number only of the command: "))
            break
        except ValueError:
            print("Enter a number 1 to 4 please")

    if choice == 1:
        today, description, amount = get_input()
        new_entry(today, description, amount)
    elif choice == 2:
        view_report()
    else:
        exit_program()

def get_input():
    while True:
            today = input("Do you want to set date to today[yes/no]: ").lower()
            if today == "yes":
                today = date.today()
                break
            elif today == "no":
                while True:
                    today = input("Date (Format:[DD/MM/YYYY]): ")
                    correct = True
                    try:
                        day_, month_, year_ = today.split("/")
                        day, month, year = int(day_), int(month_), int(year_)
                        if 1 < day > 31:
                            correct = False
                        elif 1 < month > 12:
                            correct = False
                        elif 1930 < year > 2030:
                            correct = False
                        if correct == True:
                            break
                        else:
                            pass
                    except ValueError:
                        pass
                break
            else:
                pass

    description = input("Description: ").capitalize().strip()
    amount = input("Amount: ").capitalize().strip()
    return today, description, amount


def new_entry(today, description, amount, filename="report.csv"):
    file_exists = os.path.exists("report.csv") and os.path.getsize("report.csv") > 0
    field = ["date", "description", "amount"]

    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
        "date": str(today),
        "description": description,
        "amount": amount
    })



def view_report():
    try:
        with open("report.csv", "r") as file:
            reader = csv.DictReader(file)
            income = 0.0
            expense = 0.0
            for row in reader:
                amt = float(row["amount"])
                if amt >= 0:
                    income += amt
                else:
                    expense += abs(amt)
            net = income - expense
            print(f"Income: ${income}")
            print(f"Expense: ${expense}")
            print(f"Net Profit/Loss: ${net}")
            if expense > income:
                print("We should dial back on expense!!!")
            else:
                print("We printing money BABY!!!")
    except FileNotFoundError:
        print("No Transaction Yet")


def exit_program():
    try:
        income = 0.0
        expense = 0.0
        with open("report.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                amt = float(row["amount"])
                if amt >= 0:
                    income += amt
                else:
                    expense += abs(amt)
            net = income - expense
            print(f"Net Profit/Loss: ${net}")
    except FileNotFoundError:
        print("No Transaction Yet")

if __name__ == "__main__":
    main()
 
