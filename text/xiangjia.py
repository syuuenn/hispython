def sum(n):
    a=2
    x=1
    s=a*n
    y=1
    while x<n:
        a=a*10
        s=s+a*(n-y)
        y+=1
    print(s)
sum(2)

