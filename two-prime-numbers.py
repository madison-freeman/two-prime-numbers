# Return two prime numbers

# Given an even number N (greater than 2), return two prime numbers whose sum will be equal to given number.
# There are several combinations possible. Print only the pair whose minimum value is the smallest among
# all the minimum values of pairs and print the minimum element first.

import math

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


class Solution:
    def primeDivision(self, N):
        # code here
        i = 2
        while 1:
            if isprime(i) and isprime(N - i):
                return i, N - i
            i += 1
# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1, end=" ")
        print(p2)
# } Driver Code Ends