import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except:
        print('cannot open')