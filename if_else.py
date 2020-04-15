a=int(input("Enter a = "))
b=int(input("Enter b = "))

if a > b:
    print("a is grater than b")
elif b > a:
    print("b is grater than a")
else:
    print("a equal to b")

if a>b and a < 1000:
    print("b < a <1000")
elif a>1000 or a>500:
    print("a = ",a)


