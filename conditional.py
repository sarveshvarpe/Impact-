# ==============================
# Question 1: Ride Eligibility
# ==============================
age = int(input("Q1 - Enter age: "))
height = int(input("Q1 - Enter height (cm): "))

if age >= 12 and height >= 150:
    print("Eligible for the ride")
else:
    print("Not eligible for the ride")


# ==============================
# Question 2: Library Fine
# ==============================
late_days = int(input("\nQ2 - Enter late days: "))

if late_days <= 5:
    fine = 5
elif late_days <= 10:
    fine = 10
else:
    fine = 15

print("Fine: ₹", fine)


# ==============================
# Question 3: Grade System
# ==============================
marks = int(input("\nQ3 - Enter marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)


# ==============================
# Question 4: Temperature Status
# ==============================
temp = int(input("\nQ4 - Enter temperature (°C): "))

if temp < 0:
    print("Freezing")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")


# ==============================
# Question 5: Cinema Ticket Discount
# ==============================
age = int(input("\nQ5 - Enter age: "))
price = 20

if age < 12:
    price *= 0.5
elif age >= 60:
    price *= 0.7

print("Final Ticket Price: ₹", price)


# ==============================
# Question 6: Magic Number Guess
# ==============================
magic = 7
guess = int(input("\nQ6 - Guess the number: "))

if guess < magic:
    print("Too low!")
elif guess > magic:
    print("Too high!")
else:
    print("Congratulations! Correct guess")


# ==============================
# Question 7: Shop Discount
# ==============================
amount = int(input("\nQ7 - Enter purchase amount: "))

if amount >= 3000:
    discount = 0.30
elif amount >= 2000:
    discount = 0.20
elif amount >= 1000:
    discount = 0.10
else:
    discount = 0

final_price = amount - (amount * discount)
print("Final Price: ₹", final_price)


# ==============================
# Question 8: Leap Year
# ==============================
year = int(input("\nQ8 - Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# ==============================
# Question 9: Loan Eligibility
# ==============================
salary = int(input("\nQ9 - Enter salary: "))
credit_score = int(input("Q9 - Enter credit score: "))

if salary >= 3000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# ==============================
# Question 10: Employee Bonus
# ==============================
years = int(input("\nQ10 - Enter years of service: "))
salary = int(input("Q10 - Enter annual salary: "))

if years < 5:
    bonus = 0
elif years <= 10:
    bonus = salary * 0.10
else:
    bonus = salary * 0.20

print("Bonus Amount: ₹", bonus)


# ==============================
# Question 11: Simple ATM
# ==============================
balance = 1000
choice = int(input("\nQ11 - 1.Check Balance 2.Deposit 3.Withdraw: "))

if choice == 1:
    print("Balance: ₹", balance)
elif choice == 2:
    amt = int(input("Enter deposit amount: "))
    balance += amt
    print("Updated Balance: ₹", balance)
elif choice == 3:
    amt = int(input("Enter withdrawal amount: "))
    if amt <= balance:
        balance -= amt
        print("Updated Balance: ₹", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid option")


# ==============================
# Question 12: Greeting by Time
# ==============================
hour = int(input("\nQ12 - Enter hour (0-23): "))

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")


# ==============================
# Question 13: Celsius to Fahrenheit
# ==============================
c = float(input("\nQ13 - Enter Celsius: "))
f = (c * 9/5) + 32

print("Fahrenheit:", f)

if c > 30:
    print("Hot")
elif c >= 15:
    print("Moderate")
else:
    print("Cold")


# ==============================
# Question 14: Even or Odd
# ==============================
num = int(input("\nQ14 - Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==============================
# Question 15: Positive / Negative / Zero
# ==============================
num = int(input("\nQ15 - Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ==============================
# Question 16: Largest of Three Numbers
# ==============================
a = int(input("\nQ16 - Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("Largest:", max(a, b, c))


# ==============================
# Question 17: Vowel or Consonant
# ==============================
ch = input("\nQ17 - Enter character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# ==============================
# Question 18: Password Check
# ==============================
password = "python123"
user_pass = input("\nQ18 - Enter password: ")

if user_pass == password:
    print("Password Matched")
else:
    print("Incorrect Password")


# ==============================
# Question 19: Divisible by 5 and 11
# ==============================
num = int(input("\nQ19 - Enter number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")


# ==============================
# Question 20: Character Type
# ==============================
ch = input("\nQ20 - Enter character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
