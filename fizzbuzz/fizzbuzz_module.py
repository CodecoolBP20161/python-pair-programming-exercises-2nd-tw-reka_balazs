def fizzbuzz(number):
    to_return = ""
    if number % 3 == 0:
        to_return = "Fizz"
    if number % 5 == 0:
        to_return += "Buzz"
    return to_return or number


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
