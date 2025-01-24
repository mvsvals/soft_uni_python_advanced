def neg_vs_positive(*args):
    pos_sum = sum(int(x) for x in args if int(x) > 0)
    neg_sum = sum(int(x) for x in args if int(x) < 0)
    print(neg_sum)
    print(pos_sum)
    if abs(neg_sum) > abs(pos_sum):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

neg_vs_positive(*input().split())