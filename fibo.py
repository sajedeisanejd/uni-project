def fibo(nums):
    x=0
    y=1
    count=0
    if nums <= 0:
        print('please enter adad mosbt')
    elif nums == 1:
        print(x)
    else:
        while count < nums:
            print(x)
            z=x+y
            x=y
            y=z
            count += 1
print(fibo(30))