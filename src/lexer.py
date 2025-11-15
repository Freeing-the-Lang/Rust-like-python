class Token:
    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"Token({self.kind}, {self.value})"


def lex(code):
    tokens = []
    current = ""

    def flush_current():
        nonlocal current
        if current:
            if current.isdigit():
                tokens.append(Token("NUMBER", int(current)))
            else:
                tokens.append(Token("IDENT", current))
            current = ""

    for c in code:
        if c.isdigit():
            current += c
        elif c.isalpha():
            current += c
        elif c == "+":
            flush_current()
            tokens.append(Token("PLUS"))
        elif c == "=":
            flush_current()
            tokens.append(Token("EQUAL"))
        elif c == "\n":
            flush_current()
            tokens.append(Token("NEWLINE"))
        elif c in [" ", "\t"]:
            flush_current()
        else:
            pass

    flush_current()
    return tokens
