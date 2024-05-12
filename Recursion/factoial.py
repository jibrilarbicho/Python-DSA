def factorial(n):
    assert n>=0 and int(n)==n ,"The number must be integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(32))