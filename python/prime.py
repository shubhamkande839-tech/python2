a=int(input("enter the number = "))

if a<=1:
    print("the given number is not a prime number")
else:
    for i in range(2,a):
        if a % i ==0:
            print("the given number is not a prime number")
            break
        else:
            print("given number is prime")