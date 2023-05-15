"""
@ author David Malan
"""

def square(number):
    """
    function square
    """
    return number * number


def main():
    """
    function main
    """
    value_x = int(input("What's x? "))
    print("x squared is", square(value_x))

main()
