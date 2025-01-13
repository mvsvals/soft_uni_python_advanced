
delivery = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_needed = 0


while delivery:
    current_capacity = rack_capacity
    racks_needed += 1
    while delivery and delivery[-1] <= current_capacity:
        current_capacity -= delivery.pop()


print(racks_needed)


