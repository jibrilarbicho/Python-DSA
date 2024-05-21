def power(base,exp):

    assert exp>=0 and int(exp)==exp ,"The number must be integer"
    if exp==0:
        return 1
    


    return base*power(base,exp-1)
print(power(4,2))