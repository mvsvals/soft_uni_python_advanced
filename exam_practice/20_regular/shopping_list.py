def shopping_list(budget, **kwargs):
    output = []
    if budget < 100:
        return "You do not have enough budget."
    for product, data in kwargs.items():
        if len(output) == 5:
            break
        total_cost = data[0] * data[1]
        if total_cost <= budget:
            output.append(f"You bought {product} for {total_cost:.2f} leva.")
            budget -= total_cost

    return '\n'.join(output)


