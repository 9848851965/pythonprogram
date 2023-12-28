def view(a):
    for i in a:
        if type(i) in [list,str,tuple,dict]:
            yield len(i)
        else:
            yield i
out=view([1,[4,5,6],{7,8},'efg',{'a':2},9,5,12])
print(list(out))