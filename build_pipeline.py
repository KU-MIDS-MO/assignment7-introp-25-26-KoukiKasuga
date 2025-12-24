def build_pipeline(operation_names):
    ### Replace with your own code (begin) ###
    operations = {
        "add_one": lambda x: x + 1,
        "square": lambda x: x * x,
        "double": lambda x: x * 2,
        "triple": lambda x: x * 3,
        "negate": lambda x: -x
    }

    functions = []
    

    for name in operation_names:
        if name not in operations:
            raise KeyError(f"Unknown operation: {name}")
        functions.append(operations[name])

    def pipeline(value):
        for f in functions:
            value = f(value)
        return value
    
    return pipeline
    pass


#fails

#Did not raise error
"""
    def add_one(x):
        return x + 1
    def square(x):
        return x * x
    def double(x):
        return x * 2
    def triple(x):
        return x * 3
    
    operations = {
        "add_one": add_one,
        "square": square,
        "double": double,
        "triple": triple
    }

    def pipeline(value):
        for name in operation_names:
            if name not in operations:
                raise KeyError(f"Unknown operation: {name}")
            value = operations[name](value)
        return value
    
    return pipeline
"""

#Did not raise error
"""  
    def pipeline(x):
        for op in operation_names:
            if op == "double":
                x = x * 2
            elif op == "triple":
                x = x * 3
            elif op == "square":
                x = x ** 2
            else:
                raise KeyError("Unknown Operation.")
        return x
    return pipeline
"""
    
    ### Replace with your own code (end)   ###
