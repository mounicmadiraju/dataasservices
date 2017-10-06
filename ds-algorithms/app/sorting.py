def bubble_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    for pass_num in range(len(arr_list) - 1, 0, -1):
        for j in range(pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[j + 1]:
                arr_list[j], arr_list[j + 1] = arr_list[j + 1], arr_list[j]
                num_of_exchanges += 1 # For bigO benchmarking

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


def short_bubble_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    exchange = True
    pass_num = len(arr_list) - 1

    while pass_num > 0 and exchange:
        exchange = False
        for j in range(pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[j + 1]:
                exchange = True
                arr_list[j], arr_list[j + 1] = arr_list[j + 1], arr_list[j]
                num_of_exchanges += 1 # For bigO benchmarking

        pass_num -= 1

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


def selection_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    for pass_num in range(len(arr_list) - 1, 0, -1):
        pos_max = 0
        for j in range(1, pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[pos_max]:
                pos_max = j

        arr_list[pass_num], arr_list[pos_max] = arr_list[pos_max], arr_list[pass_num]
        num_of_exchanges += 1 # For bigO benchmarking

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


def sublist_insertion_sort(arr_list, start_index=0, gap=1):
    # For bigO benchmarking
    num_of_comparison = 0

    for pass_num in range(start_index + gap, len(arr_list), gap):
        current_value = arr_list[pass_num]
        position = pass_num

        while position > start_index and arr_list[position - gap] > current_value:
            num_of_comparison += 1 # For bigO benchmarking
            arr_list[position] = arr_list[position - gap]
            position -= gap

        arr_list[position] = current_value

    # In general, a shift operation requires approximately a third of the
    # processing work of an exchange since only one assignment is performed.
    return num_of_comparison


def insertion_sort(arr_list):
    num_of_comparison = sublist_insertion_sort(arr_list)

    return '%s comparisons and %s shifts.' % (num_of_comparison, num_of_comparison) # For bigO benchmarking


def shell_sort(arr_list):
    num_of_sublists = len(arr_list) // 2
    num_of_comparison = 0

    while num_of_sublists > 0:
        for start_index in range(num_of_sublists):
            num_of_comparison += sublist_insertion_sort(arr_list, start_index=start_index, gap=num_of_sublists)

        num_of_sublists //= 2

    return '%s comparisons and %s shifts.' % (num_of_comparison, num_of_comparison) # For bigO benchmarking


def merge_sort(arr_list):
    if len(arr_list) > 1:
        mid = len(arr_list) // 2

        # splitting takes place here
        left_list = arr_list[:mid]
        right_list = arr_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        # merging begins here
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr_list[k] = left_list[i]
                i += 1
            else:
                arr_list[k] = right_list[j]
                j += 1

            k += 1

        while i < len(left_list):
            arr_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            arr_list[k] = right_list[j]
            j += 1
            k += 1


def quick_sort(arr_list):
    quick_sort_helper(arr_list, 0, len(arr_list) - 1)

def quick_sort_helper(arr_list, first_index, last_index):
    if first_index < last_index:
        # Unlike merge_sort, no additional storage is required as the list is partitioned
        split_point_index = partition(arr_list, first_index, last_index)

        quick_sort_helper(arr_list, first_index, split_point_index - 1)
        quick_sort_helper(arr_list, split_point_index + 1, last_index)

def partition(arr_list, first_index, last_index):
    pivot_value = arr_list[first_index]
    left_mark = first_index + 1
    right_mark = last_index

    quit = False
    while not quit:
        while left_mark <= right_mark and arr_list[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and arr_list[right_mark] >= pivot_value:
            right_mark -= 1

        if left_mark > right_mark:
            quit = True
        else:
            arr_list[left_mark], arr_list[right_mark] = arr_list[right_mark], arr_list[left_mark]

    arr_list[first_index], arr_list[right_mark] = arr_list[right_mark], arr_list[first_index]

    return right_mark


if __name__ == '__main__':
    import timeit

    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    sorted_list = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    sorting_algos = [
        bubble_sort, short_bubble_sort, selection_sort,
        insertion_sort, shell_sort, merge_sort, quick_sort
    ]

    for sorting_algo in sorting_algos:
        print('{}: {} ms, {}'.format(
                sorting_algo.__name__,
                timeit.timeit(
                    '%s(%s)' % (sorting_algo.__name__, unsorted_list),
                    setup='from __main__ import %s' % sorting_algo.__name__,
                    number=1000
                ),
                sorting_algo([54, 26, 93, 17, 77, 31, 44, 55, 20])
            )
        )
