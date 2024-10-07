def find_two_smallest(input_list):
    if len(input_list) < 2:
        raise ValueError("at least two integers.")
    smallest = float('inf')
    second_smallest = float('inf')
    for number in input_list:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest:
            second_smallest = number
    return smallest, second_smallest