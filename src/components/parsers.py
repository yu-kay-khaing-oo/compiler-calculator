from components.lexica import MyLexer
from sly import Parser

class MyParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    precedence = (
        ('left', TIMES, DIVIDE),
        ('left', PLUS, MINUS),
        ('right', UMINUS),
        )

    # Grammar rules and actions
    @_('expr')
    def statement(self, p) -> int:
        return p.expr

    @_('term TIMES expr')
    def expr(self, p):
        return p.term * p.expr

    @_('term DIVIDE expr')
    def expr(self, p):
        try:
            return p.term // p.expr
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

    @_('term')
    def expr(self, p):
        return p.term

    @_('factor PLUS term')
    def term(self, p):
        return p.factor + p.term

    @_('factor MINUS term')
    def term(self, p):
        return p.factor - p.term
    
    @_('factor')
    def term(self, p):
        return p.factor

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    @_('NUMBER')
    def factor(self, p):
        return int(p.NUMBER)
    
    # https://sly.readthedocs.io/en/latest/sly.html#dealing-with-ambiguous-grammars
    # `%prec UMINUS` is the way to override the `precedence` of MINUS to UMINUS.
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr
