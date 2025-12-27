def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

n = int(input("Enter a number: "))

result = reverse_number(n)
print("Reversed number =", result)
