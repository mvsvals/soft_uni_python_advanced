from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())
final_feed_collection = []

while suggested_links and featured_articles:
    fifo_element = suggested_links.popleft()
    lifo_element = featured_articles.pop()
    if fifo_element > lifo_element:
        remainder = fifo_element % lifo_element
        final_feed_collection.append(-remainder if remainder > 0 else remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)
    elif lifo_element > fifo_element:
        remainder = lifo_element % fifo_element
        final_feed_collection.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        final_feed_collection.append(0)


total_engagement_value = sum(final_feed_collection)

print("Final Feed: ", end='')
print(', '.join(str(x) for x in final_feed_collection))

if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")
