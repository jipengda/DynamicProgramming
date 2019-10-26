# The Longest Increasing Subsequence(LIS) problem is to find the
# length of the longest subsequence of a given sequence such that
# all elements of the subsequence are sorted in increasing order
# For example, the length of LIS for {10,22,9,33,21,50,41,60,80}
# is 6 and LIS is {10,22,33,50,60,80}

# Input : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

# Input : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}

# Input : arr[] = {50, 3, 10, 7, 40, 80}
# Output: Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}
import numpy as np
def lis(a):
    n = length(a)
    d = np.zeros(n+1, int)
    for i in range(n+1):
        d[i] = 1
    for i in range(0, n):
        for j in range(0, i):
            if (a[j] < a[i]):
                d[i] = max(d[i], d[j] + 1)

    ans = d[0]
    for i in range(1, n):
        ans = max(ans, d[i])

    return ans

# driver program to check the code
if __name__ == "__main__":
    number_array = list()
    number = input("Enter the number of elements you want:")
    print('Enter numbers in array:')
    for i in range(int(number)):
        n = input("number:")
        number_array.append(int(n))
    python = lis(number_array)
    print('Longest Increasing Subsequence is %d'%(python))
