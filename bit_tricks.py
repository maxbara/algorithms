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
