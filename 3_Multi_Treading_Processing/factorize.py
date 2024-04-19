
def factorize(numbers):
    result = []

    # Check type 'number'. If it is not tuple or lis - wrape to tuple
    if not isinstance(numbers, (list, tuple)):
        numbers = (numbers,)

    for number in numbers:
        dividers_list = []
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                # Append divider only once if 'i == number'
                if i != number // i:
                    dividers_list.extend([i, number // i])
                else:
                    dividers_list.append(i)

        # Delete doubles and sort list of dividers
        dividers_list = sorted(set(dividers_list))
        result.append(dividers_list)

    return result



# run to check the functionality of the function
if __name__ == '__main__':

    numbers = (128, 255, 99999, 10651060)
    result  = factorize(numbers)

    assert result[0] == [1, 2, 4, 8, 16, 32, 64, 128]
    assert result[1] == [1, 3, 5, 15, 17, 51, 85, 255]
    assert result[2] == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert result[3] == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print("The function 'factorize' works correctly")

