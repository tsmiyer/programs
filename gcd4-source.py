#15, 10
#10, (15-10)
# gcd(10,15) = gcd(5,10)
#18,12
#12, (18-12)
#12, 6
#gcd(18,12) = gcd(6,12)
#gcd(95,90) = gcd(90,(95-90)) = gcd(90,5)=(gcd(
# gcd(6,5)=gcd(5,1)=gcd((5-1),1)=(gcd(4-1),1)=(gcd(3-1),1)=(gcd(2-1),1)=(gcd(1,1)
def gcd4(m,n):
    
    while True:
        if (m<n):
            (m,n)=(n,m)
        if (m==n):
            print (m)
        else:
            m=m-n
gcd4(220,535);