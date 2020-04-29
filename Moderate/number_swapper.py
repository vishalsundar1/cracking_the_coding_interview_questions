''' number swapper pseudocode
we take 2 variables that need to be swapped
we then have a choice to either subtraction or XOR it.
XOR is better as we improve range of data types that can be used to swap
let a = 101 and b=110 be our variables
a = a^b 101^110=011
b = a^b 011^110=101->b
a = a^b 011^101 = 110
 '''

def swap_numb(a, b):
    a = a - b
    print( a , b)
    b = b + a
    print( a , b)
    a = b - a 
    print( a , b)
    return a, b

def swap_numb_XOR(c , d):
    c = c^d
    print (c , d)
    d = c^d
    print(c, d)
    c = c^d
    print(c, d)
    return c, d

n = swap_numb(9, 6)
xor = swap_numb_XOR(10, 5)
print (n)