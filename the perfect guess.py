# To guess a number by the user:
import random
r1=random.randint(1,100)

for i in range(1,1000000):
    n = int(input("enter the number: "))
    if (r1>n):
         print("the entered number is low:\n")

    elif(r1<n):
        print("the entered number is too high:\n")

    elif(r1==n):
        print("********Congratulations!you have guessed the number*********")
        print(f"you have guessed the number in {i}attempts")
        break;





