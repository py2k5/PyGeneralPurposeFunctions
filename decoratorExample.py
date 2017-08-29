def logger(fun):
    print("Looging details for function {}".format(fun))
    def wrapper(*args):
        fun(args)
        return wrapper
    return logger

@logger
def fun1(inp_var):
    print("Testing the wrapper function {}".format(inp_var))


fun1(10)
