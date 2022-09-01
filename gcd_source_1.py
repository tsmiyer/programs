#Let us define a function by name gcd1
# The function gcd1 determines the greatest common divisior of two numbers
#ASSUMPTION:  m>0 and n>0
#Algorithm of gcd1(m,n)
def gcd1(m,n):

#Step1:  Pass m, n as arguments to gcd1

#step2:  set the list of factors  factorsOf_m to an empty list
    factorsOf_m = []
    
#Step3:  set the list of factors  factorsOf_n to an empty list
    factorsOf_n = []

#Step4:  set the list of common factors of m and n factorsOf_mn to empty
    factorsOf_mn = []


#Step5: for each factor of m 
#           append factor to factorsOf_m
    for i in range(1,m+1):
        if (m%i == 0):
            factorsOf_m.append(i)
            

#Step6: for each factor of n
#           append factor to factorsOf_n
    for i in range(1,n+1):
        if (n%i == 0):
            factorsOf_n.append(i)

#Step7: for each factor present in factorsOf_m
#           if factor is also presnet in factorsOf_n
#                     append factor to factorsOf_mn
    for i in factorsOf_m:
        if i in factorsOf_n:
            factorsOf_mn.append(i)
            

#Step8:  determine the maximum factor in factorsOf_mn and return as the gcd
    print(factorsOf_mn[-1])

gcd1(260,110);

#HOMEWORK
  # gcd(0,x) = x   (we assume x>0)
  # Can you extend the above algorithm/code to see that program behaves
  # correctly when either m or n is equal to 0  but not both?
 #  What should you do for the case where both m==0 and n==0?