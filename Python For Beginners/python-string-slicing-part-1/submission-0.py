def get_substring(input_string: str, start: int, end: int) -> str:
    result = input_string[start:end]

    if result == None:
        return ""
    elif end > len(input_string):
        return ""
    else:
        return result

# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
