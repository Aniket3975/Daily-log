# Greedy Interval Scheduling Algorithm

def is_less_than(x1, y1, x2, y2):
    # Check if point (x1,y1) lies on the left side of line segment formed by (x2,y2)
    if x1 == x2:
        return False  # If points are same then not less than
    else:
        # Calculate slope
        m = (y2-y1)/(x2-x1)
        # Calculate y value
        y = m * (x1 - x2) + y1

        # Check if point lies on left side of line segment
        if y < y1:
            return True  # Point is less than line segment
        else:
            return False  # Point is not less than line segment


def comp_points(p1, p2):
    # Compare two points
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            return -1  # Less than
        else:
            return 1  # Greater than
    elif p1[0] > p2[0]:
        return -1  # Point 1 is less than point 2
    else:
        return 1  # Point 1 is greater than point 2


def greedy_interval(arr):
    n = len(arr)
    
    # Sort the interval array based on end value
    arr.sort(key=lambda x: (x[0], -x[1]))

    # Initialize result and curr end time
    res = []
    curr_end_time = float('-inf')

    for i in range(n):
        if is_less_than(arr[i][0], arr[i][1], curr_end_time, float('inf')):
            res.append(arr[i])
            curr_end_time = arr[i][1]

    return res


# Driver Code
if __name__ == "__main__":
    # Define intervals as a list of tuples (start, end)
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8)]
    print("Intervals:", intervals)

    print("Scheduling using Greedy Interval Scheduling Algorithm:")
    scheduled_intervals = greedy_interval(intervals)

    # Print the schedule
    for i in range(len(scheduled_intervals)):
        print(f"Interval {i+1}: Start={scheduled_intervals[i][0]}, End={scheduled_intervals[i][1]}")