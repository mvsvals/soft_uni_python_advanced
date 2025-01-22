from functools import reduce

def operate(operator, *args):
    def sum_nums():
        return reduce(lambda x, y: x + y, args)
    def sub_nums():
        return reduce(lambda x, y: x - y, args)
    def mul_nums():
        return reduce(lambda x, y: x * y, args)
    def div_nums():
        return reduce(lambda x, y: x / y, args)

    mapper = {
        '+': sum_nums,
        '-': sub_nums,
        '*': mul_nums,
        '/': div_nums
    }
    return mapper[operator]()