# print("fn: ", __name__)
def my_sum(*args):
    if len(args) > 2:
        return -sum(args)
    else:
        return 1

