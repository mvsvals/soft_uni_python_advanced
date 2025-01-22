
def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for cheese, quantities in sorted_data:
        result += cheese + '\n'
        for quant in sorted(quantities, reverse=True):
            result += f'{quant}\n'
    return result

