while True:
    number = input("")
    if number == "0":
        break
    if number != number[::-1]:
        print("no")
    else:
        print("yes")
