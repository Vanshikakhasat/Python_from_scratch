a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("Greatest:", a)
elif b > c:
    print("Greatest:", b)
else:
    print("Greatest:", c)
