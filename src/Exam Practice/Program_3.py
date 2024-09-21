def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sort_by_last_element(sample_list)
print("Sorted list:", sorted_list)