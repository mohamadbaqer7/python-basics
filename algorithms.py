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
#login in and system part

users = {}
logged = False

while True:
    print("\n1.Factorial  2.Find Max  3.Linear Search  4.Fibonacci  5.Login  6.Exit")
    c = input("Choice: ").strip()

    if c in {"1","2","3","4"} and not logged:
        print("Please login first.")
        continue
    if c == "1": 
        print(factorial(int(input("n: "))))
    elif c == "2":
        nums = [int(x) for x in input ("numbers: ").split()]
        print(find_max(nums))
    elif c == "3":
        nums = [int(x) for x in input("numbers: ").split()]
        print(linear_search(nums,int(input("target: "))))
    elif c == "4":
        print(fibonacci(int(input("n: "))))
    elif c == "5":
        u = input("Username: ").strip()
        p = input("Password: ").strip()
        if u in users:
            if users[u] == p:
                logged = True
                print("Logged in.")
            else:
                print("Wrong password.")
        else:
            users[u] = p
            logged = True
            print("User saved and logged in.")
    elif c == "6":
        print("Thank you for using my app")
        break
    else:
        print("Invalid.")
        