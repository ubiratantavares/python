"""
@ author David Malan
"""

def main():
    """
    function main
    """
    name = input("What's your name? ")
    hello(name)


def hello(to_message="world"):
    """
    function hello
    """
    print("hello,", to_message)


if __name__ == "__main__":
    main()
