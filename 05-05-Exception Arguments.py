# Demo 05-05
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Args:
        print("Argument doesn’t a numbers\n", Args.args)

temp_convert("Thailand")


