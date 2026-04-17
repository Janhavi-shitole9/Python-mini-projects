# Even Odd Checker

while True:
    num = input("Enter number (or q to quit): ")

    if num == 'q':
        break

    num = int(num)

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
