
a = input(" Enter a Number: ")


try:
    int(a)
    a = int(a)
    if a % 5 == 0 and a % 2 == 0:
        print("Saad")

    elif a % 5 == 0:
        print("Qamer")

    elif a % 2 == 0:
        print("Bari")

    else:
        print("Sultani")

except ValueError:
    print("This is not a number.")


