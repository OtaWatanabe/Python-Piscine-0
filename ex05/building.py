import sys


def main():
    """This program counts the number of upper letters,
    lower letters, punctuation marks, spaces and digits in a given text."""
    if 2 < len(sys.argv):
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n") + "\n"
    else:
        text = sys.argv[1]

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    all_count = 0

    for char in text:
        all_count += 1
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            punctuation_count += 1

    print(f"The text contains {all_count} characters")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
