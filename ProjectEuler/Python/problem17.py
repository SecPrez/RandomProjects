# def min_swaps_to_balance(s):
#     stack = []
#     swaps = 0

#     for char in s:
#         if char == "[":
#             stack.append(char)
#         elif char == "]":
#             if stack:
#                 stack.pop()
#             else:
#                 swaps += 1

#     if len(stack) != swaps:
#         return -1
#     else:
#         return swaps + len(stack) // 2


# # Test cases
# # print(min_swaps_to_balance("[]"))  # 0
# # print(min_swaps_to_balance("]][["))  # -1
# # print(min_swaps_to_balance("[[]]"))  # 0
# # print(min_swaps_to_balance("[]]["))  # 1
# print(min_swaps_to_balance("][][[]]["))  # 1


def min_swaps_to_balance_andrew(s):

    closing_out_of_place = 0
    stack = []
    for char in s:
        if char == "[":
            stack.append(char)
        elif char == "]":
            if stack:
                stack.pop()
            else:
                closing_out_of_place += 1
    if len(stack) != closing_out_of_place:
        return -1
    else:
        return closing_out_of_place


print(min_swaps_to_balance_andrew("][][[]]["))
print(min_swaps_to_balance_andrew(""))
print(min_swaps_to_balance_andrew("["))
print(min_swaps_to_balance_andrew("[[]]]["))


def has_duplicates(arr):
    distinct_elements = set()
    for element in arr:
        if element in distinct_elements:
            return True
        distinct_elements.add(element)

    return False


# print(has_duplicates([1, 2, 3, 1]))
# print(has_duplicates([1, 2, 3, 4]))
# print(has_duplicates([1, 2, 3, 1]))
# print(has_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# print(has_duplicates([]))
# print(has_duplicates(["a", "a"]))
# print(has_duplicates(["a", 1]))
# print(has_duplicates(["a", 1]))
