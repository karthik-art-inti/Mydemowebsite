def add(a1,*v):
    a=type(v[0])
    print(a)
    
    sum = a(a1)
    
    for i in v:
        a2=a(i)
        sum=sum+a2
    return sum

print(add(23,"Hi"," welcome"," to python.",2.3))



#first paramater will go into first argument in the function definition "fargs"
#rest all argument will go into *args as a sequence data type

