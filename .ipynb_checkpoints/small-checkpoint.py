from find_small import find_two_smallest
from lists_int import list1, list2, list3, list4
lists = [list1, list2, list3, list4]
results = []
for integer_list in lists:
    smallest_two = find_two_smallest(integer_list)
    results.append(smallest_two)
with open('result.txt', 'w') as file:
    for result in results:
        file.write(f"{result}\n")