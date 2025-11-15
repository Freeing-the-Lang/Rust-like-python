from ast import Let, Print, Number, Identifier, BinaryOp
from lex import Token


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, kind=None):
        tok = self.peek()
        if tok is None:
            return None
        if kind and tok.kind != kind:
            raise Exception(f"Expected {kind}, got {tok.kind}")
        self.pos += 1
        return tok

    def parse_stmt(self):
        tok = self.peek()

        if tok.kind == "IDENT" and tok.value == "let":
            self.consume()
            name = self.consume("IDENT").value
            self.consume("EQUAL")
            expr = self.parse_expr()
            return Let(name, expr)

        if tok.kind == "IDENT" and tok.value == "print":
            self.consume()
            expr = self.parse_expr()
            return Print(expr)

        raise Exception("Unknown statement")

    def parse_expr(self):
        left = self.parse_primary()
        tok = self.peek()

        if tok and tok.kind == "PLUS":
            self.consume()
            right = self.parse_primary()
            return BinaryOp(left, "+", right)

        return left

    def parse_primary(self):
        tok = self.consume()

        if tok.kind == "NUMBER":
            return Number(tok.value)

        if tok.kind == "IDENT":
            return Identifier(tok.value)

        raise Exception("Unexpected token in expression")

    def parse(self):
        stmts = []
        while self.peek():
            if self.peek().kind == "NEWLINE":
                self.consume()
                continue
            stmts.append(self.parse_stmt())
        return stmts
