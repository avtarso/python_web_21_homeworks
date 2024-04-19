import time
from multiprocessing import Pool, current_process, cpu_count

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


def callback(result):
    print(f"Result in callback: {result}")

if __name__ == "__main__":
    # numbers_list = [128, 255, 99999, 10651060]



    numbers_list = [789753159741, 900000000, 80000000000, 489368412987,
                    789753159741, 900000000, 80000000000, 489368412987,
                    789753159741, 900000000, 80000000000, 489368412987,
                    789753159741, 900000000, 80000000000, 489368412987]
    start_time = time.time()
    results = factorize(numbers_list)
    one_time = time.time() - start_time
    print("Results:", results)


    start_time = time.time()
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize,
            numbers_list,
            callback=callback
        )
        p.close()
        p.join()

    multi_time = time.time() - start_time
    print("Synchronous execution time:", one_time)
    print(f"Multi process (core count = {cpu_count()}) execution time:", multi_time)