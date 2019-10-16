int fun(int n){
    if(n == 1 || n == 2)
        return n;
    if(!dp[n-1])
        dp[n-1] = fun(n-1);
    if(!dp[n-2])
        dp[n-2] = fun(n-2);
    return dp[n-1] + dp[n-2];
}
