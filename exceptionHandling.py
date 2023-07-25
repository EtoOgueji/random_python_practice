# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number> Try again...")
#     except (RuntimeError, TypeError, NameError):
#         pass

# class B(Exception):
#     pass
# class C(B):
#     pass
# class D(C):
#     pass
#
# for cls in [C, D, B]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)