def factorial(num):
    """Calculates and returns the factorial (num!)"""
    x = 1
    for i in range(1, num + 1):
        x *= i

    return x