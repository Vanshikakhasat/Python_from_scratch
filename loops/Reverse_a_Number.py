num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reverse =", rev)
