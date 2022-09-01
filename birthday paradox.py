#Question 2
x=int(input("Enter the number of people in the room : "))

def date (n):
    q= 1
    if n>0 and n%5==0 and n<=100:
        for i in range(1, n):
            probability = i/ 365
            q *= (1 - probability)
        p = 1-q
        print ("The probability of two people having same birthday in a room of",x,"is : " ,p)
    else:
        print("Invalid Input , Enter in multiples of 5 and less than 100 ")
date(x)