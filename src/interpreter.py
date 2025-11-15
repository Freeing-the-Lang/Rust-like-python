from ast import Number, Identifier, BinaryOp, Let, Print
from runtime import Runtime


class Interpreter:
    def __init__(self):
        self.rt = Runtime()

    def eval_expr(self, expr):
        if isinstance(expr, Number):
            return expr.value

        if isinstance(expr, Identifier):
            return self.rt.get_var(expr.name)

        if isinstance(expr, BinaryOp):
            left = self.eval_expr(expr.left)
            right = self.eval_expr(expr.right)
            if expr.op == "+":
                return left + right

        raise Exception("Unknown expression")

    def run_stmt(self, stmt):
        if isinstance(stmt, Let):
            value = self.eval_expr(stmt.expr)
            self.rt.set_var(stmt.name, value)

        elif isinstance(stmt, Print):
            value = self.eval_expr(stmt.expr)
            print(value)

    def run(self, stmts):
        for s in stmts:
            self.run_stmt(s)
