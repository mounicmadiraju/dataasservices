def unsorted_sequential_search(haystack, needle):
    endpoint = len(haystack)
    counter = 0
    found = False

    while counter < endpoint and not found:
        if haystack[counter] == needle:
            found = True
        else:
            counter += 1

    return found

def sorted_sequential_search(haystack, needle):
    endpoint = len(haystack)
    counter = 0
    found = stop = False

    while counter < endpoint and not (found or stop):
        if haystack[counter] == needle:
            found = True
        elif needle < haystack[counter]:
            stop = True
        else:
            counter += 1

    return found

def binary_search(haystack, needle):
    if len(haystack) == 0:
        return False

    midpoint = len(haystack) // 2

    if haystack[midpoint] == needle:
        return True

    if needle > haystack[midpoint]:
        return binary_search(haystack[midpoint + 1:], needle)
    else:
        return binary_search(haystack[:midpoint], needle)
