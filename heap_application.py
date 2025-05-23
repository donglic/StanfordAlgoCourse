import heapq

# Read numbers from the file
with open("/mnt/data/median.txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

# Heaps for maintaining the lower and upper halves
low = []   # Max-heap (invert values to simulate max behavior with min-heap)
high = []  # Min-heap

medians = []

for num in numbers:
    # Insert into appropriate heap
    if not low or num <= -low[0]:
        heapq.heappush(low, -num)
    else:
        heapq.heappush(high, num)

    # Rebalance the heaps so that len(low) >= len(high)
    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

    # The median is always the max of the lower half (i.e., top of max-heap)
    medians.append(-low[0])

# Compute the final result modulo 10000
result = sum(medians) % 10000
print("Result:", result)
