#mclexer.py

r'''
El papel de un analizador léxico es convertir texto sin procesar en símbolos 
reconocidos conocidos como tokens.

Se requiere que el analizador léxico de MiniC reconozca los siguientes 
símbolos. El nombre sugerido del token está a la izquierda. El texto 
coincidente está a la derecha.


Palabras Reservadas:
    STATIC  : 'static'
    EXTERN  : 'extern'
    INT     : 'int'
    FLOAT   : 'float'
    CHAR    : 'CHAR'
    CONST   : 'const'
    RETURN  : 'return'
    BREAK   : 'break'
    CONTINUE: 'continue'
    IF      : 'if'
    ELSE    : 'else'
    WHILE   : 'while'
    FOR     : 'for'
    TRUE    : 'true'
    FALSE   : 'false'
    INT     : 'int'
    CHAR    : 'char'
    STRING  : 'string'
    INCLUDE : 'include'


    ...

Identificadores:
    ID      : Texto iniciando con una letra o '_' seguido de cualquier 
              número de letras, digitos o '_'. 
              Ejemplo: 'abc' 'ABC' 'abc123' '_abc' 'a_b_c'

Literales:
    INUMBER : 123 (decimal)

    FNUMBER : 1.234
              .1234
              1234.

    CHARACTER:'a' (un solo caracter - byte)
              '\xhh' (valor byte)
              '\n' (newline)
              '\'' (literal comilla simple)

    STRING  : "cadena" (varios caracteres entre comilla doble)
              permite secuenciads de escape como: '\n', '\t\, etc..


Operadores:
    PLUS    : '+'
    MINUS   : '-'
    TIMES   : '*'
    DIVIDE  : '/'
    LT      : '<'
    LE      : '<='
    GT      : '!
    GE      : '>='
    EQ      : '=='
    NE      : '!='
    LAND    : '&&'
    LOR     : '||'
    LNOT    : '!'
    MOD     : '%'


Simbolos Miselaneos
    ASSIGN  : '='
    SEMI    : ';'
    LPAREN  : '('
    RPAREN  : ')'
    LBRACE  : '{'
    RBRACE  : '}'
    COMMA   : ','
    ELIPSIS : '...'
    ADD     : '+='
    SUS     : '-='
    MULT    : '*='
    DIVI    : '/='
    PERC    : '%='


Comentarios: Deben ser ignorados
    //          Ignora el resto de la linea
    /* ... */   Ignora un bloque (no se permite anidar)

Errores: Su lexer puede opcionalmente reconocer e informar los siguientes 
mensajes de error:

    lineno: character 'c' ilegal
    lineno: constante de caracter no terminada
    lineno: comentario sin terminar

'''

from  sly import Lexer

class MyLexer(Lexer):

    tokens = {
    #Palabras Reservadas:
    ID,STATIC,EXTERN,INT,FLOAT,CHAR,CONST,RETURN,BREAK,CONTINUE,IF,ELSE,WHILE,FOR,TRUE,FALSE,STRING,INCLUDE,NUMBER,FNUMBER,CHARACTER,STRING,
    #Operadores:
    PLUS,MINUS,TIMES,DIVIDE,LT,LE,GE,EQ,NE,LAND,LOR,LNOT,MOD,   
    #Simbolos Miselaneos
    ASSIGN,SEMI,LPAREN,RPAREN,LBRACE,RBRACE,COMMA,ELIPSIS,ADD,SUS,MULT,DIVI,PERC,
    }

    literals = '+-*/%<>!=;,(){}[]'

    #Ignorar espacios en blanco
    ignore = ' \t\r'

    #ignorar comentarios
    ignore_lineacomment = r'//.*\n'
    ignore_BLOCKcomment = r'/\*(.|\n)*\*/'

    #Identificador
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    #Palabras reservadas
    ID['static'] = STATIC
    ID['extern'] = EXTERN
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['string'] = STRING
    ID['return'] = RETURN
    ID['char'] = CHARACTER
    #Operadores:
    NUMBER = r'\d+'
    PLUS   = r'\+'
    MINUS  = r'\-'
    TIMES  = r'\*'
    DIVIDE = r'\/'
    LT     = r'\<'
    LE     = r'\<='
    GE     = r'\>='
    EQ     = r'\=='
    NE     = r'\!='
    LAND   = r'\&&'
    LOR    = r'\|\|'
    LNOT   = r'\!'
    MOD    = r'\%'
    STRING = r'".*"'
    RETURN = r'STRING|\d'
    CHAR = r'"\'+\'"'

    

    #Simbolos Miselaneos
    ASSIGN  = r'\='
    SEMI    = r'\;'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACE  = r'\{'
    RBRACE  = r'\}'
    COMMA   = r'\,'
    ELIPSIS = r'\...'
    ADD     = r'\+='
    SUS     = r'\-='
    MULT    = r'\*='
    DIVI    = r'\/='
    PERC    = r'\%='
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('error at Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

from prettytable import PrettyTable

if __name__ == '__main__':
    file = open("parcero.c","r")
    data = file.read()
    lexer = MyLexer()
    types,values,lines = [], [], []
    for tok in lexer.tokenize(data):
        types.append(tok.type)
        values.append(tok.value)
        lines.append(tok.lineno) 
    myTable = PrettyTable(["TYPE", "VALUE", "LINE"])
    types,values,lines
    table = []
    for i in range(len(values)):
        row = [ types[i] , values[i] , lines[i]]
        myTable.add_row(row)

    print(myTable)
       
    file.close()
