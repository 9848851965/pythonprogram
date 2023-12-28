def sample(a):
    if a%2==0:
        return True
    else:
        return False
out=filter(sample,(1,2,3,4,55,6,7,8,9))
print(list(out))