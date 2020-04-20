# this is a comment.
a=int(input("Enter a ="))
while a > 10:
    if a <= 100:
        print("a = ",a)
    else:
        break
    a=a+1
else:
    print("a < 10 = ", a)
print("exit of while loop")