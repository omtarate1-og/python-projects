
# 1. Student Grade Management System

name = input("Enter student name: ")
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")


# 2. ATM System


balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance =", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")



# 3. Employee Salary Calculator


name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.05

gross_salary = basic_salary + hra + da - pf

print("\nEmployee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Gross Salary:", gross_salary)


# 4. Library Management System


books = ["Python", "Java", "C++", "Data Science"]

while True:
    print("\n1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("\nAvailable Books:")
        for book in books:
            print(book)

    elif choice == 2:
        borrow = input("Enter book name: ")

        if borrow in books:
            books.remove(borrow)
            print("Book Borrowed Successfully")
        else:
            print("Book Not Available")

    elif choice == 3:
        return_book = input("Enter book name to return: ")
        books.append(return_book)
        print("Book Returned Successfully")

    elif choice == 4:
        break

    else:
        print("Invalid Choice")


# 5. Number Guessing Game

import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess number between 1 to 100: "))

    if guess == secret_number:
        print("Correct Guess")
        break

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")



# 6. Bank Account System


account_holder = input("Enter account holder name: ")
balance = 10000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        balance += amount
        print("Money Deposited")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Funds")

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        break



# 7. Restaurant Billing System


pizza = 200
burger = 120
cold_drink = 50

qty1 = int(input("Enter pizza quantity: "))
qty2 = int(input("Enter burger quantity: "))
qty3 = int(input("Enter cold drink quantity: "))

total = (pizza * qty1) + (burger * qty2) + (cold_drink * qty3)

print("\n------ BILL ------")
print("Total Amount =", total)
print("Thank You Visit Again")


# 8. Password Generator


import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password =", password)


# 9. Contact Book

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")

        contacts[name] = number

    elif choice == 2:
        print("\nContacts:")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == 3:
        search = input("Enter name to search: ")

        if search in contacts:
            print(search, ":", contacts[search])
        else:
            print("Contact Not Found")

    elif choice == 4:
        break



# 10. Voting Eligibility System


name = input("Enter name: ")
age = int(input("Enter age: "))

if age >= 18:
    print(name, "is eligible for voting")
else:
    print(name, "is not eligible for voting")



# 11. Electricity Bill Calculator

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = units * 7

else:
    bill = units * 10

print("Electricity Bill =", bill)



# 12. Hotel Room Booking System

rooms = 10

while True:
    print("\n1. Check Rooms")
    print("2. Book Room")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Available Rooms =", rooms)

    elif choice == 2:

        if rooms > 0:
            rooms -= 1
            print("Room Booked Successfully")
        else:
            print("No Rooms Available")

    elif choice == 3:
        break



# 13. Shopping Bill System


item1 = int(input("Enter laptop price: "))
item2 = int(input("Enter mobile price: "))
item3 = int(input("Enter headphones price: "))

total = item1 + item2 + item3

discount = total * 0.10

final_amount = total - discount

print("\nTotal Amount =", total)
print("Discount =", discount)
print("Final Amount =", final_amount)




# 14. Simple Login System


username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")



# 15. Student Attendance System


total_days = int(input("Enter total working days: "))
present_days = int(input("Enter present days: "))

attendance = (present_days / total_days) * 100

print("Attendance Percentage =", attendance)

if attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
