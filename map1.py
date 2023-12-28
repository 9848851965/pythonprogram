def sample(a):
    if a%2==0:
        return a*a
    else:
        return a*a*a
out=map(sample,[1,2,3,4,])
print(list(out))
