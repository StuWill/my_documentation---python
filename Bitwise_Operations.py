print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

# Can use int() functions 2nd parameter to choose what base the number being converted is to
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)

print int("0b11001001",2)

# Left and right shift bitwise operators
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right) # prints 0b11
print bin(shift_left) # prints 0b100

# And Operator (like an AND gate, a&b bits are only turned on when both a and b have a 1)
#      a:   00101010   42
#      b:   00001111   15       
#       ===================
#  a & b:   00001010   10

print bin(0b11100 & 0b101) # prints 0b100

# Or Operator (like an OR gate, a|b bits  only turn on when either a or b or both have a 1)
#     a:  00101010  42
#     b:  00001111  15       
#      ================
# a | b:  00101111  47

# Xor Operator (like an eXclusiveOR gate, a^b bits only turn on when either a or b but not both have a 1)
#     a:  00101010   42
#     b:  00001111   15       
# ================
# a ^ b:  00100101   37

# Not Operator (add 1 to the bit and flip its sign)
# ~3 = -4

# Masks are ways to check if bits are off
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"#
# Masks can also turn on bits, using Or operator
# Xor operators with masks can be used to flip bits

# Flip bit function
def flip_bit(number, n): #input a number and the bit that needs to be flipped
  mask = 0b1
  result = number ^ (mask << n-1)
  return bin(result)
  




