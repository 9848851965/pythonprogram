def indexvowel(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if a[i] in "aeiouAEIOU":
            out=out+[i]
    return out
f=indexvowel("gireesh")
print(f)