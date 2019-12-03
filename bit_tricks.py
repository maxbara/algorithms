# For example, the number (01010000) would turn into (01011111)
def rightPropagateRightMostOne(x):
    
    return x | (x - 1)

# determines whether an interger is a power of 2
def isPowerOfTwo(x):
    
    return 0 == x & (x - 1)
    
# computes x mod (power of 2). For example, returns 13 for 77 mod 64
def modForAPowerOfTwo(x, aPowerOfTwo):
    
    return x & (aPowerOfTwo - 1)
    
# tests if n-th bit (nth, 3th, 2th, 1th, 0th) is set
def isNthBitSet(x, n):

    return (x >> n) & 1

# sets the nth bit (nth, 4th, 3th, 2th, 1th, 0th) to 1
def setNthBit(x, n):

    return x | (1 << n)

# turn off rightmost bit
def turnOffRightmostBit(x):

    return x & (x - 1)

# isolates the rightmost set bit    
def isolateRightmostSetBit(x):

    return x & ~(x - 1)

# adds 1
def addOne(x: int):
    
    k = 1   
    # flip all set bits to zero until finding a zero to flip
    while x & k:       
        x ^= k      
        k <<= 1
    
    # flip the rightmost 0 bit to zero
    x ^= k    
    return x
 
# multiples a times b using bitwise and addition operators
def russianPeasantMultiplication(a, b):
    
    res = 0
    
    while b > 0:
        
        if b & 1:
            
            res += a
          
        a <<= 1
        b >>=  1
    
    return res

# adds bit strings together, and returns a bit string with the total
def addBitStrings( first, second ): 
    
    # Helper method: makes length of bit strings equal
    def makeEqualLength(str1, str2): 
  
        len1 = len(str1)
        len2 = len(str2)
        if len1 < len2: 
            str1 = (len2 - len1) * '0' + str1 
            len1 = len2 
        elif len2 < len1: 
            str2 = (len1 - len2) * '0' + str2 
            len2 = len1 
        return len1, str1, str2 
    
    result = ''
  
    length, first, second = makeEqualLength(first, second) 
  
    carry = 0
    for i in range(length - 1, -1, -1): 
        firstBit = int(first[i]) 
        secondBit = int(second[i]) 
  
        # is bit 1 or 0, among 3 bits
        sum = (firstBit ^ secondBit ^ carry) + 48
        result = chr(sum) + result 
  
        # do we need a carry?
        carry = (firstBit & secondBit) |  (secondBit & carry) | (firstBit & carry) 
  
    # overflow
    if carry == 1: 
        result = '1' + result 
    return result

# xor operation without xor
def xorOperation(a: int, b: int)-> int:
    
    return (a | b) & (~a | ~b)


# Tests for these functions
print()
print(bin(40))
print(bin(rightPropagateRightMostOne(40))) 
    
print()
print(isPowerOfTwo(3))
print(isPowerOfTwo(128))
print(isPowerOfTwo(99))

print()
print(modForAPowerOfTwo(77, 64))
print(modForAPowerOfTwo(19, 4))

print()
print(bin(40))
for i in range(0, 6):
    
    print(isNthBitSet(40, i))

print()   
print(bin(32))
print(bin(setNthBit(32, 3)))
    
print()
print(bin(40))
print(bin(turnOffRightmostBit(40)))

print()
print(isolateRightmostSetBit(40))

print(addOne(7))
print(addOne(8))
print(addOne(12))

print(russianPeasantMultiplication(3, 9))

str1 = '1100101'
str2 = '1011'
print('Sum is', addBitStrings(str1, str2)) 

print(xorOperation(10, 7))
