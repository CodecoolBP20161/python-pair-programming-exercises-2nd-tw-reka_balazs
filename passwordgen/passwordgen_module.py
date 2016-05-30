import random
import string


def passwordgen(diff=""):
    result = ""
    if diff == "weak":
        weakpw = ["poopyhead123", "sleepyface1990", "ihavenoidea"]
        result = random.choice(weakpw)
    else:
        chars = string.ascii_letters + string.digits + "*-+_!?"
        strongpw = "".join(random.choice(chars) for _ in range(random.randrange(8, 21)))
        result = strongpw
    return result


def main():
    while True:
        request = input("Request new password? (Y/N)")
        if request == "Y":
            diff = input("Strenght of password? (weak/strong)")
            print(passwordgen(diff))
        else:
            break
    return


if __name__ == '__main__':
    main()
