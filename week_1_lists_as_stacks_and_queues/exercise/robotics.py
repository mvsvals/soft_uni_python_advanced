from collections import deque


def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def seconds_to_time(seconds):
    seconds = seconds % 86400
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


robots = deque()
for robot in input().split(';'):
    name, time = robot.split('-')
    robots.append([name, int(time), 0])

products = deque()
h, m, s = [int(x) for x in input().split(':')]
current_seconds = time_to_seconds(h, m, s)

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_seconds += 1

while products:
    current_product = products.popleft()
    robot_found = False

    for i in range(len(robots)):
        robot = robots[i]
        robot_name = robot[0]
        process_time = robot[1]

        if current_seconds >= robot[2]:
            print(f"{robot_name} - {current_product} [{seconds_to_time(current_seconds)}]")
            robot[2] = current_seconds + process_time
            robot_found = True
            break

    if not robot_found:
        products.append(current_product)

    current_seconds += 1