def sample(a):
    if  'A'<=a <='Z':
        return True
    else:
        return False
out=filter(sample,('aBc@123$Chguh'))
print(list(out))
