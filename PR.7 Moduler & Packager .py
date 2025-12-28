import datetime
import time
import math
import random
import uuid
import os

# ================= DATETIME & TIME =================
def datetime_menu():
    while True:
        print("\nDatetime and Time Operations")
        print("1. Display current date and time")
        print("2. Date difference")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        ch = input("Enter your choice: ")

        if ch == "1":
            now = datetime.datetime.now()
            print("Current Date and Time:", now)

        elif ch == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            print("Difference:", abs((date2 - date1).days), "days")

        elif ch == "3":
            now = datetime.datetime.now()
            print("Formatted Date:", now.strftime("%d-%m-%Y %H:%M:%S"))

        elif ch == "4":
            input("Press Enter to start stopwatch")
            start = time.time()
            input("Press Enter to stop")
            end = time.time()
            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif ch == "5":
            sec = int(input("Enter seconds: "))
            for i in range(sec, 0, -1):
                print(i)
                time.sleep(1)
            print("Time's up!")

        elif ch == "6":
            break


# ================= MATH =================
def math_menu():
    while True:
        print("\nMathematical Operations")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")

        ch = input("Enter your choice: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            t = float(input("Time: "))
            ci = p * (1 + r / 100) ** t
            print("Compound Interest:", round(ci, 2))

        elif ch == "3":
            angle = math.radians(float(input("Enter angle: ")))
            print("Sin:", math.sin(angle))
            print("Cos:", math.cos(angle))
            print("Tan:", math.tan(angle))

        elif ch == "4":
            r = float(input("Radius: "))
            print("Area:", math.pi * r * r)

        elif ch == "5":
            break


# ================= RANDOM =================
def random_menu():
    while True:
        print("\nRandom Data Generation")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. OTP")
        print("5. Back")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Random Number:", random.randint(1, 100))

        elif ch == "2":
            lst = [random.randint(1, 50) for _ in range(5)]
            print("Random List:", lst)

        elif ch == "3":
            length = int(input("Password length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$"
            password = "".join(random.choice(chars) for _ in range(length))
            print("Password:", password)

        elif ch == "4":
            otp = random.randint(1000, 9999)
            print("OTP:", otp)

        elif ch == "5":
            break


# ================= UUID =================
def generate_uuid():
    print("Generated UUID:", uuid.uuid4())


# ================= FILE OPERATIONS =================
def file_menu():
    while True:
        print("\nFile Operations")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        ch = input("Enter your choice: ")

        if ch == "1":
            fname = input("File name: ")
            open(fname, "w").close()
            print("File created")

        elif ch == "2":
            fname = input("File name: ")
            data = input("Enter data: ")
            with open(fname, "w") as f:
                f.write(data)
            print("Written successfully")

        elif ch == "3":
            fname = input("File name: ")
            with open(fname, "r") as f:
                print(f.read())

        elif ch == "4":
            fname = input("File name: ")
            data = input("Enter data: ")
            with open(fname, "a") as f:
                f.write("\n" + data)
            print("Appended")

        elif ch == "5":
            break


# ================= DIR EXPLORATION =================
def explore_module():
    name = input("Enter module name: ")
    try:
        module = __import__(name)
        print(dir(module))
    except:
        print("Module not found")


# ================= MAIN MENU =================
def main():
    while True:
        print("\n=== Multi Utility Toolkit ===")
        print("1. Datetime & Time")
        print("2. Math Operations")
        print("3. Random Data")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank you for using the toolkit!")
            break


if __name__ == "__main__":
    main()
