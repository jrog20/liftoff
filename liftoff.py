"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    """
    Using a for loop, this program will count down from 10 to 1.
    """

    for i in range(10, 0, -1):
        print(i)
    print("Liftoff!")


if __name__ == "__main__":
    main()
