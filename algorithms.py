def factorial(n):  # O(n)
    if n < 0:
        return "Error: negative number"
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

