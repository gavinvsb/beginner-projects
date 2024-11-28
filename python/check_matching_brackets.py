def is_matched(string: str):
    "Returns boolean whether inputted string contain matching angular brackets."
    mapper = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in string: # iterate over string
        if char in mapper:
            stack.append(mapper[char])
        elif char not in mapper.values():
            continue
        elif not (stack and char == stack.pop()):
            return False
    return not stack

test1 = "{{open}"
test2 = "[closedd]"
test3 = "]closed edge case"
test4 = "open edge case (p"
test5 = "(wjasdf) {{{[]}}}"

print(is_matched(test1), is_matched(test2), is_matched(test3), is_matched(test4), is_matched(test5))
