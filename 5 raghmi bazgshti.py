def reverse_decimal_number(number):
    if len(number) == 1:
        return number
    else:
        return number[-1] + reverse_decimal_number(number[:-1])

decimal_number = input("add 5 raghmi ashari vared konid: ")
while len(decimal_number) < 5:
    decimal_number = input("dobare add 5 raghmi ashari vared konid: ")

reversed_number = reverse_decimal_number(decimal_number)
print("add varone: ", reversed_number)