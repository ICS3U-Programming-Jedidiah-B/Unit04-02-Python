# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: April 18 2022

def main():
    # values
    loop_counter = 0
    factorial_answer = 1

    try:
        # user input
        user_number = int(input("Enter a positive number: "))
        # negative input catch
        if user_number < 0:
            print("input cannot be negative")
        # loop
        while True:
            # process
            loop_counter = loop_counter + 1

            factorial_answer = factorial_answer * loop_counter
            # output
            print("{} * {}".format(factorial_answer, loop_counter))
            print("Tracking {} times through loop.".format(loop_counter))
            if loop_counter >= user_number:
                print("{} ! = {}".format(loop_counter, factorial_answer))
                break
    # invalid input catch
    except ValueError:
        print("invalid input")
    finally:
        print("thank you for using this program")


if __name__ == "__main__":
    main()
