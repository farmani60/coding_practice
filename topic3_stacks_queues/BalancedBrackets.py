def isBalanced(expression):
    # Check if the expression is empty
    if not expression:
        print("No element in the input expression!")
    stack = list()
    for c in expression:
        if c == "{":
            stack.append("}")
        elif c == "[":
            stack.append("]")
        elif c == "(":
            stack.append(")")
        else:
            if (not stack) or (c != stack[-1]):
                return False
        stack.pop()
    return not stack