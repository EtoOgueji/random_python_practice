# while True:
#     try:
#         number = int(input("Name: "))
#         break
#     except ValueError:
#         print("No number entered")
#     except:
#         print('Unknown error occured')
#
# print("Thank you")

secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("You guess it")
        break