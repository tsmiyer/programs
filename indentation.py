#Question 3
def indent():
    x=int(input(" According to the indentation structure of the source code, enter as coloumn numbers : "))
    cols = x
    check = 0
    while(x>0):
        no = x%10
        check = check*10 + no
        x=x//10
    if (cols == check):
        print("Valid Indentation")
        return True
    else :
        print("Invalid Indentation")
        return False
result = indent()
print(result)