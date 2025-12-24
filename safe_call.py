def safe_call(func, a, b):
    ### Replace with your own code (begin) ###
    try:
        result = func(a, b)
        return True, result, None
    except (ZeroDivisionError, TypeError, ValueError, IndexError, KeyError) as error:
        return False, None, type(error).__name__  
    pass
    ### Replace with your own code (end)   ###
