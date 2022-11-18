def main():
    while True:
        try:
            number = int(input("Please enter a number: "))
            if number % 2 == 0:
                print("The number is even")
            else:
                print("The number is odd")
        except ValueError:
            print("That is not a number")

main()
