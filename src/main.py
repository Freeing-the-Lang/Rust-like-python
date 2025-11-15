from lexer import lex
from parser import Parser
from interpreter import Interpreter

code = """
let x = 10
let y = x + 20
print y
"""

tokens = lex(code)
parser = Parser(tokens)
stmts = parser.parse()

interpreter = Interpreter()
interpreter.run(stmts)
