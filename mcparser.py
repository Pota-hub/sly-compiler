from sly import Parser,Lexer 
from mclexer import MyLexer

class CalcParser(Parser):
    tokens = MyLexer.tokens
    
    def __init__(self):
        self.id = {}
    
    expr = ''
    ''' giving error so far
    @_(' ID "=" expr')
    def statement(self,p):
        self.ids[p.id] = p.expr
    '''
    @_(r'ID')
    def statement(self,p):
        print(p.expr)
    @_(r'INT NUMBER')
    def statement(self,p):
        return  int(number)
        
if __name__ == '__main__':
    lexer = MyLexer()
    parser = CalcParser()
    file = open("parcero.c","r")
    data = file.read()
    for tok in lexer.tokenize(data):
        '''
            types.append(tok.type)
            values.append(tok.value)
            lines.append(tok.lineno) 
        '''
       