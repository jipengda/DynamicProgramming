#Ugly numbers are numbers whose only prime factors are 2,3 or 5. The sequence 1,
#2,3,4,5,6,,8,9,10,12,15,...shows the first 11 ugly numbers. By convention, 1 is
#included

#Given a number n,the task is to find n'th Ugly number.
#Examples:
#Input : n = 7
#Output: 8
#Input : n = 10
#Output: 12

#Input : n = 15
#Output: 24

#Input : n = 150
#Output: 5832

# Recommened: Please solve it on "PRACTICE" first, before moving on to
# the solution
import numpy as np
def uglyNumber(n):
        # f2 maintains the index of the ugly number
        # for multiplication by 2
        f2 = 1;
        # f3 maintains the index of the ugly number
        # for multiplication by 3
        f3 = 1;
        # f5 maintains the index of the ugly number
        # for multiplication by 5
        f5 = 1;
        dp = np.zeros(n+1, int)
        # first ugly number is 1
        dp[1] = 1;
        # filling the dp matrix from i = 2
        for i in range(2, n+1):
            # calculating the next number from previous ugly numbers
            ans_f_2 = dp[f2] * 2;
            ans_f_3 = dp[f3] * 3;
            ans_f_5 = dp[f5] * 5;
            # finding minimum of all the answer
            final_ans = min(ans_f_2, min(ans_f_3, ans_f_5))
            #storing the ans
            dp[i] = final_ans;
            # if our final_ans is ans_f_2, ans_f_3, ans_f_5
            # then increment their counters i.e f2, f3, f5
            if(final_ans == ans_f_2):
                    f2 = f2 + 1;

            if(final_ans == ans_f_3):
                    f3 = f3 + 1;

            if(final_ans == ans_f_5):
                    f5 = f5 + 1;
        return dp[n];

# driver program to check the code
if __name__=="__main__":
    n = input("Enter number n: ")
    n = int(n)
    uglyNumber = uglyNumber(n)
    print("The %dth ugly number is %d" % (n, uglyNumber))
