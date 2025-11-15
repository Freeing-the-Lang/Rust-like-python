class Runtime:
    def __init__(self):
        self.env = {}

    def set_var(self, name, value):
        self.env[name] = value

    def get_var(self, name):
        return self.env.get(name, None)
