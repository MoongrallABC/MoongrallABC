def smallest_number(a, b, c):
    return min(a, b, c)

num1 = float(input("876:"))
num2 = float(input("978: "))
num3 = float(input("1186: "))

smallest = smallest_number(num1, num2, num3)
print("The smallest number is: ", num2)