nums = [1, 2, 3, 4, 5]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
    else:
        print("not found")

# prime number
num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")