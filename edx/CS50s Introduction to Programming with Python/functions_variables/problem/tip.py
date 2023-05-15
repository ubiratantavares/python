"""
@ author Ubiratan da SIlva Tavares
"""

def dollars_to_float(dollars):
    """
    dollars: dollar
    """
    value_string = dollars.replace('$', '')
    value_float = float(value_string)
    return value_float


def percent_to_float(percent):
    """
    percent
    """
    value_string = percent.replace('%', '')
    value_float = float(value_string)
    return value_float/100

def main():
    """
    função principal
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
