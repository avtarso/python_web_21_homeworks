import sys


def int_one_arg_input(min_value: int, max_value: int) -> int:
    
    VALUE_RANGE = f"The range of acceptable values is between {min_value} and {max_value}."
    INPUT = f"Input number between {min_value} and {max_value} >>> "
    ERROR = "Error. You must enter a valid number."

    first_run = True

    while True:
        try:
            if first_run and len(sys.argv) > 1:
                one_arg_int = int(sys.argv[1])
            else:
                one_arg_int = int(input(INPUT))

            if min_value <= one_arg_int <= max_value:
                return one_arg_int
            else:
                print(VALUE_RANGE)
            
            first_run = False

        except ValueError:
            print(ERROR)
            first_run = False


def transform_data(data: list) -> str:
    
    result = ""
    
    if not data:
        return result

    for item in data:
        for date, currencies in item.items():
            for currency, rates in currencies.items():
                result += f"{currency} sale/purchase - {rates['sale']}/{rates['purchase']}\n"

    return result