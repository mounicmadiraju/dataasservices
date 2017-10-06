from . import data-structures


# 1. Stack application
def balanced_parentheses_checker(symbol_string):
    """Verify that a set of parentheses is balanced."""

    opening_symbols = '{[('
    closing_symbols = '}])'

    opening_symbols_stack = data_structures.Stack()
    symbol_count = len(symbol_string)
    counter = 0

    while counter < symbol_count:
        current_symbol = symbol_string[counter]
        if current_symbol in '{[(':
            opening_symbols_stack.push(current_symbol)
        else:
            if not opening_symbols_stack.is_empty() and \
            opening_symbols.index(opening_symbols_stack.peek()) == \
            closing_symbols.index(current_symbol):
                opening_symbols_stack.pop()
            else:
                counter = symbol_count

        counter += 1

    return opening_symbols_stack.is_empty() and counter == symbol_count

# 2. Stack application
def base_converter(decimal_num, base):
    """Convert a decimal number to base 2 or 8 or 16."""

    digits = '0123456789ABCDEF'
    remainder_stack = data_structures.Stack()
    conversion_result = ''

    while decimal_num > 0:
        remainder_stack.push(decimal_num % base)
        decimal_num = decimal_num // base

    while not remainder_stack.is_empty():
        conversion_result += digits[remainder_stack.pop()]

    return conversion_result


# 3. Queue application: Simulation of Hot Potato Game
def hot_potato(participants_list, num_of_passes):
    participants = data_structures.Queue(participants_list)

    while participants.size() > 1:
        for _ in range(num_of_passes):
            participants.enqueue(participants.dequeue())

        participants.dequeue()

    return participants.dequeue()


# 4. Deque application
def palindrome_checker(input_string):
    whitelist_char = 'abcdefghijklmnopqrstuvwxyz'
    cleaned_char = [x for x in input_string.lower() if x in whitelist_char]

    char_deque = data_structures.Deque(cleaned_char)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        if char_deque.remove_front() != char_deque.remove_rear():
            still_equal = False

    return still_equal



if __name__ == '__main__':
    print(balanced_parentheses_checker('[]{[]{([][])}()}'))
    [print(base_converter(233, base)) for base in [2, 8, 16]]
    print(hot_potato(['Mounic', 'Venu', 'Lekha', 'Dinesh', 'Raju', 'Madiraju'], 7))
    [print(palindrome_checker(x)) for x in ["radar", "lsdkjfskf", "Don I'm Don", "No lemon, no melon."]]
