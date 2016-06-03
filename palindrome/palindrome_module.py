def palindrome(str):
    return str[::-1].lower().replace(" ", "") == str.lower().replace(" ", "")


def main():
    word = input("Enter a word to test if it is a palindrome: ")
    print(palindrome(word))
    return


if __name__ == '__main__':
    main()
