def isBalanced(expression):
    if not expression:
        print("Input expression is empty!")
    stack = []
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