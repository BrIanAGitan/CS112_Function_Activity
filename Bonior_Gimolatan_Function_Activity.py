def multi():
    if num1 == num2 != num3:
        bab = (num1 * num2) + num3
        print(f"The result is: {bab}")
    elif num2 == num3 != num1:
        bab = (num2 * num3) + num1
        print(f"The result is: {bab}")
    elif num1 == num3 != num2:
        bab = (num1 * num3) + num2
        print(f"The result is: {bab}")
    elif num1 != num2 != num3:
        sad = num1 + num2 + num3
        print(f"The result is: {sad}")
    elif num1 == num2 == num3:
        bab = num1 * num2 * num3
        print(f"The result is: {bab}")
    else:
        print("Invalid Result:")


num1 = eval(input("Input First Number:\n"))
num2 = eval(input("Input Second Number:\n"))
num3 = eval(input("Input Third Number:\n"))

multi()