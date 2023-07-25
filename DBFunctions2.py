# def mult_divide(num1, num2):
#     return (num1 * num2), (num1 / num2)
#
# mult, divide = mult_divide(5, 4)
#
# print("5 * 4 =", mult)
# print("5 / 4 =", divide)

# creating a list of primes

listOfPrimes = []

for i in range(2, 11):
    is_prime = True

    # to check if a number has any divisors from 2 up to the sqrt of the number
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
            listOfPrimes.append(i)

print(listOfPrimes)

# Note: If a number is divisible by 2 (other than 2 itself), then it is not a prime number