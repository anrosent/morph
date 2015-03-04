#!/usr/bin/env python
sys = __import__("sys")
ast = __import__("ast")
time = __import__("time")
astunparse = __import__("astunparse")
__builtins__ = eval("__builtins__")

def execute():
    print("do")

def transform(s):

    salt = hash(time.time())

    def hashname(n):
        h = abs(hash(n) + salt)
        return 'v_' + str(h)

    m = ast.parse(s)
    for node in ast.walk(m):
        if isinstance(node, ast.Name):
            if node.id not in dir(__builtins__):
                node.id = hashname(node.id)
        elif isinstance(node, ast.FunctionDef):
            node.name = hashname(node.name)
    return m

with open(sys.argv[0], 'r+') as f:
    execute()
    s = transform(f.read())
    f.seek(0)
    f.truncate()
    f.write('#!/usr/bin/env python\n')
    f.write(astunparse.unparse(s))
