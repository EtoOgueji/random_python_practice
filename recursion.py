# def factorial(num):
#
#     if num <= 1:
#         return 1
#     else:
#
#         result = num * factorial(num - 1)
#         return result
#
# print("4! =", factorial(4))

# fibonacci

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:

        result = fib(x - 1) + fib(x - 2)
        return result

numFibValues = int(input("How many fibonacci values should be found: "))

i = 1

while i < numFibValues:
    fibValue = fib(i)

    print(fibValue)

    i += 1

print("All Done")