def sample(a):
        if type(a) in [list,str,tuple,set,dict]:
            return len(a)
        else:
            return a
out=map(sample,[1,(4,5),[7,9],{1:2,'a':5}])
print(list(out))