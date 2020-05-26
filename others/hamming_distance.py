# The Hamming distance between two integers is the number of
# positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

def convert_binary(self, n):
    """Convert decimal number n to binary."""
    if n > 1:
        self.convert_binary(n // 2)
    print(n % 2)


# Bitwise XOR sets the bits in the result to 1 if either,
# but not both, of the corresponding bits in the two operands is 1.
# Example: 1 ^ 3 ====> bin(1) = 1 and bin(3) = 11 ==> 1 ^ 11 = 01
#          decimal(01) = 2 ===> 1 ^ 3 = 2
# Example: 2 ^ 3 ====> bin(2) = 01 and bin(3) = 11 ==> 01 ^ 11 = 10
#          decimal(10) = 1 ===> 2 ^ 3 = 1
# Example: 1 ^ 4 ====> bin(1) = 1 and bin(4) = 001 ==> 1 ^ 001 = 101
#          decimal(101) = 5 ===> 1 ^ 4 = 5
# Example: 9 ^ 5 ====> bin(9) = 1001 and bin(5) = 101 ==> 1001 ^ 101 = 0011
#          decimal(0011) = 12 ===> 9 ^ 5 = 12

class Solution( object ):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
