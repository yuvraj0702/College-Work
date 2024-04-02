import sys
try:
    x = (sys.argv[1])
    y = (sys.argv[2])
except:
    print("Enter a string in command line")
    sys.exit()

print(x+y) 