# Write an efficient program to find the sum of contiguous subarray
# within a one-dimensional array of numbers which has the largest
# sum
# For example,
# For array {-2, -3, 4, -1, -2, 1, 5, -3}
# Largest is 4 + (-1) + (-2) + 1 + 5 = 7
# Maximum Contiguous Array Sum is 7
import math
def maxContiguousArraySum(a):
    n=len(a)
    local_max = 0
    global_max = -(math.inf)

    for i in range(n):
        local_max = max(a[i], a[i]+local_max)
        if (local_max > global_max):
            global_max = local_max
    return global_max

# driver program to check the code
if __name__=="__main__":
    number_array = list()
    number = input("Enter the number of elements you want:")
    print('Enter numbers in array:')
    for i in range(int(number)):
        n = input("number:")
        number_array.append(int(n))
    sum = maxContiguousArraySum(number_array)
    print("Maximum Contiguous Array Sum is %d"%(sum))
