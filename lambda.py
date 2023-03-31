def lambda_func(n):
    return lambda a : a + n
ans=lambda_func(10)
print(ans(100))