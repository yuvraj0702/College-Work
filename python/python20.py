try:
    n = int(input("Enter a no: "))
    print(n**2)
except KeyboardInterrupt:
    print("program interupted")
except ValueError:
    print("Enter a string")