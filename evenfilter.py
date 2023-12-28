def sample(a):
    for i in a:
        if type[i] in [int and float and complex and bool] :
            yield i
out=filter(sample,([(1,2),(2,3),{4,5},'gireesh']))
print(list(out))