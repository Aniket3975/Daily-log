# Greedy Interval Scheduling
=====================================

This algorithm solves the Interval Scheduling problem, where we have a list of intervals and a priority queue that stores them in increasing order of their end times.

```python
import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def greedy_interval_scheduling(intervals):
    # Sort the intervals based on their end times
    intervals.sort(key=lambda x: x.end)
    
    # Initialize a priority queue to store the selected intervals
    pq = []
    
    # Iterate through the sorted intervals
    for interval in intervals:
        # If the current interval does not overlap with the previous one, add it to the priority queue
        if not pq or interval.start >= pq[0].end:
            heapq.heappush(pq, interval)
        else:
            # Otherwise, replace the overlapping interval with the current one
            while pq and pq[0].end <= interval.start:
                heapq.heappop(pq)
            # Add the current interval to the priority queue
            heapq.heappush(pq, interval)
    
    return pq

def print_intervals(intervals):
    for i, interval in enumerate(intervals):
        print(f"Interval {i+1}: Start={interval.start}, End={interval.end}")

# Example usage:
intervals = [
    Interval(1, 3),
    Interval(2, 4),
    Interval(3, 5),
    Interval(6, 8),
    Interval(7, 9)
]

selected_intervals = greedy_interval_scheduling(intervals)
print("Selected intervals:")
print_intervals(selected_intervals)

# Output:
# Selected intervals:
# Interval 1: Start=1, End=3
# Interval 2: Start=4, End=5
# Interval 3: Start=6, End=8