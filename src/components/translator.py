from components.parsers import MyParser

class MyTranslator:
    def __init__(self):
        self.operators = {'*': 1, '/': 1, '+': 2, '-': 2, '(': 0}

    def is_operator(self, char):
        return char in self.operators

    def get_precedence(self, char):
        return self.operators[char]

    def translate(self, infix):

        # Reverse the infix expression
        reversed_infix = infix[::-1]
        modified_infix = ''
        for char in reversed_infix:
            if char == '(':
                modified_infix += ')'
            elif char == ')':
                modified_infix += '('
            else:
                modified_infix += char
        
        # Convert to postfix
        stack = []
        postfix = ''
        for char in modified_infix:
            if char.isalnum():
                postfix += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            elif self.is_operator(char):
                while stack and self.get_precedence(stack[-1]) >= self.get_precedence(char):
                    postfix += stack.pop()
                stack.append(char)

        while stack:
            postfix += stack.pop()

        # Reverse the postfix expression
        prefix = postfix[::-1]
        
        return prefix, postfix
