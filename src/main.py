from lexer import lex
from parser import Parser
from vm_runner import VMRunner

code = """
let x = 10
let y = x + 20
print y
"""

tokens = lex(code)
parser = Parser(tokens)
ast = parser.parse()

vm = VMRunner()
output = vm.run(ast)

print("Sponge VM Output:")
print(output)
