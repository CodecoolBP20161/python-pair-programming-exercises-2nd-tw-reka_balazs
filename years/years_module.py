import datetime


def years(age):
    remaining_years = 100 - age
    current_year = datetime.datetime.now()
    hundred_years = current_year.year + remaining_years
    return hundred_years


def main():
    name = input("What is your name?")
    age = int(input("What is your age?"))
    repeat = int(input("How many times to repeat the message?"))
    print(("You will be 100 years old in %d.\n" % years(age)) * repeat)
    return

    
if __name__ == '__main__':
    main()
