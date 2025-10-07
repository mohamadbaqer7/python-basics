#functions
def factorial(n):  # O(n)
    if n < 0:
        return "Error: negative number"
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x

def find_max(list):  # O(n)
    if not list:
        return "Error: empty list"
    max = list[0]
    for x in list[1:]:
        if x > max:
            max = x
    return max

def linear_search(list, t):  # O(n).
    return t in list

def fibonacci(n):  # O(n).
    if n < 0:
        return "Error: negative number"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

#login in and menu system

users = {}
logged_user = None

while True:
    print("\n1.Factorial  2.Find Max  3.Linear Search  4.Fibonacci  5.Login/Register  6.Logout  7.Exit")
    choice = input("Choice: ").strip()

    # must login first
    if choice in {"1", "2", "3", "4"} and not logged_user:
        print("Please login first.")
        continue

    if choice == "1":
        print(factorial(int(input("n: "))))
    elif choice == "2":
        nums = [int(x) for x in input("numbers: ").split()]
        print(find_max(nums))
    elif choice == "3":
        nums = [int(x) for x in input("numbers: ").split()]
        print(linear_search(nums, int(input("target: "))))
    elif choice == "4":
        print(fibonacci(int(input("n: "))))
    elif choice == "5":
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username in users:
            if users[username] == password:
                logged_user = username
                print(f"Welcome back, {username}!")
            else:
                print("Wrong password.")
        else:
            users[username] = password
            logged_user = username
            print(f"New account created for {username}. You are now logged in.")
    elif choice == "6":
        if logged_user:
            print(f"User '{logged_user}' logged out.")
            logged_user = None
        else:
            print("No user is currently logged in.")
    elif choice == "7":
        print("Thank you for using my app.")
        break
    else:
        print("Invalid choice.")
