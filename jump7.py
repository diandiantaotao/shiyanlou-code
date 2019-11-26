for i in range(1,101):
    a=i%10
    b=i/10%10
    if a==7 or b==7:
        print(i)
        continue
    elif i%7==0:
        print(i)
