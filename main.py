# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def guessing_game(max_num, max_guess):
    half_num = max_num // 2
    correct_num = random.randint(0, max_num)
    print(correct_num)
    while max_guess > 0:
        num = int(input("Please guess a number:  \n"))

        if num == correct_num:
            print(f"Correct! You have finally gotten the number after {11 - max_guess} guess(es)")

            break
        elif 9 > max_guess > 6:
            if correct_num <= half_num:
                print(f"Number is less than {half_num + 1}")
            else:
                print(f"Number is greater than {half_num}")
        elif max_guess < 5:
            if correct_num % 2 == 0:
                print("The number is even")
            else:
                print("The number is odd")
        else:
            print("Incorrect")

        max_guess -= 1
        print("*" * 40)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    guessing_game(3, 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
