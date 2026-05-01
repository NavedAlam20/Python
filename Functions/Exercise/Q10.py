def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum_val = 0

    while temp > 0:
        digit = temp % 10
        sum_val += digit ** order
        temp //= 10

    return sum_val == num

num = int(input("Enter number: "))
print("Armstrong" if is_armstrong(num) else "Not Armstrong")