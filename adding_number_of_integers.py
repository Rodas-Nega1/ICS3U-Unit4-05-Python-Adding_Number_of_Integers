# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user to pick a number of integers
# and sums all of those integers


def main():
    # this function loops a sum of inputted positive integers
    # and eliminates the negatives from the sum if the user enters
    # a negative integer

    # loop variable
    integer_sum = 0
    sum = 0

    # input
    user_number = input("Enter in the number of integers to add: ")
    print("")

    # process & output
    try:

        user_number_int = int(user_number)

        for integer_sum in range(user_number_int):
            user_number = input("Enter in integer: ")
            user_number_int = int(user_number)

            if user_number_int < 0:
                continue

            sum = sum + user_number_int

        print("")
        print("The sum is {0}.".format(sum))

    except Exception:
        print("That is an invalid response.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
