from operator import itemgetter

# ##### EXAMPLE 1 ##### #
# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Cannot divide by 0.")
#     return dividend / divisor


# def calculate(*values, operator):
#     return operator(*values)


# # calling the name of the function as the operator, not calling a str value
# result = calculate(20, 4, operator=divide)
# print(result)


# ##### EXAMPLE 2 ##### #
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Zac Sol", "age": 30},
    {"name": "Nico Cam", "age": 30},
    {"name": "Tea Str", "age": 30},
]


def get_friend_name(friend):
    return friend["name"]


# print(search(friends, "Zac Sol", get_friend_name))
print(search(friends, "Zac Sol", itemgetter("name")))
