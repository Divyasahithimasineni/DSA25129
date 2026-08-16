def power(p, n):
    if n == 0:
        return 1

    return p * power(p, n - 1)

p = int(input("Enter principal/base value: "))
n = int(input("Enter number of years/power: "))

print("Result =", power(p, n))
