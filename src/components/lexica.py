from sly import Lexer

class MyLexer(Lexer):
    """
    MyLexer is a class that inherits from sly.Lexer
    It is used to tokenize the input string.
    ref: https://sly.readthedocs.io/en/latest/sly.html#sly-sly-lex-yacc
    

    Python regEX: https://www.w3schools.com/python/python_regex.asp
    """

    # Set of token names
    tokens = { NUMBER, PLUS, MINUS, DIVIDE, TIMES, LPAREN, RPAREN}

    # Regular expression rules for tokens
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    LPAREN  = r'\('
    RPAREN  = r'\)'

    # Ignore spaces and tabs 
    ignore = ' \t'

    # Extra action for newlines
    @_(r'\n+')
    def ignore_newline(self, t):
        # https://sly.readthedocs.io/en/latest/sly.html#line-numbers-and-position-tracking
        self.lineno += t.value.count('\n')

    def error(self, t):
        self.index += 1
        print(f"ERROR: Illegal character '{t.value[0]}' at line {self.lineno}")
