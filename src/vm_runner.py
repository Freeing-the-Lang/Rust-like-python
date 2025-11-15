from sponge_vm_bridge import run_on_sponge_vm


class VMRunner:
    def __init__(self):
        pass

    def run(self, ast):
        # Python AST → JSON 변환
        ast_json = self._ast_to_json(ast)
        return run_on_sponge_vm(ast_json)

    def _ast_to_json(self, ast_nodes):
        result = []

        for node in ast_nodes:
            result.append(self._expr_to_json_node(node))

        return result

    def _expr_to_json_node(self, node):
        t = type(node).__name__

        if t == "Let":
            return {
                "type": "let",
                "name": node.name,
                "expr": self._expr_to_json_node(node.expr)
            }

        if t == "Print":
            return {
                "type": "print",
                "expr": self._expr_to_json_node(node.expr)
            }

        if t == "Number":
            return {"type": "number", "value": node.value}

        if t == "Identifier":
            return {"type": "identifier", "name": node.name}

        if t == "BinaryOp":
            return {
                "type": "binary",
                "op": node.op,
                "left": self._expr_to_json_node(node.left),
                "right": self._expr_to_json_node(node.right),
            }

        raise Exception(f"Unknown AST node {t}")
