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

def linear_search(list, t):  # O(n)
    return t in list

def fibonacci(n):  # O(n)
    if n < 0:
        return "Error: negative number"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
