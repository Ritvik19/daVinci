def pyeval(x):
    try:
        return eval(x)
    except Exception as e:
        return str(e)
