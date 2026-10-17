
def infix_to_postfix(expression):
    stack = []
    postfix = ""

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[ch] or
                    (precedence[stack[-1]] == precedence[ch] and ch != '^'))):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


expression = input("Enter infix expression: ")
print("Postfix expression:", infix_to_postfix(expression))

