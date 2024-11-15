# Accept a positive integer n as input and print the smallest integer that is
# divisible by all the integers in the range [1, n], endpoints inclusive.



def gcd(a,b): 
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def lcm(a,b):
    return (a*b) //gcd (a,b)

def lcm_n(n):
    ans = 1
    for i in range(1,n+1) :
        ans = lcm(ans, i)
    return ans
n = int(input("Enter a positive integer: "))
print (lcm_n(n))