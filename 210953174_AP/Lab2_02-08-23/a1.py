
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    dp={0:0,1:1}
    for i in range(2,n+2):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n-1]

n=int(input("Enter n : "))
print("Nth Fibonacci Number: ",fibonacci(n))
