#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if a certain grandmother will allow the user to date her grandchild through the user's age


def main():
    # Finds if a certain grandmother will allow the user to date her grandchild through the user's age

    age = input("Enter your age: ")
    try:
        age_int = int(age)
        if age_int >= 25 and age_int <= 40 and not age_int < 0:
            print("\nThis grandmother will approve of you dating her grandchild.")
        elif age_int > 25 or age_int < 40 and not age_int < 0:
            print("\nThis grandmother will not approve of you dating her grandchild.")
        else:
            print("\nError: {} is not a proper age.".format(age_int))
    except ValueError:
        print("\nError: {} is not an integer.".format(age))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
