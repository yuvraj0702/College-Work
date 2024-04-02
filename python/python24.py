import sys
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except:
    print("Enter a string")
    sys.exit()

print(x**y)