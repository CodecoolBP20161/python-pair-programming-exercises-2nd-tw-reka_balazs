def palindrome(aaa):
    return aaa[::-1].lower().replace(" ", "") == aaa.lower().replace(" ", "")


def main():
    word = input("Enter a word: ")
    print(palindrome(word))
    return


if __name__ == '__main__':
    main()
