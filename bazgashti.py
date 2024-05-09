def odd_numbers(x):
    if x <= 300:
        if x % 2 != 0:
            print(x)
        odd_numbers(x+1)
odd_numbers(100)
