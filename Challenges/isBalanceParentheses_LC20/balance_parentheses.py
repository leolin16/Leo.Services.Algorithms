def balanced(strs):
    stack = []
    for i in range(len(strs)):
        if strs[i] == "(" or  strs[i] == "{" or  strs[i] == "[":
            stack.append(strs[i])
        elif strs[i] == ")" and (len(stack) == 0 or stack.pop() != "("):
            return False
        elif strs[i] == "]" and (len(stack) == 0 or stack.pop() != "["):
            return False
        elif strs[i] == "}" and (len(stack) == 0 or stack.pop() != "{"):
            return False
    return len(stack) == 0

print('Input: "()", Output: ', balanced("()"))
print('Input: "()[]{}", Output: ', balanced("()[]{}"))
print('Input: "(]", Output: ', balanced("(]"))
print('Input: "([)]", Output: ', balanced("([)]"))
print('Input: "{[]}", Output: ', balanced("{[]}"))