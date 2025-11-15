class Expr:
    pass


class Number(Expr):
    def __init__(self, value):
        self.value = value


class Identifier(Expr):
    def __init__(self, name):
        self.name = name


class BinaryOp(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Stmt:
    pass


class Let(Stmt):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class Print(Stmt):
    def __init__(self, expr):
        self.expr = expr
